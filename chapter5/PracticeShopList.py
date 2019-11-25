def displayInventory(shopDict):
    ashopDict = dictUnfold(shopDict)
    print("Inventory:")
    total = 0
    for k in ashopDict.keys():
        num = ashopDict[k]
        total += num
        print(str(num) + ' ' + k)
    print('Total number of items: ' + str(total))


def dictUnfold(dictBefore):
    dicAfter = {}
    for k, v in dictBefore.items():
        if type(v) is dict:
            dicMid = dictUnfold(v)
            for k2, v2 in dicMid.items():
                dicAfter[k2] = v2
        else:
            dicAfter[k] = v
    return dicAfter


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if inventory.get(i, 0) != 0:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


myDict = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(dictUnfold(myDict))
displayInventory(myDict)

myDict2 = {'A': {'A1': 1, 'A2': 2}, 'B': 3, 'C': {'C1': 4, 'C2': {'C21': 5, 'C22': 6}}}
print(dictUnfold(myDict2))
displayInventory(myDict2)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
newDict = addToInventory(myDict, dragonLoot)
displayInventory(newDict)
