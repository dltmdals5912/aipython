# 구구단 출력 프로그램

# 사용자로부터 단수를 입력받습니다.
number = int(input("구구단의 단수를 입력하세요: "))

# 1부터 9까지 곱한 결과를 출력합니다.
for i in range(1, 10):
    print(f"{number} x {i} = {number * i}")
