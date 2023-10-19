# 리스트(자바스크립트에서는 배열)
score = [90, 89, 77, 95, 67]
fruit = ['apple', 'banana', 'orange']
print(score)  # [90, 89, 77, 95, 67]
print(fruit)  # ['apple', 'banana', 'orange']

# 리스트의 인덱스
color = ['red', 'green', 'blue', 'black', 'white']
print(color[0])  # red
print(color[4])  # white
print(color[1:4])  # ['green', 'blue', 'black']

# list, range 활용해 list 만들기
num = list(range(1, 21, 2))  # 1~21 전까지 2간격으로 리스트 만들기
print(num)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(num[3:7])  # [7, 9, 11, 13]

# 리스트 합치기
a = [1, 2, 3]
b = [4, 5, 6, 7]
c = a+b
print(len(c))  # 7
print(c)  # [1, 2, 3, 4, 5, 6, 7]
