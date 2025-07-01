import json
from datetime import datetime

def read_mission_log():
    """미션 로그 파일 읽기"""
    try:
        # 파일 열어서 읽기
        with open('mission_computer_main.log', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            clean_lines = []
            for line in lines:
                # 줄바꿈 문자 제거 후 콤마로 분리
                line = line.strip()
                if line:  # 빈 줄이 아닌 경우에만 처리
                    clean_lines.append(line.split(','))

            return clean_lines
        
    except FileNotFoundError:
        # 파일 못 찾을때 에러
        print('파일을 찾을 수 없습니다.')
        return None

def sort_by_time(lines):

    if lines is None:
        return None
    
    data_lines = lines[1:]
    sorted_lines = sorted(data_lines, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S'), reverse=True)

    return sorted_lines
    

def convert_to_dict(lines):
    
    result_dict = {}
    for i, line in enumerate(lines):
            result_dict[i] = {
                "timestamp": line[0],
                "content": line[1],
                "message" : line[2]
            }
    return result_dict

def save_to_json(data):
    """사전 객체를 JSON 파일로 저장"""
    
    try:
        with open('mission_computer_main.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print('데이터가 .json 파일로 저장되었습니다.')

    except Exception as e:
        print(f'파일 저장 중 오류 발생: {e}')

def write_mission_log(lines):
    """미션 로그 출력 함수"""
    if lines is None:
        print('출력할 로그 데이터가 없습니다.')
        return

    print('=== 미션 컴퓨터 로그 ===')
    for line in lines:
        print(line)

def main():
    # 1. 로그 파일 읽기
    log_data = read_mission_log()
    
    if log_data is None:
        return
    
    # 2. 원본 데이터 출력
    print("=== 원본 로그 데이터 ===")
    write_mission_log(log_data)
    
    # 3. 시간 역순으로 정렬
    sorted_data = sort_by_time(log_data)
    print("\n=== 시간 역순 정렬된 로그 데이터 ===")
    write_mission_log(sorted_data)
    
    # 4. 사전(Dict) 객체로 변환
    dict_data = convert_to_dict(log_data)
    print("\n=== 사전 객체로 변환된 데이터 ===")
    if dict_data:
        for key, value in dict_data.items():
            print(f"{key}: {value}")
    
    # 5. JSON 파일로 저장
    save_to_json(dict_data)

if __name__ == '__main__':
    main()