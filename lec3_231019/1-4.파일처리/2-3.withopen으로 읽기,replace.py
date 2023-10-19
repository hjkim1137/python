# with open 은 f.close 안해도 된다
# add(끝에 문장 추가)
with open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input3.txt", "a", encoding="utf-8") as f:
    f.write(" 추가 문구입니다.")

with open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input3.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    print("-"*20)

# 특정 부분을 수정하기(replace)
# read
with open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input4.txt", "r", encoding="utf-8") as f:
    data = f.read()

# replace
with open("/Users/hyunjungkim/Desktop/일경험교육/일경험 파이썬 교육/hyun_python/lec3_231019/1-4.파일처리/input4.txt", "w", encoding="utf-8") as f:
    data = data.replace("Girlfriend", "여자친구")
    f.write(data)
