import re
import os


files = os.listdir('/Users/meitu/Documents/python/myPython1/chapter8')
pattern = input('Please enter your pattern:\n')
finalList = []
for i in files:
    if i.endswith('.txt'):
        findFile = open(i)
        findStr = findFile.readlines()
        findFile.close()
        findRegex = re.compile(pattern)
        for j in findStr:
            findMatch = findRegex.findall(j)
            if len(findMatch) != 0:
                print(findMatch)
                finalList.append(findMatch)
print(finalList)