# 사용자로부터 입력을 받는 함수
def print_multiplication_table():
    # 사용자에게 숫자를 입력받습니다.
    number = int(input("구구단을 출력할 숫자를 입력하세요 (예: 2): "))
    
    # 구구단 출력
    print(f"{number}단:")
    for i in range(1, 10):  # 1부터 9까지 반복
        result = number * i
        print(f"{number} x {i} = {result}")

# 프로그램 실행
print_multiplication_table()