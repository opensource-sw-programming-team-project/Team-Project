import ast
import os

data_store_path = 'data_store.py'
list_name = "movie_list"  # 업데이트할 기존 리스트 이름

# 기존 리스트를 안전하게 파싱하여 읽어오는 함수
def read_existing_lists(file_path, list_name):
    with open(file_path, 'r', encoding='utf-8') as data_store_file:
        file_content = data_store_file.read()

    # 파이썬 코드 파싱
    parsed_content = ast.parse(file_content)
    for node in parsed_content.body:
        if isinstance(node, ast.Assign):  # 변수 할당 노드
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == list_name:
                    return ast.literal_eval(node.value)  # 리스트 값 반환
    return []

# 새 데이터를 읽는 함수
def read_new_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return ast.literal_eval(file_content)

# 업데이트된 리스트를 다시 파일에 저장하는 함수
def write_to_data_store(file_path, list_name, updated_data, new_list_name=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    if new_list_name:  # 새로운 리스트 추가
        new_list_code = f"\n{new_list_name} = {repr(updated_data)}\n"
        file_content += new_list_code
    else:  # 기존 리스트 업데이트
        parsed_content = ast.parse(file_content)
        new_content = []
        for node in parsed_content.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == list_name:
                        new_content.append(f"{list_name} = {repr(updated_data)}\n")
                        break
                else:
                    new_content.append(file_content[node.lineno - 1])
            else:
                new_content.append(file_content[node.lineno - 1])

        file_content = ''.join(new_content)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(file_content)

# 중복 제거 및 업데이트 처리 함수
def update_data_store(existing_data, new_data, choice, list_name, data_store_path):
    if choice == "1":
        # 변수 초기화
        unique_data = []  # 중복 제거를 위한 리스트 초기화
        seen_keys = set()  # 이미 본 키 추적용 집합 초기화

        combined_data = existing_data + new_data

        for item in combined_data:
            key = f"{item['제목']} & {item['감독']}"  # 각 항목의 고유 키 정의
            if key not in seen_keys:
                seen_keys.add(key)
                unique_data.append(item)

        # 10줄마다 줄바꿈 처리하며 리스트 포맷팅
        formatted_list = f"{list_name} = [\n"
        for i, item in enumerate(unique_data, start=1):
            formatted_list += f"    {repr(item)},\n"
            if i % 10 == 0:  # 10줄마다 줄바꿈 추가
                formatted_list += "\n"
        formatted_list += "]\n"

        # 파일 업데이트
        with open(data_store_path, 'a', encoding='utf-8') as data_store_file:
            data_store_file.write(formatted_list)
        print("기존 리스트에 데이터가 추가됨")

    elif choice == "2":
        # 새로운 리스트 이름 받기
        new_list_name = "movie_list"
        
        # 10줄마다 줄바꿈 처리하며 새로운 리스트 포맷팅
        formatted_list = f"{new_list_name} = [\n"
        for i, item in enumerate(new_data, start=1):
            formatted_list += f"    {repr(item)},\n"
            if i % 10 == 0:  # 10줄마다 줄바꿈 추가
                formatted_list += "\n"
        formatted_list += "]\n"

        # 파일 끝에 새 리스트 추가
        with open(data_store_path, 'a', encoding='utf-8') as data_store_file:
            data_store_file.write("\n# 영화 리스트\n")
            data_store_file.write(formatted_list)
        print("새 리스트가 추가됨")

# 메인 실행 부분
if __name__ == "__main__":
    # 기존 데이터 읽기
    existing_data = read_existing_lists(data_store_path, list_name)

    # 새 데이터 읽기
    new_data = read_new_data('movie_list.txt')

    # 사용자 선택
    print("데이터 추가 방식 선택:")
    print("1. 기존 리스트에 추가")
    print("2. 새로운 리스트로 추가")
    choice = input("선택 (1 또는 2): ")

    # 데이터 업데이트
    update_data_store(existing_data, new_data, choice, list_name, data_store_path)