# 함수 안에서 자기자신을  호출하는 방식을 재귀호출이라고 한다.

# def hello():
#     print("hello, world!")
#     hello()


# hello()

# 사용예시: 눈꽃 결정, 프랙탈 트리
# 문제점: 무한루프에 빠진다, 따라서 종료 조건 만들어야 한다.

# 재귀호출 종료조건 만들기
def hello(count):
    if count == 0:
        return
    print("hello, world!", count)
    count -= 1
    hello(count)


hello(5)

'''
hello, world! 5
hello, world! 4
hello, world! 3
hello, world! 2
hello, world! 1
'''
