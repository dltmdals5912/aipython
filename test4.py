#함수 만들기
def hello():
    print("hello agumon")


def hello_name(name):
    print(f"안녕 {name}야~")


#함수 호출(실행)
name = input("이름을 입력: ")
hello_name(name)

#연산을 하는 함수
def cal(n1, n2, op): # 1, 2, +(이렇게 입력)
    r = 0 #결과값
    if op == "+":
        r = n1+ n2
    elif op == "-":
        r = n1- n2
    else:
            print("잘못 입력")
    return r # 결고값을 전달

r = cal(2, 1, "+")
print(f"두수를 더한값{r}")
r = cal(2, 1, "-")
print(f"두수를 뺸값{r}")