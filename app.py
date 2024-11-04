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

# 불용어 제거를 위한 조사 리스트
stopwords = ['은', '는', '이', '가', '을', '를', '에', '의', '에서', '와', '과', '도', '으로', '하다']

# 키워드 정의 딕셔너리
intents = {
    "greeting": ["안녕", "하이", "안녕하세요"],
    "time_request": ["몇 시", "시간", "몇시"],
    "help_request": ["도와줘", "도움", "어떻게"],
    "exchange_rate_request": ["환율", "환율정보", "환전"] #환율 정보 API 키워드(박재우)
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
    
    elif intent == "help_request":
        return jsonify({"response": "무엇을 도와드릴까요?"})
    
    else:
        return jsonify({"response": "알 수 없는 메시지입니다."})

if __name__ == '__main__':
    app.run(debug=True)
