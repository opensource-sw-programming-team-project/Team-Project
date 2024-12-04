from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from konlpy.tag import Okt
import time
import requests
from hanspell import spell_checker
import re
from concurrent.futures import ThreadPoolExecutor
import random
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
CORS(app)
okt = Okt()

from data_store import(
    time_zones,
    country_code,
    capital_mapping,
    stopwords,
    intents,
    book_list,
    movie_list,
    music_list,
    fortune_telling_list,
    emotion_anger_list,
    emotion_boredom_list,
    emotion_joy_list,
    emotion_sadness_list,
    famous_saying_list,
    activity_list,
    idiom_list,
    adage_saying_list,
    drama_list,
    webtoon_list,
    jokes
)

# 전처리 함수(불용어 제거)
def preprocess(text):
    tokens = okt.morphs(text)
    keywords = [word for word in tokens if word not in stopwords]
    return keywords

# intents의 단어들 토큰화
sentences = []
for keywords in intents.values():
    for sentence in keywords:
        sentences.append(preprocess(sentence))

# Word2Vec 모델 학습
model = Word2Vec(list(intents.values()), vector_size=50, window=3, min_count=1, workers=4)

# 단어 벡터 생성
def get_word_vector(word, model):
    try:
        return model.wv[word]
    except KeyError:
        return np.zeros(model.vector_size)

# 입력과 각 의도 간 유사도 계산
def calculate_intent_similarity(user_input):
    user_words = preprocess(user_input)
    user_vectors = [get_word_vector(word, model) for word in user_words]
    
    best_intent = None
    max_similarity = 0
    threshold=0.5

    for intent, keywords in intents.items():
        intent_vectors = [get_word_vector(word, model) for word in keywords]
        
        # 유사도 계산
        similarities = []
        for user_vector in user_vectors:
            for intent_vector in intent_vectors:
                if np.linalg.norm(user_vector) != 0 and np.linalg.norm(intent_vector) != 0:
                    similarity = cosine_similarity([user_vector], [intent_vector])[0][0]
                    similarities.append(similarity)

        if similarities and max(similarities) > max_similarity and max(similarities) >= threshold:
            max_similarity = max(similarities)
            best_intent = intent
    return best_intent

    
# 마침표,물음표,마침표 기준으로 문장 분리
def split_sentences(text):
    sentences = re.split(r'(?<=[.?!,])\s+', text.strip())
    return sentences

# 연결어를 포함한 명사-조사 결합 분리
def split_with_morpheme(sentence):
    tokens = okt.pos(sentence)
    split_parts = []
    for word, pos in tokens:
        if pos == "Josa" and word in ["와", "과","이랑","랑"]:
            split_parts[-1] += word  # 앞의 명사에 붙임
        else:
            split_parts.append(word)
    return split_parts

# 연결어를 기준으로 문장 분리
def split_with_connectors_and_morpheme(sentence):
    split_parts = split_with_morpheme(sentence)
    results = []
    current_part = []
    ends_with_tuple = ("와", "과", "이랑", "랑")
    connectors = ["그리고"]
    negations = ["말고","빼고","아니고"]  # 부정어구 리스트

    for word in split_parts:
        if word in connectors or word.endswith(ends_with_tuple):
            current_part.append(word)
            results.append(" ".join(current_part))
            current_part = []
        elif word in negations:
            # 부정어구가 등장하면 앞의 내용을 무시하고 부정어구부터 시작
            current_part = [word]
        else:
            current_part.append(word)

    if current_part:
        results.append(" ".join(current_part))
    return [part for part in results if part]  # 빈 문자열 제거
    return results

#오타 및 맞춤법 교정
def spellcheck(text):
    correct_message = spell_checker.check(text)
    return correct_message.checked

# Weather API 함수
def weather_api(country_name):
    # OpenWeatherMap API Key
    api_key = '76709f4e1bf2023762668cf9b449c3b3'

    # 국가명에 따른 수도의 좌표 선택
    capital_coordinate = capital_mapping.get(country_name, None)
    
    # 좌표 변수 설정
    latitude = capital_coordinate['latitude']
    longitude = capital_coordinate['longitude']

    # Weather API URL
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&lang=kr'  # 한국어 지원

    # 데이터 가져오기
    weather_information = requests.get(weather_api_url)
    weather_data = weather_information.json()

    # 질문에 따른 응답 생성
    if weather_information.status_code == 200:
        weather_response = f"{country_name}의 현재 날씨는 {weather_data['weather'][0]['description']}, 기온은 {weather_data['main']['temp'] - 273.15:.1f}°C입니다."
    else:
        weather_response = f"날씨 정보를 가져올 수 없습니다: {weather_data.get('message', '알 수 없는 오류')}."

    return weather_response

# Air Pollution API 함수
def air_pollution_api(country_name):
    # OpenWeatherMap API Key
    api_key = '76709f4e1bf2023762668cf9b449c3b3'

    # 국가명에 따른 수도의 좌표 선택
    capital_coordinate = capital_mapping.get(country_name, None)
    
    # 좌표 변수 설정
    latitude = capital_coordinate['latitude']
    longitude = capital_coordinate['longitude']

    # Air Pollution API URL
    air_pollution_api_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={api_key}'

    # 데이터 가져오기
    air_pollution_information = requests.get(air_pollution_api_url)
    air_pollution_data = air_pollution_information.json()

   # 질문에 따른 응답 생성
    if air_pollution_information.status_code == 200:
        air_pollution_response = f"{country_name}의 현재 미세먼지(PM10) 농도는 {air_pollution_data['list'][0]['components']['pm10']:.1f}, 초미세먼지(PM2.5) 농도는 {air_pollution_data['list'][0]['components']['pm2_5']:.1f}입니다."
    else:
        air_pollution_response = f"미세먼지 정보를 가져올 수 없습니다: {air_pollution_data.get('message', '알 수 없는 오류')}."

    return air_pollution_response

# 감정 응답 함수들
def emotion_joy():
    return random.choice(emotion_joy_list)
def emotion_sadness():
    return random.choice(emotion_sadness_list)
def emotion_anger():
    return random.choice(emotion_anger_list)
def emotion_boredom():
    return random.choice(emotion_boredom_list)
# 오늘의 운세
def random_fortune_telling():
    return f"오늘의 운세🔮\n{random.choice(fortune_telling_list)}"
# 오늘의 명언
def random_famous_saying():
    famous_saying = random.choice(famous_saying_list)
    return f'오늘의 명언💬\n"{famous_saying["명언"]}", {famous_saying["명언가"]}'
# 오늘의 사자성어
def random_idiom():
    return f"오늘의 사자성어💭\n'{random.choice(idiom_list)}'"
# 오늘의 속담
def random_adage_saying():
    return f"오늘의 속담💭\n'{random.choice(adage_saying_list)}'"
# 오늘의 추천 활동
def random_activity():
    return f"🏃 오늘의 추천 활동은 '{random.choice(activity_list)}'입니다."
# 오늘의 추천 책
def random_book():
    book = random.choice(book_list)
    return f"📚 오늘의 추천 책은 {book['저자']}의 '{book['제목']}'입니다."
# 오늘의 추천 영화
def random_movie():
    movie = random.choice(movie_list)
    return f"🎬 오늘의 추천 영화는 {movie['감독']} 감독의 '{movie['제목']}'입니다."
# 오늘의 추천 드라마
def random_drama():
    return f"📺 오늘의 추천 드라마는 '{random.choice(drama_list)}'입니다."
# 오늘의 추천 웹툰
def random_webtoon():
    webtoon = random.choice(webtoon_list)
    return f"🖌️ 오늘의 추천 웹툰은 {webtoon['작가']} 작가의 '{webtoon['제목']}'입니다."
# 오늘의 추천 음악
def random_music():
    music = random.choice(music_list)
    return f"🎶 오늘의 추천 음악은 {music['가수']}의 '{music['제목']}'입니다."
#아재개그
def random_jokes():
    joke = random.choice(jokes)
    return f"재미있는 농담하나 해드릴게요\n😄{joke['question']}\n 👉{joke['answer']}"

menu_request_activated = False
menu_recipe_activated = False
@app.route('/message', methods=['POST'])
def respond():
    user_message = request.json.get('message')

    time.sleep(1)
    # 오타 및 맞춤법 검사
    correct_message = spellcheck(user_message)

    # 문장부호를 기준으로 문장 분리
    sentences = split_sentences(correct_message)

    # 문장 처리 함수 정의
    def process_sentence(sentences):
        global menu_request_activated
        global menu_recipe_activated
        #연결어를 기준으로 문장 분리
        parts = split_with_connectors_and_morpheme(sentences)
        response_list = []
        for part in parts:
            # 사용자 메시지에서 불용어 제거 후 키워드 추출
            keywords = preprocess(part)

            # 사용자 의도 파악
            intent = calculate_intent_similarity(part)
            
            # 의도에 따른 응답
            if intent == "greeting": # 안녕
                response_list.append("안녕하세요! 반갑습니다.")
            elif intent == "emotion_joy_request": # 즐겁다
                response_list.append(emotion_joy())
            elif intent == "emotion_sadness_request": # 슬프다
                response_list.append(emotion_sadness())
            elif intent == "emotion_anger_request": # 화난다
                response_list.append(emotion_anger())
            elif intent == "emotion_boredom_request": # 지루하다
                response_list.append(emotion_boredom())
            elif intent == "time_request": # 시간
                time_response = handle_time_request(keywords)
                response_list.append(time_response)
            elif intent == "exchange_rate_request": # 환율
                exchange_rate_response = handle_exchange_rate_request(keywords)
                response_list.append(exchange_rate_response)
            elif intent == "menu_request": # 저메추
                menu_request_activated = True  # 저메추 활성화
                response_list.append("반찬, 국, 밥, 후식 중 어떤 종류의 메뉴를 원하시나요?")
            elif intent == "menu_type": # 메뉴
                if menu_request_activated == True:
                    mene_response = recommend_dish(keywords)
                    response_list.append(mene_response)
                    response_list.append("레시피를 보실건가요?")
                    menu_recipe_activated = True
                else:
                    response_list.append("먼저 메뉴추천을 물어봐 주세요!")
            elif intent == "menu_recipe": #레시피
                if menu_recipe_activated:
                    recipe = recipe_show()
                    response_list.append(recipe)
                else:
                    response_list.append("무슨 말인지 모르겠어요")
            elif intent == "weather_request": # 날씨
                weather_response = handle_weather_request(keywords)
                response_list.append(weather_response)
            elif intent == "air_pollution_request": # 공기오염
                air_pollution_response = handle_air_pollution_request(keywords)
                response_list.append(air_pollution_response)
            elif intent == "help_request": # 도와줘
                response_list.append("무엇을 도와드릴까요?")
            elif intent == "random_fortune_telling_request": # 운세
                response_list.append(random_fortune_telling())
            elif intent == "random_famous_saying_request": # 명언
                response_list.append(random_famous_saying())
            elif intent == "random_idiom_request": # 사자성어
                response_list.append(random_idiom())
            elif intent == "random_adage_saying_request": # 속담
                response_list.append(random_adage_saying())
            elif intent == "random_activity_request": # 활동
                response_list.append(random_activity())
            elif intent == "random_book_request": # 책
                response_list.append(random_book())
            elif intent == "random_movie_request": # 영화
                response_list.append(random_movie())
            elif intent == "random_drama_request": # 드라마
                response_list.append(random_drama())
            elif intent == "random_webtoon_request": # 웹툰
                response_list.append(random_webtoon())
            elif intent == "random_music_request": # 음악
                response_list.append(random_music())
            elif intent == "random_joke_request": #아재개그
                response_list.append(random_jokes())
            else: # 뭐라는거야
                response_list.append("알 수 없는 메시지입니다.")
            
        return "\n".join(response_list)
            
        # 병렬 처리
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_sentence, sentences))

        # 결과 합치기
    responses = [str(item).replace("\n", "<br>") for item in results]
    return jsonify({"response": "<br>".join(responses)})


def handle_time_request(keywords):
    for country, time_zone in time_zones.items():
        if country in keywords:
            url = f"https://timeapi.io/api/time/current/zone?timeZone={time_zone}"
            response = requests.get(url)
            if response.status_code == 200: #요청이 성공한 경
                current_world_time = response.json()
                datetime_str = current_world_time['dateTime']
                formatted_time = datetime_str.split('.')[0].replace('T', ' ')
                        
                date_part, time_part = formatted_time.split(' ')
                hour, minute, second = time_part.split(':')
                        
                return(f"{country}의 현재 시간은 {date_part} {hour}시 {minute}분 {second}초입니다.")
                break
            else:
                return "시간 정보를 가져오는 데 실패했어요."
    else:
        current_time = datetime.now().strftime("%Y-%m-%d %H시%M분%S초")
        return(f"현재 시간은 {current_time}입니다.")

                    
#환율 정보 API 호출 (박재우)
def handle_exchange_rate_request(keywords):
    country_requested = None
    for country in country_code.keys():  # country_code 딕셔너리가 제대로 정의되어 있어야 합니다.
         if country in keywords:
            date = 20240830  # API 정보 중 가장 최신 정보 (예: 2024년 8월 30일)
            countrycode = country_code[country]  # 국가명에 해당하는 국가 코드

            url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
            auth_key = "DKWGm3i0m5yiRLoGgombHtYiuLwE3mYV"

            # API 요청 파라미터
            params = {
                "authkey": auth_key,
                "searchdate": date,
                "data": "AP01"
            }

            try:
                response = requests.get(url, params=params, verify=False)
                response.raise_for_status()  # 응답 상태 확인

                data = response.json()
                            

                # 환율 정보 찾기
                found = False
                for i in data:
                    if i['cur_unit'] == countrycode:
                        return(
                            f"2024년 8월 30일 기준 {i['cur_nm']} 환율 정보: \n"
                            f"매매기준율: {i['ttb']}원 \n"
                            f"매입환율: {i['ttb']}원 \n"
                            f"매도환율: {i['tts']}원 \n")
                        found = True
                        break
                if not found:
                    return("해당 국가의 환율 정보를 찾을 수 없습니다.")
                        
            except requests.exceptions.RequestException as e:
                return(f"API요청중 오류가 발생했습니다. 잠시 기다리고 다시 요청해주세요")
                        
            break
    else:
        if country_requested is None:
            return("확실한 국가를 정해서 말해주세요.")
        else:
            return("해당 국가의 환율 정보를 찾을 수 없습니다.")
        
def get_menu(menu_type):
    
    # API 호출 URL
    api_url = f"http://openapi.foodsafetykorea.go.kr/api/d6445d618d4144e3b868/COOKRCP01/json/1/99/RCP_PAT2={menu_type}"
    try:
            response = requests.get(api_url, verify=False)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
            data = response.json()

            # 응답 데이터 구조 확인
            
    except requests.exceptions.RequestException as e:
        return [f"API 요청 중 오류 발생: {e}"]
    menu_items = []
        
    # 응답 데이터 구조 확인 후 필터링
    if 'COOKRCP01' in data:
        if 'row' in data['COOKRCP01']:
            for row in data['COOKRCP01']['row']:
                menu_name = row.get('RCP_NM', '알 수 없는 메뉴')
                menu_items.append(menu_name)
        else:
            return (f"응답에 'row' 키가 없습니다.")
    else:
        return("응답에 'COOKRCP01' 키가 없습니다.")
    
    if not menu_items:
        return ("메뉴가 없습니다.")
    
    # 랜덤으로 메뉴 추천
    if menu_items:
        return random.choice(menu_items)
    else:
        return (f"메뉴 정보를 불러올 수 없습니다.{menu_items}")
    

def get_recipe(menu_name):
    # 메뉴 이름을 기반으로 레시피를 검색하는 기능을 추가
    api_url = f"http://openapi.foodsafetykorea.go.kr/api/d6445d618d4144e3b868/COOKRCP01/json/1/99/RCP_NM={menu_name}"
    print(api_url)
    
    # API 요청
    response = requests.get(api_url, verify=False)
    response.raise_for_status()  # 응답 상태 확인
    # JSON 데이터 파싱
    data = response.json()
    
    # 레시피 정보를 추출 (여기서는 여러 항목을 포함)
    recipe_data = None
    if 'COOKRCP01' in data and 'row' in data['COOKRCP01']:
        for row in data['COOKRCP01']['row']:
            if row.get('RCP_NM') == menu_name:
                recipe_data = {
                    '조리법': [row.get(f'MANUAL{i:02d}', '') for i in range(1, 21)],
                    '재료': row.get('RCP_PARTS_DTLS', '재료 정보 없음'),
                    '열량': row.get('INFO_ENG', '열량 정보 없음'),
                    '탄수화물': row.get('INFO_CAR', '탄수화물 정보 없음'),
                    '단백질': row.get('INFO_PRO', '단백질 정보 없음'),
                    '지방': row.get('INFO_FAT', '지방 정보 없음'),
                    '나트륨': row.get('INFO_NA', '나트륨 정보 없음')
                }
                break
    
    if recipe_data:
        return recipe_data
    else:
        return (f"레시피 정보를 찾을 수 없습니다.{menu_name}")
recommended_menu = ''
def recommend_dish(menu_type):
    global recommended_menu
    global menu_request_activated
    if "밥" in menu_type:
        menu_type = '밥'
    elif "반찬" in menu_type:
        menu_type = '반찬'
    elif "후식" in menu_type:
        menu_type = '후식'
    elif "국" in menu_type:
        menu_type = '국'
    menu_request_activated = False
    recommended_menu = get_menu(str(menu_type))
    return(f"추천하는 메뉴: \n"
           f"{recommended_menu}")

def recipe_show():
    global recommended_menu
    global menu_recipe_activated
    # 레시피 보기 여부
    recipe = get_recipe(recommended_menu)
    cooking_steps = "\n".join(f"- {step}" for step in recipe['조리법'] if step)
    menu_recipe_activated = False

    # 레시피 출력
    if isinstance(recipe, dict):
        return(
            f"추천된 메뉴: {recommended_menu}\n"
            f"{recommended_menu}의 레시피:\n"
            f"조리법:"
            f"\n재료: {recipe['재료']}\n"
            f"{cooking_steps}\n"
            f"열량: {recipe['열량']}, 탄수화물: {recipe['탄수화물']}, 단백질: {recipe['단백질']}, 지방: {recipe['지방']}, 나트륨: {recipe['나트륨']}\n"
        )
    else:
        return(recipe)


# Weather API 호출 함수
def handle_weather_request(keywords):
    for country_name in capital_mapping.keys():
        if country_name in keywords:
            return weather_api(country_name)
    return "지원하지 않는 국가입니다. 다른 국가를 입력해 주세요."
                
# Air Pollution API 호출 함수
def handle_air_pollution_request(keywords):
    for country_name in capital_mapping.keys():
        if country_name in keywords:
            return air_pollution_api(country_name)
    return "지원하지 않는 국가입니다. 다른 국가를 입력해 주세요."

if __name__ == '__main__':
    app.run(debug=True)