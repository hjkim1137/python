#in : 특정 문자열의 존재 여부
string1 ="my name in python!"
# python 단어가 string1에 있는가?
print("python" in string1) # True
print("b" in string1) # False

#find : 특정문자열의 인덱스 값, 자료가 없으면 -1 반환
string1 ="my name in python!"
print(string1.find('p')) # 11
print(string1.find('m')) # 0 -> 두개 이상이면 첫번째 위치의 값을 반환
print(string1.find('c')) # -1 -> 자료가 없으면 -1 반환