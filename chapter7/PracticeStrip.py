import re


def regStrip(astr, key='\s'):
    if key == '\s':
        # regexLeft_format = '^' + key + '+'
        # regexRight_format = key + '+' + '$'
        # strip_format = '^' + key + '+|' + key + '+' + '$'
        # 还可以利用占位符如下
        strip_format = r'^%s+|%s$' % (key, key)
    else:
        # regexLeft_format = key + '+'
        # regexRight_format = key + '+'
        strip_format = key + '+|' + key + '+'

    # wSpace_left = re.compile(regexLeft_format)
    # wSpace_right = re.compile(regexRight_format)
    strip_regex = re.compile(strip_format)

    newStr = strip_regex.sub('', astr)
    # newStr = wSpace_right.sub('', newStr)
    print(newStr)
    print(strip_regex.findall(astr))


myStr1 = '    Hello World!    '
myStr2 = 'lHello World!l'
regStrip(myStr1)
regStrip(myStr2, 'l')