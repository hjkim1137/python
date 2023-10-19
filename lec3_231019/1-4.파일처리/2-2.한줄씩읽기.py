# 한줄만 읽기
# f = open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input2.txt", "r", encoding="utf-8")
# line = f.readline()
# print(line)
# f.close()

# 한줄씩 for 문으로 읽어오기
f = open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input2.txt", "r", encoding="utf-8")
for line in f:
    print(line)
    print('-'*20)
f.close()
