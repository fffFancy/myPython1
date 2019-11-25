# 方法一，不完善，没有考虑列表嵌套
# def changeListToStr(alist):
#     para = str(alist[0])
#     for i in range(1, len(alist)-1):
#         para = para + ', ' + str(alist[i])
#
#     para = para + ' and ' + str(alist[-1])
#
#     print(para)
#
# changeListToStr(['apples','bananas','tofu','cats'])
# changeListToStr([1,2,3,4,5])
# changeListToStr([1,2,'4',5,'cats'])

# 方法二，使用一些现成的方法,摘自网络，缺点没有处理非字符串的情况以及and前面的逗号
# 值得借鉴的是把和前面不一样的元素直接在列表中处理成一个整体
# def list2Str(alist):
#     alist[-1] = ' and ' + str(alist[-1])
#     para = ', '.join(alist)
#     print(para)
#
# list2Str(['apples','bannas','tofu','cats'])

# 方法三，考虑列表嵌套，先处理列表
def listUnfold(listBefore):
    listAfter = []
    for value in listBefore:
        if type(value) == list:
            listMid = listUnfold(value)
            for item in listMid:
                listAfter.append(item)
        else:
            listAfter.append(value)
    return listAfter

def list2str(alist):
    blist = listUnfold(alist)
    print(blist)
    blist[-1] = ' and ' + str(blist[-1])
    astr = str(blist[0])
    for i in range(len(blist)-1):
        astr = astr + ', ' + str(blist[i])
    astr = astr + str(blist[-1])
    print(astr)

list2str([[[7,5],0],8,[8,[0,[9,7]]],3,9])

