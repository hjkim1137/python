# 예제1 (enumerate 활용)


def args_func(*args):
    for i, v in enumerate(args):  # 인덱스, value 받아옴
        print(i, v)


args_func("lee")  # 0 lee
args_func("lee", "kim")  # 0 lee 1 kim

# 예제 2


def args_func(*args):
    for i, v in enumerate(range(10)):
        print(i, v)


args_func("lee")  # 이렇게 인자 넘기더라도

'''
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
'''
