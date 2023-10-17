# append()로 리스트 요소 마지막에 추가
flower = ['무궁화', '장미', '개나리']
print(flower)
flower.append('벚꽃')
print(flower)

# ['무궁화', '장미', '개나리']
# ['무궁화', '장미', '개나리', '벚꽃']


# 리스트 요소 삭제 : remove
member = ['이수현', 20, '경기도 파주시', "abc@google.com", '010-1234-5678']
print(member)
member.remove(20)
print(member)

# ['이수현', 20, '경기도 파주시', 'abc@google.com', '010-1234-5678']
# ['이수현', '경기도 파주시', 'abc@google.com', '010-1234-5678']