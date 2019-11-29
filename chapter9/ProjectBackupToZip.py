#！python3


import zipfile,os


def backupToZip(folder):
    # folder是绝对路径
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1
    print('Creating %s ...' % zipFileName)
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s ...' % foldername)
        # backupZip.write(foldername) 这句话会从users路径开始压缩进来
        backupZip.write(foldername.replace(folder, '.'))

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername.replace(folder, '.'), filename))
    backupZip.close()
    print('Done')


backupToZip('/Users/meitu/Documents/python/myPython1/chapter9')
