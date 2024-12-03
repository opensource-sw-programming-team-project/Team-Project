import ast
import os

data_store_path = 'data_store.py'
list_name = "book_list"  # 데이터를 가져오고 싶은 리스트 이름


# 기존 리스트 가져오기
def read_existing_lists(file_path, list_name):
    if not os.path.exists(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as data_store_file:
        file_content = data_store_file.read()

        if list_name in file_content:
            try:
                start_idx = file_content.find(f"{list_name} = ") + len(f"{list_name} = ")
                end_idx = file_content.find("]", start_idx) + 1
                if start_idx > -1 and end_idx > -1:
                    return ast.literal_eval(file_content[start_idx:end_idx])
            except Exception as e:
                print(f"기존 데이터 읽기 중 오류 발생: {e}")
    return []


# 새로운 데이터 읽기
def read_new_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"새 데이터 파일이 존재하지 않습니다: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        try:
            return ast.literal_eval(file_content)
        except Exception as e:
            raise ValueError(f"새 데이터 읽기 중 오류 발생: {e}")


# 파일 업데이트 함수
def update_data_store(existing_data, new_data, choice, list_name, data_store_path):
    try:
        if choice == "1":
            # 기존 리스트에 새 데이터 추가
            combined_data = existing_data + new_data

            # 중복 제거 (제목과 저자를 기준으로)
            unique_data = list({f"{item['제목']}|{item['저자']}": item for item in combined_data}.values())

            # 포맷팅된 리스트 생성
            formatted_list = f"{list_name} = [\n"
            for i, item in enumerate(unique_data, start=1):
                formatted_list += f"    {repr(item)},\n"
                if i % 10 == 0:
                    formatted_list += "\n"
            formatted_list += "]\n"

            # 파일 덮어쓰기
            with open(data_store_path, 'w', encoding='utf-8') as data_store_file:
                data_store_file.write(formatted_list)
            print("기존 리스트에 데이터가 추가되었습니다.")

        elif choice == "2":
            # 새로운 리스트 추가
            new_list_name = "emotion_anger_list"  # 새 리스트 이름
            formatted_list = f"{new_list_name} = [\n"
            for i, item in enumerate(new_data, start=1):
                formatted_list += f"    {repr(item)},\n"
                if i % 10 == 0:
                    formatted_list += "\n"
            formatted_list += "]\n"

            # 파일에 추가 쓰기
            with open(data_store_path, 'a', encoding='utf-8') as data_store_file:
                data_store_file.write("\n# 분노한 감정에 대한 응답\n")
                data_store_file.write(formatted_list)
            print("새 리스트가 추가되었습니다.")

        else:
            print("잘못된 선택입니다. 프로그램을 종료합니다.")

    except Exception as e:
        print(f"데이터 업데이트 중 오류 발생: {e}")


# 실행
if __name__ == "__main__":
    try:
        existing_data = read_existing_lists(data_store_path, list_name)

        new_data = read_new_data('emotion_anger_list.txt')

        print("데이터 추가 방식 선택 :")
        print("1. 기존 리스트에 추가")
        print("2. 새로운 리스트로 추가")
        choice = input("선택 (1 또는 2): ")

        update_data_store(existing_data, new_data, choice, list_name, data_store_path)

        # 업데이트 후 결과 확인
        with open(data_store_path, 'r', encoding='utf-8') as file:
            print("\n업데이트된 파일 내용:\n")
            print(file.read())

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")