# 매개변수가 몇 개 일지 모르는 경우(*args, **kwargs)
# arguments, keyword arguments

# 예제1
def args_func(*hello):
    print(hello)


args_func("lee")
args_func("lee", "kim")
args_func("lee", "kim", "park")


'''
# 출력
('lee',)
('lee', 'kim')
('lee', 'kim', 'park')
'''

# 예제 2


def args_func(*args):
    for t in args:
        print(args)
        print(tuple(t))


args_func("lee")
args_func("lee", "kim")
args_func("lee", "kim", "park")

'''
# 출력
('lee',)
('l', 'e', 'e')
('lee', 'kim')
('l', 'e', 'e')
('lee', 'kim')
('k', 'i', 'm')
('lee', 'kim', 'park')
('l', 'e', 'e')
('lee', 'kim', 'park')
('k', 'i', 'm')
('lee', 'kim', 'park')
('p', 'a', 'r', 'k')
'''
