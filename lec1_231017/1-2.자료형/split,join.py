# split: 문자열 자르기
string1 ='apple'
print(string1.split("p")) # p를 기준으로 쪼개기 ['a', '', 'le']

# join : 쪼개진 것을 하나의 문자열로 합치기
string1 =['apple', 'mango']
print("&".join(string1)) # apple&mango -> "&" 기호를 기준으로 합치기