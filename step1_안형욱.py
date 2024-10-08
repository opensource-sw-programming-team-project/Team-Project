import datetime

# 딕셔너리를 사용해 키워드와 응답을 짝을 짓고 키워드가 있을시 응답을 답하는 형식
responses = {
    "날짜": "오늘 날짜는 {}입니다.",
    "요일": "오늘 요일은 {}입니다."
}

# 영어 요일을 한국어 요일로 매핑하는 딕셔너리
day_mapping = {
    "Monday": "월요일",
    "Tuesday": "화요일",
    "Wednesday": "수요일",
    "Thursday": "목요일",
    "Friday": "금요일",
    "Saturday": "토요일",
    "Sunday": "일요일"
}

def get_responses(user_input):   # 사용자에게 입력을 받아 키워드가 포함되어있는지 확인
    user_input = user_input.lower()
    
    # 현재 날짜와 요일을 가져오기
    today = datetime.datetime.now()
    date = today.strftime("%Y년 %m월 %d일")  # 날짜 형식
    day = today.strftime("%A")  # 요일 (영어)

    korean_day = day_mapping.get(day, day) #한국어로 변환

    for key in responses: 
        if key in user_input:
            if key == "날짜":
                return responses[key].format(date)  # 날짜 반환
            elif key == "요일":
                return responses[key].format(korean_day)  # 요일 반환

    return "죄송합니다, 이해하지 못했습니다."

while True:
    user_input = input("입력: ")
    if user_input == "종료":
        break
    response = get_responses(user_input)
    print("챗봇: ", response)