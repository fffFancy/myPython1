#！/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
# bulletPointAdder.py - 文字分段并前加星号

import pyperclip
text = pyperclip.paste()
print(text)
# TODO: 分段，并加星

lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
print(text)
pyperclip.copy(text)
