h = int(input("키:")) # 키 정수 변환
w= float(input("몸무게:")) # 몸무게 실수변환

bmi= w/(h*h) *10000 #0.00245675...가 나오기 때문에 만을 곱해준다
print('%.2f' %bmi)