#simple Logic
import datetime
#딕셔너리를 사용해 키워드와 응답을 짝을 짓고 키워드가 있을시 응답을 답하는 형식
responses = {
    "안녕" : "안녕하세요! 무엇을 도와드릴까요?",
    "안녕하세요" : "안녕하세요! 무엇을 도와드릴까요?",
    "시간" : "현재 시간은 {}입니다",
    "자기소개" : "저의 이름은 한밭봇이에요!"
}

def get_responses(user_input):   #사용자에게 입력을 받아 키워드가 포함되어있는지 확인
    for key in responses: 
        if key in user_input:
            if key == "시간":
                time = datetime.datetime.now().strftime("%H:%M:%S")
                return responses[key].format(time) #시간을 문자열에 포함
            else:
                return responses[key]
    return "죄송합니다 이해하지 못했습니다."

while True:
    user_input = input("입력:")
    if user_input == "종료":
        break
    response = get_responses(user_input)
    print("챗봇: ", response)

