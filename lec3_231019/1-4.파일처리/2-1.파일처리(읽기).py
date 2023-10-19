# 3-1.일부만 가져오기
f = open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input2.txt", "r", encoding="utf-8")
first = f.read(4)
print(first)
print("-"*20)

# 3-2. 전체 다 가져오기
second = f.read()
print(second)
f.close()
