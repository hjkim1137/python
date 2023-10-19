# 순서가 있는 자료구조
[10, 20, 30] == [20, 10, 30]
# 서로 다른 자료구조 이다.

# sorted(오름차순으로 정렬하되, 기존 리스트를 훼손하지 않음)
num1 = [10, 3, 2, 1]
# print(num1.sort())  # [1, 2, 3, 10]
print(sorted(num1))  # [1, 2, 3, 10]
print(num1)  # [10, 3, 2, 1]

# count
mylist1 = [1, 1, 1, 3, 3]
print(mylist1.count(1))  # 3
