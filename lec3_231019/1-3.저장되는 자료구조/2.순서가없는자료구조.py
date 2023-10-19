# 리스트
info1 = {'age': 10, 'age': 15}
print(info1)  # {'age': 15}
# value는 중복 가능, key 는 중복 금지


tom1 = {'foot_size': 120, 'toeic_score': 750}
tom2 = {'toeic_score': 750, 'foot_size': 120}
tom1 == tom2  # true

# 집합
set1 = {'tom', 'dodo', 'james'}
com1 = {}
print(type(com1))  # <class 'dict'>
set1 = set()
print(type(set1))  # <class 'set'>

# 집합 요소 추가(add)
set1 = {'tom', 'dodo', 'james'}
print('set1', set1)  # set1 {'tom', 'dodo', 'james'}
set1.add('grape')
print('set1', set1)
# set1 {'tom', 'dodo', 'grape', 'james'} # 순서에 상관없이 아무데나 들어감

# 합집합
set1 = {1, 2, 3}
set2 = {5, 6, 7}
print(set1 | set2)  # {1, 2, 3, 5, 6, 7}

# 교집합
set1 = {1, 2, 3}
set2 = {3, 5, 6, 7}
print(set1 & set2)  # {3}

# 차집합
set1 = {1, 2, 3, 5, 6}
set2 = {5, 6, 7}
print(set1-set2)  # {1, 2, 3}
