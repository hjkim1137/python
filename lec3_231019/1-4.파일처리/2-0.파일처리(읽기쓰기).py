# open(): 파일을 특정한 모드로 여는 함수
# 읽을 때는 r, 쓸 때는 w 사용
# read() : 파일 객체로 부터 모든 내용을 읽는 함수
# import csv

# 1. read
# 파일 누르고 경로복사한다.
f = open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()

# 2. write
f = open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input.txt", "w", encoding="utf-8")
txt = "내용을 갱신합니다. 파일이 없으면 물리적인 파일을 새롭게 생성합니다."
f.write(txt)
f.close()
