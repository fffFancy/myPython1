import pyperclip
import shelve


def mcb(option, keyword=''):
    clipShelf = shelve.open('pmcb')
    if option.lower() == 'save':
        clipShelf[keyword] = pyperclip.paste()
    elif option.lower() == 'list' and keyword == '':
        pyperclip.copy(str(list(clipShelf.keys())))
    elif option.lower() == 'list' and keyword != '':
        pyperclip.copy(str(clipShelf[keyword]))
    elif option.lower() == 'delete' and keyword == '':
        clipShelf.clear()
        print('all data have been delete!')
    elif option.lower() == 'delete' and keyword != '':
        try:
            del clipShelf[keyword]
        except KeyError:
            print('no data')
    clipShelf.close()


# mcb('save', 'test')


mcb('list')
print(pyperclip.paste())

# mcb('list', 'test')
# print(pyperclip.paste())

mcb('delete')
mcb('list')
print(pyperclip.paste())