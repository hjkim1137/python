# 튜플
import random

my_tuple = (1, 2, 3, 4, 5)
random_element1 = random.choice(my_tuple)
print(random_element1)

# 문자열
my_string = "hello, world"
random_char = random.choice(my_string)
print(random_char)


# 집합과 딕셔너리는 list 형식으로 먼저 바꾸고 실행
# 집합
my_set = {10, 20, 30, 40, 50}
random_element2 = random.choice(list(my_set))
print(random_element2)

# 딕셔너리
my_dic = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
random_element3 = random.choice(list(my_dic.keys()))
print(random_element3)
