import zipfile, os


# 将当前操作目录切换到指定path
os.chdir('/Users/meitu/Documents/python/myPython1/chapter9')

exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo('8929ec838ebfefa.gif')
print(spamInfo.file_size)
print(spamInfo.compress_size)

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))

exampleZip2 = zipfile.ZipFile('123.zip')
exampleZip2.extractall()

exampleZip.extract('8929ec838ebfefa.gif','/Users/meitu/Documents/python/myPython1/chapter9/456')
exampleZip.close()