import random
def getAnswer(answerNum):
    if answerNum == 1:
        return 'It is certain'
    elif answerNum == 2:
        return 'It is decidedly so'
    elif answerNum == 3:
        return 'Yes'
    else:
        return 'Ask again later'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)