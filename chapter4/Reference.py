# def eggs(someParameter):
#     someParameter.append('Hello')
#
# spam = [1,2,3]
# eggs(spam)
# print(spam)

import copy
spam = ['A','B','C']
cheese = copy.copy(spam)
cheese[1]=42
print(spam)
print(cheese)