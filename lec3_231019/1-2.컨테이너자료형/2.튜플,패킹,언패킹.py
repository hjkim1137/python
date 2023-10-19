# 튜플(Tuple)은 여러 개의 값을 묶어서 저장하고 처리할 수 있는 장점을 가진 자료형
# 리스트와 달리 한 번 저장한 요소를 바꿀 수 없음.
# 패킹(packing): 한 개의 변수에 여러 개의 요소를 저장
# 여러 가지 자료를 하나의 컨테이너 변수인 튜플로 저장하는 것을 의미함

# 패킹
owl_1 = ('kiki', 8, True)
owl_2 = ('kiki', 8), True  # 첫 번째 요소에 ('kiki',8)의 튜플 저장
owl_3 = 'kiki', (8, True)  # 두 번째 요소에 (8,True)의 튜플 저장

print('owl_1은', owl_1)
print(type(owl_1[0]), type(owl_1[1]), type(owl_1[2]))
print('owl_2는', owl_2)
print(type(owl_2[0]), type(owl_2[1]))
print('owl_3는', owl_3)
print(type(owl_3[0]), type(owl_3[1]))

# owl_1은('kiki',8,True)
# <class 'str'><class 'int'><class 'bool'>
# owl_2는(('kiki',8),True)
# <class 'tuple'><class 'bool'>
# owl_3은('kiki',(8,True))
# <class 'str'><class 'tuple'>


# 언패킹:튜플에 저장된 여러 개의 요소를 다시 변수에 한 개씩 나누어 담는 것
owl = ('kiki', 8, True)
# owl에 저장된 튜플의 요소를 세 개의 변수에 각각 저장

# 예제1
owl_name, owl_age, owl_male = owl
print(owl_name, type(owl_name))
print(owl_age, type(owl_age))
print(owl_male, type(owl_male))

'''
kiki <class 'str'>
8 <class 'int'>
True <class 'bool'>
'''

# 예제2
a, b = 10, 20
a, b = b, a  # '='의 우측 b와 a는 변수
print('a는', a, ',', 'b는', b)
