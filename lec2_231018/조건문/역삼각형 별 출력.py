for i in range(5):  # 줄의 개수
    for j in range(5):  # 해당 줄 안에 별의 개수
        if j < i:
            print(" ", end="")
        else:
            print("*", end="")
        print(" ")


# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()  # 이 줄을 추가하여 줄바꿈을 한 번만 수행


n = 5
for i in range(n):
    for k in range(n-i):
        print('*', end='')
    print()
