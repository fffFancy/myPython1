import os, send2trash


for root, dirs, files in os.walk('/Users/meitu/Documents/python/myPython1/'):
    for file in files:
        filePath = os.path.join(root, file)
        if os.path.getsize(filePath) > 1048576:
            print(filePath)
            send2trash.send2trash(filePath)