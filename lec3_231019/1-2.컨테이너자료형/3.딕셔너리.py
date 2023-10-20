# 딕셔너리(Dictionary)는 서로 연관된 정보를 key와 value로
# 묶어서 저장하는 자료형으로 자료를 저장하고 처리하기 쉽다는 장점이 있음.
# key를 사용하여 딕셔너리에 요소를 추가하거나 변경, 삭제할수 있으며,
# 한 개의 key에 튜플이나 리스트의 형식으로 여러개의 value를 저장할 수 있음.

# 예제1
chameleon = {'name': ('cabo', 'camely')}
print(chameleon)
chameleon['color'] = ['red', 'yellow']
print(chameleon)
chameleon['color'] = 'perl'
print(chameleon)
print(type(chameleon['name']), type(chameleon['color']))

'''
{'name': ('cabo', 'camely')}
{'name': ('cabo', 'camely'), 'color': ['red', 'yellow']}
{'name': ('cabo', 'camely'), 'color': 'perl'}
<class 'tuple'> <class 'str'>
'''

# 예제2
player = {'name': "John"}
print(player)
player['score'] = 95
player['gender'] = "M"
print(player)

'''
{'name': 'John'}
{'name': 'John', 'score': 95, 'gender': 'M'}
'''


# 요소 삭제
# del 딕셔너리 이름[key]
del player['name']
print(player)
# {'score': 95, 'gender': 'M'}


# 딕셔너리 in, notIn
chameleon = {'name': ('cabo', 'camely')}
print(chameleon)
chameleon['color'] = ['red', 'yellow']
print(chameleon)
chameleon['color'] = 'perl'
print(chameleon)
print(type(chameleon['name']), type(chameleon['color']))

# in/notin
print('color' in chameleon)  # true
print('age' not in chameleon)  # true

# 방법1
# keys, values, items
chameleon = {'name': ('cabo', 'camely'), 'color': ['red', 'yellow']}
print(chameleon.keys())
print(chameleon.values())
print(chameleon.items())

# dict_keys(['name', 'color'])
# dict_values([('cabo', 'camely'), ['red', 'yellow']])
# items는 전체를 출력함: dict_items([('name',('cabo','camely')),('color',['red','yellow'])])

# 방법 2
#  for in 반복문
chameleon = {'name': ('cabo', 'camely'), 'color': ['red', 'yellow']}
# key와 value를 모두 출력
for key in chameleon:
    print(key, chameleon[key])

# key를 모두 출력
# end=' '를 사용하여 순회시마다 줄바꿈 하지 않으며, 1칸씩 공백 설정
for key in chameleon:
    print(key, end=' ')
# value를 모두 출력
for key in chameleon:
    print(chameleon[key], end=' ')

'''
name ('cabo','camely')
color ['red','yellow']
'''

'''
name color ('cabo','camely') ['red','yellow']
'''
