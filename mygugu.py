# 숫자 두개를 입력을 받아서 
# +, -, *, /를 출력하는 프로그램

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print("+ :", num1 + num2)
print("- :", num1 - num2)
print("* :", num1 * num2)

if num2 != 0:
    print("/ :", num1 / num2)
else:
    print("두 번째 숫자가 0이어서 나눗셈을 할 수 없습니다.")
