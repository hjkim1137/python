num = int(input("정수를 입력하세요: "))
result = "입력된 정수는 100~1000 사이에 있지 않습니다!"
if num >= 100 and num <= 1000:
    result = "입력된 정수는 100~1000 사이에 있습니다!"

print("입력된 정수: %d" % num)
print('%s' % result)
