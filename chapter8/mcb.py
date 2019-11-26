#! /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8\\
# mcb.pyw - save and load pieces of text to the clipboard
# usage: python mcb.pyw save <keyword> - save clipboard to keyword
#        python mcb.pyw list <keyword> - load keyword to clipboard
#        python mcb.pyw list - load all keywords to clipboard

import shelve
import pyperclip
import sys


mcbShelf = shelve.open('mcb')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(str(list(mcbShelf[sys.argv[1]])))
mcbShelf.close()