import re, pyperclip

# 创建正则表达式 + 分组
phoneNum = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# 匹配正则表达式
mo = phoneNum.search('uuuuuuu(444)-555-8888')
# 传0或不传参数，返回全部
# 传n返回第n个括号中匹配的文本
phone1, phone2 = mo.groups()
print(phone1)
print(phone2)


# 管道匹配
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

# 管道匹配多个模式中的一个，作为正则表达式的一部分
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
print(mo2.group(1))

# 星号匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())

# 加号匹配一次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1)
print(mo2.group())
print(mo3.group())

# 花括号多次匹配
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
print(mo1.group())
print(mo2)

# 字符分类
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, \
                  6 geese, 5 rings, 4 birds, 3 hens, 2 doves,1 partridge'))

# 自定义字符分类
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # area code，带括号或者不带
    (\s|-|\.)?                      # separator，空白符号/-/.
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)
print(phoneRegex.findall('415-863-9900a415-863-9950'))

pwdRegex = re.compile(r'[a-zA-Z0-9]{8,}')
print(pwdRegex.search('FFFFFFFF'))