from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime #재우님
from konlpy.tag import Okt #종명
import time
import requests

app = Flask(__name__)
CORS(app)
okt = Okt()

# 타임존 정보
time_zones = {
    "한국": "Asia/Seoul",
    "일본": "Asia/Tokyo",
    "중국": "Asia/Shanghai",
    "인도": "Asia/Kolkata",
    "인도네시아": "Asia/Jakarta",
    "아랍에미리트": "Asia/Dubai",
    "호주": "Australia/Sydney",
    "러시아": "Europe/Moscow",
    "영국": "Europe/London",
    "독일": "Europe/Berlin",
    "프랑스": "Europe/Paris",
    "네덜란드": "Europe/Amsterdam",
    "이탈리아": "Europe/Rome",
    "남아프리카 공화국": "Africa/Johannesburg",
    "이집트": "Africa/Cairo",
    "브라질": "America/Sao_Paulo",
    "미국": "America/New_York",
    "미국": "America/Los_Angeles",
    "캐나다": "America/Toronto",
    "멕시코": "America/Mexico_City",
    "아르헨티나": "America/Argentina/Buenos_Aires",
} #여러 국가의 타임존을 미리 저장후 불러오기

#국가 코드 정보(박재우)
counrty_code = {
    "아랍에미리트" : "AED",
    "호주" : "AUD",
    "바레인" : "BHD",
    "브루나이" : "BND",
    "캐나다" : "CAD",
    "스위스" : "CHF",
    "중국" : "CNH",
    "덴마크" : "DKK",
    "유로연합" : "EUR",
    "영국" : "GBP",
    "홍콩" : "HKD",
    "인도네시아" : "IDR",
    "일본" : "JPY",
    "한국" : "KRW",
    "쿠웨이트" : "KWD",
    "말레이시아" : "MYR",
    "노르웨이" : "NOK",
    "뉴질랜드" : "NZD",
    "사우디아라비아" : "SAR",
    "스웨덴" : "SEK",
    "싱가포르" : "SGD",
    "태국" : "THB",
    "미국" : "USD"
} #국가와 국가코드를 매칭

# 국가명과 수도의 좌표 매핑(Chat GPT 사용)
capital_mapping = {
    '가나': {'latitude': 5.6037, 'longitude': -0.1870},
    '가봉' : {'latitude': 0.4162, 'longitude': 9.4673},
    '가이아나': {'latitude': 6.8013, 'longitude': -58.1551},
    '과테말라': {'latitude': 14.6349, 'longitude': -90.5069},
    '그리스': {'latitude': 37.9838, 'longitude': 23.7275},
    '기니' : {'latitude': 9.6412, 'longitude': -13.5784},
    '나미비아' : {'latitude': -22.5609, 'longitude': 17.0658},
    '나이지리아': {'latitude': 9.0765, 'longitude': 7.3986},
    '남수단' : {'latitude': 4.8594, 'longitude': 31.5713},
    '남수단공화국' : {'latitude': 4.8594, 'longitude': 31.5713},
    '남아프리카공화국': {'latitude': -25.7479, 'longitude': 28.2293},
    '네덜란드': {'latitude': 52.3676, 'longitude': 4.9041},
    '네팔': {'latitude': 27.7172, 'longitude': 85.3240},
    '노르웨이': {'latitude': 59.9139, 'longitude': 10.7522},
    '뉴질랜드': {'latitude': -41.2865, 'longitude': 174.7762},
    '니제르' : {'latitude': 13.5116, 'longitude': 2.1254},
    '대만': {'latitude': 25.0330, 'longitude': 121.5654},
    '대한민국': {'latitude': 37.5665, 'longitude': 126.9780},
    '덴마크': {'latitude': 55.6761, 'longitude': 12.5683},
    '독일': {'latitude': 52.5200, 'longitude': 13.4050},
    '라오스': {'latitude': 17.9757, 'longitude': 102.6331},
    '라트비아': {'latitude': 56.9496, 'longitude': 24.1052},
    '러시아': {'latitude': 55.7558, 'longitude': 37.6176},
    '루마니아': {'latitude': 44.4268, 'longitude': 26.1025},
    '르완다' : {'latitude': -1.9579, 'longitude': 30.1127},
    '리비아' : {'latitude': 32.8872, 'longitude': 13.1913},
    '리투아니아': {'latitude': 54.6872, 'longitude': 25.2797},
    '마다가스카르': {'latitude': -18.8792, 'longitude': 47.5079},
    '말레이시아': {'latitude': 3.1390, 'longitude': 101.6869},
    '말리' : {'latitude': 12.6392, 'longitude': -8.0029},
    '멕시코': {'latitude': 19.4326, 'longitude': -99.1332},
    '모로코' : {'latitude': 34.0207, 'longitude': -6.8416},
    '모리타니' : {'latitude': 18.0735, 'longitude': -15.9582},
    '모잠비크' : {'latitude': -25.9653, 'longitude': 32.5892},
    '몽골': {'latitude': 47.8864, 'longitude': 106.9057},
    '미국': {'latitude': 38.9072, 'longitude': -77.0369},
    '미얀마': {'latitude': 19.7633, 'longitude': 96.0785},
    '바누아투' : {'latitude': -17.7333, 'longitude': 168.3273},
    '방글라데시': {'latitude': 23.8103, 'longitude': 90.4125},
    '베네수엘라': {'latitude': 10.4806, 'longitude': -66.9036},
    '베트남': {'latitude': 21.0285, 'longitude': 105.8542},
    '벨기에': {'latitude': 50.8503, 'longitude': 4.3517},
    '벨라루스': {'latitude': 53.9006, 'longitude': 27.5590},
    '보츠와나' : {'latitude': -24.6282, 'longitude': 25.9231},
    '볼리비아': {'latitude': -16.5000, 'longitude': -68.1500},
    '부르키나파소' : {'latitude': 12.3714, 'longitude': -1.5197},
    '북마케도니아': {'latitude': 41.9981, 'longitude': 21.4254},
    '불가리아' : {'latitude': 42.6977, 'longitude': 23.3219},
    '브라질': {'latitude': -15.8267, 'longitude': -47.9218},
    '사우디아라비아': {'latitude': 24.7136, 'longitude': 46.6753},
    '세네갈' : {'latitude': 14.6928, 'longitude': -17.4467},
    '세르비아': {'latitude': 44.7866, 'longitude': 20.4489},
    '소말리아' : {'latitude': 2.0469, 'longitude': 45.3182},
    '솔로몬제도': {'latitude': -9.4289, 'longitude': 159.9602},
    '수단' : {'latitude': 15.5007, 'longitude': 32.5599},
    '수리남': {'latitude': 5.8520, 'longitude': -55.2038},
    '스리랑카' : {'latitude': 6.9271, 'longitude': 79.8612},
    '스웨덴': {'latitude': 59.3293, 'longitude': 18.0686},
    '스위스': {'latitude': 46.9480, 'longitude': 7.4474},
    '스페인': {'latitude': 40.4168, 'longitude': -3.7038},
    '슬로바키아': {'latitude': 48.1486, 'longitude': 17.1077},
    '시리아': {'latitude': 33.5138, 'longitude': 36.2765},
    '아랍에미리트': {'latitude': 24.4539, 'longitude': 54.3773},
    '아르헨티나': {'latitude': -34.6037, 'longitude': -58.3816},
    '아이슬란드': {'latitude': 64.1355, 'longitude': -21.8954},
    '아일랜드' : {'latitude': 53.3498, 'longitude': -6.2603},
    '아제르바이잔': {'latitude': 40.4093, 'longitude': 49.8671},
    '아프가니스탄': {'latitude': 34.5553, 'longitude': 69.2075},
    '알바니아': {'latitude': 41.3275, 'longitude': 19.8187},
    '알제리' : {'latitude': 36.7372, 'longitude': 3.0865},
    '앙골라' : {'latitude': -8.8390, 'longitude': 13.2894},
    '에리트레아' : {'latitude': 15.3229, 'longitude': 38.9251},
    '에콰도르': {'latitude': -0.1807, 'longitude': -78.4678},
    '에티오피아': {'latitude': 9.1450, 'longitude': 40.4897},
    '영국': {'latitude': 51.5074, 'longitude': -0.1278},
    '예멘' : {'latitude': 15.3694, 'longitude': 44.1910},
    '오만' : {'latitude': 23.5859, 'longitude': 58.4059},
    '오스트레일리아': {'latitude': -35.2809, 'longitude': 149.1300},
    '오스트리아': {'latitude': 48.2082, 'longitude': 16.3738},
    '온두라스': {'latitude': 14.0723, 'longitude': -87.1921},
    '우간다' : {'latitude': 0.3476, 'longitude': 32.5825},
    '우루과이': {'latitude': -34.9011, 'longitude': -56.1645},
    '우즈베키스탄': {'latitude': 41.2995, 'longitude': 69.2401},
    '우크라이나': {'latitude': 50.4501, 'longitude': 30.5234},
    '이라크': {'latitude': 33.3152, 'longitude': 44.3661},
    '이란': {'latitude': 35.6892, 'longitude': 51.3890},
    '이스라엘': {'latitude': 31.7683, 'longitude': 35.2137},
    '이집트': {'latitude': 30.0444, 'longitude': 31.2357},
    '이탈리아': {'latitude': 41.9028, 'longitude': 12.4964},
    '인도': {'latitude': 28.6139, 'longitude': 77.2090},
    '인도네시아': {'latitude': -6.2088, 'longitude': 106.8456},
    '일본': {'latitude': 35.6895, 'longitude': 139.6917},
    '자메이카': {'latitude': 18.0179, 'longitude': -76.8099},
    '잠비아' : {'latitude': -15.3875, 'longitude': 28.3228},
    '적도기니' : {'latitude': 3.7500, 'longitude': 8.7833},
    '중국': {'latitude': 39.9042, 'longitude': 116.4074},
    '중앙아프리카공화국' : {'latitude': 4.3947, 'longitude': 18.5582},
    '짐바브웨' : {'latitude': -17.8252, 'longitude': 31.0335},
    '차드' : {'latitude': 12.6348, 'longitude': 15.0744},
    '체코': {'latitude': 50.0755, 'longitude': 14.4378},
    '칠레': {'latitude': -33.4489, 'longitude': -70.6693},
    '카메룬' : {'latitude': 3.8480, 'longitude': 11.5021},
    '카보베르데' : {'latitude': 14.9330, 'longitude': -23.5133},
    '카자흐스탄': {'latitude': 51.1694, 'longitude': 71.4491},
    '캐나다': {'latitude': 45.4215, 'longitude': -75.6972},
    '케냐': {'latitude': -1.2864, 'longitude': 36.8172},
    '콜롬비아': {'latitude': 4.7110, 'longitude': -74.0721},
    '콩고': {'latitude': -4.2634, 'longitude': 15.2429},
    '콩고공화국' : {'latitude': -4.2634, 'longitude': 15.2429},
    '콩고민주공화국' : {'latitude': -4.4419, 'longitude': 15.2663},
    '쿠바': {'latitude': 23.1136, 'longitude': -82.3666},
    '크로아티아': {'latitude': 45.8130, 'longitude': 15.9775},
    '키르기스스탄' : {'latitude': 42.8746, 'longitude': 74.6121},
    '타이': {'latitude': 13.7563, 'longitude': 100.5018},
    '타지키스탄' : {'latitude': 38.5598, 'longitude': 68.7870},
    '탄자니아' : {'latitude': -6.7924, 'longitude': 39.2083},
    '태국': {'latitude': 13.7563, 'longitude': 100.5018},
    '통가' : {'latitude': -21.1394, 'longitude': -175.2012},
    '투르크메니스탄' : {'latitude': 37.9601, 'longitude': 58.3797},
    '튀니지' : {'latitude': 36.8065, 'longitude': 10.1815},
    '튀르키예': {'latitude': 39.9334, 'longitude': 32.8597},
    '파나마' : {'latitude': 8.9833, 'longitude': -79.5167},
    '파라과이': {'latitude': -25.2637, 'longitude': -57.5759},
    '파키스탄': {'latitude': 33.6844, 'longitude': 73.0479},
    '파푸아뉴기니': {'latitude': -9.4438, 'longitude': 147.1803},
    '페루': {'latitude': -12.0464, 'longitude': -77.0428},
    '포르투갈': {'latitude': 38.7169, 'longitude': -9.1399},
    '폴란드': {'latitude': 52.2297, 'longitude': 21.0122},
    '프랑스': {'latitude': 48.8566, 'longitude': 2.3522},
    '핀란드': {'latitude': 60.1695, 'longitude': 24.9355},
    '필리핀': {'latitude': 14.5995, 'longitude': 120.9842},
    '한국': {'latitude': 37.5665, 'longitude': 126.9780},
    '헝가리': {'latitude': 47.4979, 'longitude': 19.0402},
    '호주': {'latitude': -35.2809, 'longitude': 149.1300}
    # 다른 국가 추가 가능
}

# 불용어 제거를 위한 조사 리스트
stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '에서', '와', '과', '도', '으로', '하다']

# 키워드 정의 딕셔너리
intents = {
    "greeting": ["안녕", "하이", "안녕하세요"],
    "time_request": ["몇 시", "시간", "몇시"],
    "help_request": ["도와줘", "도움", "어떻게"],
    "exchange_rate_request": ["환율", "환율정보", "환전"], #환율 정보 API 키워드(박재우)
    "weather_request": ["날씨", "기온", "온도"],
    "air_pollution_request": ["대기오염", "미세먼지", "초미세먼지"]
}

# 키워드 추출 및 불용어 제거
def extract_keywords(text):
    tokens = okt.morphs(text)
    keywords = [word for word in tokens if word not in stopwords]
    return keywords

# 의도 분류
def detect_intent(text):
    tokens = extract_keywords(text)
    for intent, keywords in intents.items():
        if any(keyword in tokens for keyword in keywords):
            return intent
    return "unknown"

#환율 정보 API(박재우)
def get_exchange_rate(countrycode, date, country):
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    auth_key = "DKWGm3i0m5yiRLoGgombHtYiuLwE3mYV"

    #API 요청 파라미터
    params = {
        "authkey" : auth_key,
        "searchdate": date,
        "data" : "AP01"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        for i in data:
            if i['cur_unit'] == countrycode:
                return{
                    'date' : date,
                    'country' : i['cur_nm'],
                    'exchange_rate' : i['ttb'],
                    'purchase_rate' : i['ttb'],
                    'sell_rate' : i['tts']
                }
        #요청한 국가가 환율 정보가 없는 경우
        return {"response": f"{country}에 대한 환율 정보를 찾을 수 없습니다."}
    except requests.exceptions.RequestException as e:
        return {"response": f"API 요청 중 오류가 발생했습니다: {e}"}

# Weather API
def weather_api(country_name):
    # OpenWeatherMap API Key
    api_key = '76709f4e1bf2023762668cf9b449c3b3'

    # 국가명에 따른 수도의 좌표 선택
    capital_coordinate = capital_mapping.get(country_name, None)

    if capital_coordinate is None:
        return '지원하지 않는 국가입니다. 다른 국가를 입력해 주세요.'
    
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
        weather_response = f"날씨는 {weather_data['weather'][0]['description']}, 기온은 {weather_data['main']['temp'] - 273.15:.1f}°C입니다."
    else:
        weather_response = f"날씨 정보를 가져올 수 없습니다: {weather_data.get('message', '알 수 없는 오류')}."

    return weather_response

# Air Pollution API
def air_pollution_api(country_name):
    # OpenWeatherMap API Key
    api_key = '76709f4e1bf2023762668cf9b449c3b3'

    # 국가명에 따른 수도의 좌표 선택
    capital_coordinate = capital_mapping.get(country_name, None)

    if capital_coordinate is None:
        return '지원하지 않는 국가입니다. 다른 국가를 입력해 주세요.'
    
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
        air_pollution_response = f"미세먼지(PM10) 농도는 {air_pollution_data['list'][0]['components']['pm10']:.1f}, 초미세먼지(PM2.5) 농도는 {air_pollution_data['list'][0]['components']['pm2_5']:.1f}입니다."
    else:
        air_pollution_response = f"미세먼지 정보를 가져올 수 없습니다: {air_pollution_data.get('message', '알 수 없는 오류')}."

    return air_pollution_response

@app.route('/message', methods=['POST'])
def respond():
    user_message = request.json.get('message')

    time.sleep(1)

    # 사용자 메시지에서 불용어 제거 후 키워드 추출
    keywords = extract_keywords(user_message)
    
    # 사용자 의도 파악
    intent = detect_intent(user_message)
    
    # 의도에 따른 응답
    if intent == "greeting":
        return jsonify({"response": "안녕하세요! 반갑습니다."})
    
    elif intent == "time_request":
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
                    
                    return jsonify({"response": f"{country}의 현재 시간은 {date_part} {hour}시 {minute}분 {second}초 에."})
                else:
                    return jsonify({"response": "시간 정보를 가져오는 데 실패했어요."})
        
        current_time = datetime.now().strftime("%Y-%m-%d %H시%M분%S초")
        return jsonify({"response": f"현재 시간은 {current_time}입니다."})
    #환율 정보 API 호출 (박재우)
    elif intent == "exchange_rate_request":
        for country in counrty_code.keys():
            if country in keywords:
                date = 20240830 # API 정보중 가장 최신 정보
                countrycode = counrty_code[country]
                rate_info = get_exchange_rate(countrycode, date, country)
                if "response" in rate_info:
                    return jsonify(rate_info)
                else:
                    return jsonify({
                        "response" : f"2024년 8월 30일 기준 {rate_info['country']} 환율 정보: \n"
                                     f"매매기준율: {rate_info['exchange_rate']}원 \n"
                                     f"매입환율: {rate_info['purchase_rate']}원 \n"
                                     f"매도환율: {rate_info['sell_rate']}원 \n"
                    })
        return jsonify({"response" : "해당 국가의 환율 정보를 찾을 수 없습니다."})
    
    # Weather API 호출
    elif intent == "weather_request":
        for country_name in capital_mapping.keys():
            if country_name in keywords:
                weather_api_response = weather_api(country_name)
                return jsonify({"response": weather_api_response})
            
    # Air Pollution API 호출
    elif intent == "air_pollution_request":
        for country_name in capital_mapping.keys():
            if country_name in keywords:
                air_pollution_api_response = air_pollution_api(country_name)
                return jsonify({"response": air_pollution_api_response})
    
    elif intent == "help_request":
        return jsonify({"response": "무엇을 도와드릴까요?"})
    
    else:
        return jsonify({"response": "알 수 없는 메시지입니다."})

if __name__ == '__main__':
    app.run(debug=True)