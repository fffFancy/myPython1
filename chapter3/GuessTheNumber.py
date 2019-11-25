# This is a guess the number game
import  random
secretNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    guess = int(input('Take a guess!\n'))

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break

if guess != secretNum:
    print('Nope. The number I was thinking of was ' + str(secretNum))
else:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')