# 2차원 리스트
members = [[10, 20, 30], [40,50, 60, 70, 80]]
print(members[0][1])
print()
print(members[1][0])
print(members[1][3])

# 20

# 40
# 70

#예제
strings =[['잠자리', '풍뎅이', '여치'], ['짜장면', '파스타', '피자']]
for i in range(len(strings)):
  for j in range(len(strings[i])):
    print(strings[i][j])
  print() # 카테고리 별로 한줄 띄기 (for j와 같은 위치여야함 유의)

# 잠자리
# 풍뎅이
# 여치

# 짜장면
# 파스타
# 피자