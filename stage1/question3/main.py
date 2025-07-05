# Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다.
def read_mission_csv():
    """미션 로그 파일 읽기"""
    try:
        with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                print(line)

    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')

# Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.
def convert_to_list():
    """미션 로그 파일 읽기"""
    try:
        with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            clean_lines = []
            for line in lines:
                clean_lines.append(line.strip())
            
            # 결과 출력
            for line in clean_lines:
                print(line)
            
            return clean_lines
            
    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')   

# 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다.
def sort_by_hazard_level():
    """배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다."""
    try:
        with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            clean_lines = []
            for line in lines:
                clean_lines.append(line.strip())

            # 헤더 제거하고 데이터만 정렬
            header = clean_lines[0]
            data_lines = clean_lines[1:]
            
            # 인화성(4번째 컬럼) 기준으로 정렬
            data_lines.sort(key=lambda x: float(x.split(',')[4]), reverse=True)
            
            # 헤더와 정렬된 데이터 합치기
            sorted_lines = [header] + data_lines
            
            # 결과 출력
            for line in sorted_lines:
                print(line)
            
            return sorted_lines
            
    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')

# 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
def filter_by_hazard_level():
    """인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다."""
    try:
        with open('Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as file:
            lines = file.readlines()

            clean_lines = []
            for line in lines:
                clean_lines.append(line.strip())
            
            # 헤더 제거하고 데이터만 필터링
            header = clean_lines[0]
            data_lines = clean_lines[1:]

            # 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력
            filtered_lines = [header]
            for line in data_lines:
                if float(line.split(',')[4]) >= 0.7:
                    filtered_lines.append(line)
            
            # 결과 출력
            for line in filtered_lines:
                print(line)
            
            return filtered_lines
            
    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')



def main():
    """메인 함수"""
    print("=== 원본 데이터 ===")
    read_mission_csv()
    print()
    print("=== convert_to_list 함수 실행 결과 ===")
    convert_to_list()
    print()
    print("=== sort_by_hazard_level 함수 실행 결과 ===")
    sort_by_hazard_level()
    print()
    print("=== filter_by_hazard_level 함수 실행 결과 ===")
    filter_by_hazard_level()

    # 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다.
    danger_data = filter_by_hazard_level()
    if danger_data:
        with open('Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as file:
            for line in danger_data:
                file.write(line + '\n')
        print("=== Mars_Base_Inventory_danger.csv 파일 저장 완료 ===")


if __name__ == '__main__':
    main()

