def input_num():
    n = input("정수를 입력해주세요:")
    while not n.isdigit():  # 정수가 아니면 계속 반복
        print("정수가 아닙니다. 정수를 입력해주세요.")
        n = input()
    print("입력된 정수:", n)


input_num()
