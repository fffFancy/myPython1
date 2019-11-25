def collatz(number):
    if number % 2 == 0:
        divNum = number // 2
    else:
        divNum = 3 * number + 1

    return divNum

#
# try:
#     result = int(input('Enter a number~\n'))
#     # 没有考虑到输入0时会死循环
#     # if result == 0:
#     #     print('0 is a special number')
#     # else:
#     #     while result != 1 and result!=0:
#     #         result = collatz(result)
#     #         print(result)
#     while result != 1 and result != 0:
#         result = collatz(result)
#         print(result)
# except ValueError:
#     print('Please enter a integer!')

result = input('Enter a number~\n')
while True:
    try:
        result = collatz(int(result))
        print(result)
        if result==1 or result==0:
            break
    except ValueError:
        print('Please enter a integer!')
        break


