# 여러가지 자료셩의 요소를 가진 리스트를 생성하고
# 리스트의 요소와 자료형 출력하기

list_d = ['owl', 27, True]

print(list_d)
print(type(list_d))
print(type(list_d[0]), type(list_d[1]), type(list_d[2]))

'''
['owl', 27, True]
<class 'list'>
<class 'str'> <class 'int'> <class 'bool'>
'''

# range() 함수와 함께 사용(역순도 가능)
list1 = list(range(0, 10))
list2 = list(range(0, 10+1))
list3 = list(range(0, 10, 2))
list4 = list(range(0, 10+1, 2))

print(list1)
print(list2)
print(list3)
print(list4)

'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8, 10]
'''

# 리스트 연산(더하기)
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1+list2
print("list3", list3)
# list3 [1, 2, 3, 4, 5, 6, 7, 8]

# 리스트 곱하기
list1 = [1, 2, 3, 4]
list2 = list1*3  # 3번 반복
print('list2', list2)
# list2 [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# 리스트 append
list1 = ["kiki"]
list1.append(8)
print('append', list1)

# 리스트 extend : 가장 마지막에 여러 개의 요소를 한 번에 추가
list1 = ["kiki"]
list1.extend([8, True])
print('extend', list1)

# 리스트 insert : 특정 위치(인덱스)에 요소 추가
list1 = ["kiki", True]
list1.insert(1, 8)  # 리스트의 두 번째 위치에 8 추가
print('insert', list1)

# 리스트 pop: 특정 위치의 요소 제거
list1 = ['kiki', 8, True]
print(list1)
list1.pop(1)  # list1의 두 번째 요소를 삭제합니다.
print(list1)
list1.pop()  # list1의 마지막 요소를 삭제합니다.
print(list1)

'''
['kiki',8,True]
['kiki',True]
['kiki']
'''

# clear 리스트의 모든 요소를 삭제합니다.
# del 리스트의 특정 요소를 삭제하며, 삭제할 범위를 지정 가능
list1 = ['kiki', 8, True]
list1.clear()  # []

# 리스트:sort
list1 = [3, 1, 2, 5, 4]
list2 = ['c', 'd', 'b', 'a']
list1.sort()  # list1의 요소를 오름차순으로 정렬
print(list1)
list2.sort(reverse=True)  # list2의 요소를 내림차순으로 정렬
print(list2)

# 리스트: sum
list1 = [3, 4, 1, 7, 5, 6, 2]
print(sum(list1))


# in / not in 연산자
list1 = ['kiki', 8, True]
print('kiki' in list1)  # 리스트에 'kiki'가 있는지 확인
print('kiki' not in list1)  # 리스트에 'kiki'가 없는지 확인
print(9 in list1)  # 리스트에 9가 있는지 확인
print(9 not in list1)  # 리스트에 9가 없는지 확인

'''
True
False
False
True
'''

# 리스트 슬라이싱
owl = ["kiki",  8, True]
print(owl[1:2])
print(owl[1:])  # 인덱스 [1] 다음 나머지 모두 불러옴
print(owl[:-1])  # [-1]가 오기 전까지 전체를 불러옴
print(owl[:])  # 전체를 모두 불러옴

'''
[8]
[8, True]
['kiki', 8]
['kiki', 8, True]
'''
