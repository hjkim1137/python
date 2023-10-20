# pip3 intsall numpy

# 배열 생성
import numpy as np
my_list = np.arange(1, 6)
print(my_list)


my_list = np.zeros((2, 2))
print(my_list)


my_list = np.ones(3)
print(my_list)


sul = 2
rep_cnt = 5
result = np.repeat(sul, rep_cnt)
print(result)
print(type(result))


# concatenate
array1 = np.array([1, 2])
array2 = np.array([3, 4])
print(array1)
print(array2)
result = np.concatenate((array1, array2))
print(result)

# transpose
array4 = np.array([[3, 6, 2], [4, 1, 5]])
result = np.transpose(array4)
print('array4', result)

'''
[[3 4]
 [6 1]
 [2 5]]
'''


# dot
num4 = np.array([[1, 2, 3]])
num5 = np.array([[4], [5], [6]])
num6 = np.array([[1, 2, 3], [4, 5, 6]])
num7 = np.array([[1, 2], [3, 4], [5, 6]])
print(num4)
print(num5)
print(num6)
print(num7)

num4.dot(num5)
