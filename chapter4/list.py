# 未引进列表时
# print('Enter the name of cat1: ')
# catName1 = input()
# print('Enter the name of cat2: ')
# catName2 = input()
# print('Enter the name of cat3: ')
# catName3 = input()
# print('Enter the name of cat4: ')
# catName4 = input()
# print('The cat names are: ')
# print(catName1,catName2,catName3,catName4,sep=' ')

# 列表
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + \
    '(or Enter nothing to stop.):')
    name = input()

    if name == '':
        break

    catNames = catNames + [name]

print('The cat names are :')
for name in catNames:
    print(' ' + name)