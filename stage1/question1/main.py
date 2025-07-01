def print_hello_mars():
    """ Hello Mars 출력 함수"""
    print('Hello Mars')
    return

def read_mission_log():
    """미션 로그 파일 읽기"""
    try:
        # 파일 열어서 읽기
        with open('mission_computer_main.log', 'r', encoding='utf-8') as file:
            files = file.readlines()

            clean_lines = []
            for line in files:
                clean_lines.append(line.strip())

            return clean_lines
        
    except FileNotFoundError:
        # 파일 못 찾을때 에러
        print('파일을 찾을 수 없습니다.')

def write_mission_log(lines):

    """미션 로그 출력 함수"""
    # 파일 못 찾을때 에러
    if lines is None:
        print('출력할 로그 데이터가 없습니다.')
        return

    print('=== 미션 컴퓨터 로그 ===')
    for line in lines:
        print(line)
    

def main():
    print_hello_mars()
    log_data = read_mission_log()
    write_mission_log(log_data)

if __name__ == '__main__':
    main()