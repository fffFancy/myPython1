#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
# 上句是在命令行执行文件时告诉计算机要用python来解释该文件
# pw.py - 不安全的口令保存
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    # 方括号表示可选的意思，实际执行时不需要加中扩号
    print('用法： python pw.py [account] -copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account)