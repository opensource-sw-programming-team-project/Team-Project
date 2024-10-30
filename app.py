from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime #재우님
import requests
from konlpy.tag import Okt #종명
import time

app = Flask(__name__)
okt = Okt()
CORS(app)

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

@app.route('/message', methods=['GET', 'POST'])

def respond():
    user_message = request.json.get('message')
    
    tokens = okt.morphs(user_message)

    time.sleep(1)

    if "안녕" in tokens:
        return jsonify({"response" : "안녕하세요!"})

    elif any(phrase in user_message for phrase in ["몇 시", "몇시", "시간"]):
        for country, time_zone in time_zones.items():
            if country in tokens:
                url = f"https://timeapi.io/api/time/current/zone?timeZone={time_zone}"
                response = requests.get(url)
                if response.status_code == 200:  # 요청이 성공한 경우
                    current_world_time = response.json()
                    datetime_str = current_world_time['dateTime']
                    formatted_time = datetime_str.split('.')[0].replace('T', ' ')

                    date_part, time_part = formatted_time.split(' ')
                    hour, minute, second = time_part.split(':')
                
                    return jsonify({"response": f"{country}의 현재 시간은 {date_part} {hour}시 {minute}분 {second}초 에요."})
                else:
                    return jsonify({"response": "시간 정보를 가져오는 데 실패했어요."})
                
        if any(phrase in user_message for phrase in ["지금", "현재"]):
            if "알려주지마" in tokens:
                return jsonify({"response" : "네 알려드리지 않을게요."})
            else:
                current_time = datetime.now().strftime("%Y-%m-%d %H시%M분%S초")
                return jsonify({"response" : "현재 시간은 " + current_time + " 에요."})
            
    else:
        return jsonify({"response" : "알 수 없는 메시지입니다."})

if __name__ == '__main__':
    app.run(debug=True)