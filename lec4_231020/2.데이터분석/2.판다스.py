# pip3 intsall pandas
# import pandas as pd


import pandas as pd  # pandas 라이브러리를 import

sdata = [10, 40, 30, 20]
city = ['서울', '부산', '울산', '목포']

mySeries2 = pd.Series(data=sdata, index=city)  # pd.Series로 생성

mySeries2.name = '테스트'
mySeries2.index.name = '지역'
print(mySeries2)
