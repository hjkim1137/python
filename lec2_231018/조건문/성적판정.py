score = int(input('점수를 입력해 주세요:'))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = "F"
print('성적:', score)
print('등급:', grade)
