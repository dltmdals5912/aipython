# number = int(input("구구단을 출력할 숫자를 입력하세요 (예: 2): "))
s_number = input("구구단을 출력할 숫자를 입력하세요 (예: 2): ")
print(f"{s_number}단:")
# print(number, "단:")
# print(number + "단:")
# print(f"{number}단:,{number}단:, {number}단:")
# number 값이 문자열이기 때문에 숫자로 변경해서 연산
number = int(s_number)
result = number * 2
print(result)