def spam():
    global eggs
    eggs = 'spam' # global

def bacon():
    eggs = 'bacon' # local

def ham():
    print(eggs) # global

eggs = 42 # global
spam()
print(eggs)