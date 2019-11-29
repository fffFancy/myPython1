#! python3
# MM-DD-YYYY转换成DD-MM-YYYY
import re
import os
import shutil

# 创建一个正则表达式匹配美国日期格式,因为涉及换位置，要分组
dateRegex = re.compile(r'\w{3}-\d{2}-\d{4}')
dateRegex = re.compile(r'''
    ^(.*?)              # 日期前面的文本
    ((0|1)?\d)-         # 月份
    ((0|1|2|3)?\d)-     # 日期
    ((19|20)\d\d)       # 年份
    (.*?)$              # 日期后面的文本
''', re.VERBOSE)

# 列出全部文件，查找包含美国日期的文件
allFile = os.listdir('.')
for amerFilename in allFile:
    fileName = dateRegex.match(amerFilename)
    if fileName is None:
        continue
    else:
        beforePart = fileName.group(1)
        monthPart = fileName.group(2)
        dayPart = fileName.group(4)
        yearPart = fileName.group(6)
        afterPart = fileName.group(8)

        # 改名字
        euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart +\
                       afterPart
        # 利用'\3-\1-\5'实现位置的改变
        # euroFilename = dateRegex.sub(r'\3-\1-\5', amerfilename)

        # 获得文件的绝对路径
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFileName = os.path.join(absWorkingDir, euroFileName)

        print('Renaming "%s" to "%s" ...' % (amerFilename, euroFileName))
        shutil.move(amerFilename, euroFileName)