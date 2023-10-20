class WareHouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Lee")
user2 = WareHouse("Kim")
user3 = WareHouse("Park")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

'''
{'name': 'Lee'}
{'name': 'Kim'}
{'name': 'Park'}
'''
