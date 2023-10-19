# 다중 return 함수
def function_mul(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return y1, y2, y3


val1, val2, val3 = function_mul(100)
print(val1, val2, val3)
print(type(val1), type(val2), type(val3))


# 다중 return 함수: 형변환
def function_mul2(x):
    y1 = x*100
    y2 = x*200
    y3 = x*300
    return [y1, y2, y3]


lt = function_mul2(100)
print(lt)
print(type(lt))
