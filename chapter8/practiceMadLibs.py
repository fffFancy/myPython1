import re


originFile = open('originfile.txt')
wordStr = originFile.read()
print(wordStr)
originFile.close()
wordRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
wordMatch = wordRegex.findall(wordStr)

if len(wordMatch) != 0:
    for i in range(len(wordMatch)):
        oldWord = wordMatch[i]
        wordMatch[i] = input('Please enter a word to take place of ' + wordMatch[i] + '\n')
        # wordStr = wordRegex.sub(wordMatch[i], wordStr, count=1)
        # 用string的replace方法替代正则的sub()方法
        wordStr = wordStr.replace(oldWord, wordMatch[i], 1)
        print(wordStr)

newFile = open('newfile.txt', 'w')
newFile.write(wordStr)