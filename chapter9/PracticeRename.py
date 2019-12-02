import os, shutil, re


os.chdir('spam')
numberRegex = re.compile(r'''
    ^(spam)             # begin with 'spam'
    (\d){3,}            # at least three number
    ''', re.VERBOSE)
numberSerial = {}

for file in os.listdir(os.getcwd()):
    numberMatch = numberRegex.match(file)
    if numberMatch is not None:
        number = numberMatch.group(2)
        numberSerial[number] = file
keySerial = sorted(numberSerial)

newDict = {}
for i in range(len(keySerial)):
    newDict[keySerial[i]] = int(keySerial[0]) + i
print(newDict)

# for i in numberSerial.keys():
#     if newDict[i] < 10:
#         numberSerial[i] = 'spam00' + str(newDict[i]) + '.' + numberSerial[i].split('.')[1]
#     elif 10 <= newDict[i] < 100:
#         numberSerial[i] = 'spam0' + str(newDict[i])
#     else:
#         numberSerial[i] = 'spam' + str(newDict[i])
for i in numberSerial.keys():
    # 用zfill()方法直接进行填充
    numberSerial[i] = 'spam' + str(newDict[i]).zfill(3) + '.' + numberSerial[i].split('.')[1]

print(numberSerial)