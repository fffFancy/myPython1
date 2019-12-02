import os, shutil


def copySome(folder):
    folder = os.path.abspath(folder)
    print(folder)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.zip') or file.endswith('.txt'):
                filePath = os.path.join(root, file)
                if file not in os.listdir('practice'):
                    shutil.move(filePath, '/Users/meitu/Documents/python/myPython1/chapter9/practice/')
            else:
                continue

copySome('123')
