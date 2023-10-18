print("-"*60)
print('%7s \t %7s \t %7s \t %7s' % ('cm', 'mm', 'm', 'inch'))
print("-"*60)

# \t: 문자열 사이에 탭 간격을 줄 때 사용

for cm in range(70, 90, 2):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm*0.3937
    print('%7d \t %7.0f \t %7.2f \t %7.1f' % (cm, mm, m, inch))
print('-'*60)
