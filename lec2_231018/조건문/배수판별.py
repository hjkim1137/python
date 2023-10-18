num = int(input("하나의 수를 입력하세요:"))
result = '3의 배수도 5의 배수도 아니다.'

if num % 3 == 0:
    result = "3의 배수이다."
if num % 5 == 0:
    result = "5의 배수이다."
if num % 3 == 0 and num % 5 == 0:
    result = "3의 배수이면서 5의 배수이다."

print('%d => %s' % (num, result))
# 52 => 3의 배수도 5의 배수도 아니다.
