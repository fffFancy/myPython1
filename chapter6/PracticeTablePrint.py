#! python3
# PracticeTablePrint - 表格打印


# def tablePrint(tableList):
#     strNum = []
#     for i in tableList:
#         length = 0
#         for j in i:
#             length += len(j)
#         strNum.append(length)
#     colWidth = max(strNum) + len(tableList[0]) - 1
#
#     for i in tableList:
#         tableStr = ' '.join(i)
#         # print(tableStr)
#         print(tableStr.rjust(colWidth, ' '))

def tablePrint(tableList):
    # 求出表格的宽度
    colWidth = [0] * len(tableData)
    for i in range(len(tableList)):
        # for j in range(len(tableList[i])):
        #     if len(tableList[i][j]) > colWidth[i]:
        #         colWidth[i] = len(tableList[i][j])
        colWidth[i] = len(sorted(tableList[i], key=(lambda x: len(x)))[-1])
    print(colWidth)

    # 行列转换
    for i in range(len(tableList[0])):
        for j in range(len(tableList)):
            print(tableList[j][i].rjust(colWidth[j], ' '), end=' ')
        print('\n')


tableData = [['apples', 'oranges', 'cherries', 'bananaaaaaaa'], ['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

tablePrint(tableData)