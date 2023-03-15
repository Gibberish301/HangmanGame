from os import system
from time import sleep
from random import choice

# Setup wins variable to keep track of the number of wins
# and make tries variable to setup how many times the user can guess before failing
wins = 0
tries = 5

# List of 50 words
words = ['drill', 'attract', 'cupboard', 'slant', 'keep', 'white', 'alarm', 'push', 'cross', 'comfort', 'deprive', 'dressing', 'survival', 'wheel', 'stain',\
    'rich', 'reproduce', 'effective', 'wood', 'grace', 'agree', 'describe', 'child', 'slice', 'bless', 'hand', 'undertake', 'suspicion', 'count', 'bed',\
    'available', 'theater', 'piece', 'wealth', 'dangerous', 'lung', 'spell', 'valley', 'boat', 'crew', 'murder', 'utter', 'budge', 'authorise', 'soprano',\
    'peel', 'us', 'behave', 'wall', 'expert']

# This function will print letter by letter instead of the whole line at once
def pLine(text, waitTime = 0.03, newLine = True):
    for i in text:
        print(i, end = '', flush = True)
        sleep(waitTime)

    if newLine:
        print('')

def blankify(word, guess = ''):
    wordList = list(word)

    for i in range(len(wordList)):
        wordList[i]

    blankWord = ''.join(wordList)

    return blankWord

def getGuess():
    while True:
        guess = input('Guess a letter: ')

        if guess == 'quit':
            pass
        elif len(guess) > 1 or len(guess) < 1:
            pLine('Must be exactly one character!', 0.05)
            continue
        try:
            if int(guess):
                pLine('Guess cannot be a number!', 0.05)
                continue
        except ValueError:
            pass

        break
    
    return guess

def checkGuess(guess, word, guessed):
    for i in guessed:
        if i == guess:
            return 3

    if guess in word:
        return 1
    else:
        return 2

# Clear screen
system('cls')

# Welcoming the user and then giving them options to add more words to the pool if they have more than 1 wins

# Greet the user
pLine('Hello, welcome to my Hangman Game!')
print('')
pLine(f'Your wins: {wins} wins')
print('')

pLine('Please choose one of the following options by typing in the appropriate number')
pLine('1. Play', 0.05)
sleep(0.1)
pLine(f'2. Add word to word pool (currently at {len(words)} words) - Locked to 1 win')

while True:
    try:
        userChoice = int(input('Choice: '))
    except ValueError:
        pLine('Please input an integer! (Positive whole number)')
        continue

    if userChoice > 3 or userChoice < 1:
        pLine('That is not a valid option!')
        continue
    elif userChoice == 2 and wins < 1:
        pLine('You do not have enough wins to add a word to the pool!')
        continue

    break

# Setup game
system('cls')
sleep(1)

# Get a new word
word = choice(words)
word = 'hello'

# Setup letters user has already picked
guessed = []

visibleWord = blankify(word)

# Ask user for guesses
while True:
    pLine('Enter "quit" to exit the program')
    pLine(f'You have {tries} tries left')
    print('')

    print(blankify(word))
    pLine(visibleWord)
    print('')

    guess = getGuess()

    if guess == 'quit':
        pLine('Goodbye!')
        break
    print('')
    
    guessValid = checkGuess(guess, word, guessed)

    if guessValid == 1:
        pLine('That letter is in the word!')
    elif guessValid == 2:
        pLine('That letter is not in the word!')
        tries -= 1
    else:
        pLine('You cannot guess the same letter twice!')

    guessed.append(guess)

    sleep(1)

    system('cls')

    