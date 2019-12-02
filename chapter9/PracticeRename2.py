import re, os, shutil


os.chdir('spam')
# spam开头，并且紧跟着编号的文件，编号至少3位数
numberRegex = re.compile(r'''
    ^(spam)             # begin with 'spam'
    (\d\d\d)            # at least three number
    ''', re.VERBOSE)
# 用来存放完整的编号
fullSerial = []
# 用来存放现有的文件
spamSerial = []
# 用来存放现有的编号
numberSerial = []

# 从文件夹中找出符合的文件
for file in os.listdir(os.getcwd()):
    numberMatch = numberRegex.match(file)
    if numberMatch is not None:
        spamSerial.append(file)
        numberSerial.append(int(numberMatch.group(2)))
numberSerial = sorted(numberSerial)
spamSerial = sorted(spamSerial)

# 查找缺失的编号
for i in range(1, max(numberSerial)):
    fullSerial.append(i)
    if i not in numberSerial:
        print('编号 ' + str(i) + '缺失')

# 修改名字
for n, f in zip(spamSerial, fullSerial):
    changedName = n[:4] + str(f).rjust(3,'0') + n[7:]
    shutil.move(n, changedName)
    print(changedName)
