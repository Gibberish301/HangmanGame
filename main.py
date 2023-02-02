from os import system
from time import sleep
from random import choice

# Setup wins variable to keep track of the number of wins
wins = 0

# List of 50 words
words = ['drill', 'attract', 'cupboard', 'slant', 'keep', 'white', 'alarm', 'push', 'cross', 'comfort', 'deprive', 'dressing', 'survival', 'wheel', 'stain',\
    'rich', 'reproduce', 'effective', 'wood', 'grace', 'agree', 'describe', 'child', 'slice', 'bless', 'hand', 'undertake', 'suspicion', 'count', 'bed',\
    'available', 'theater', 'piece', 'wealth', 'dangerous', 'lung', 'spell', 'valley', 'boat', 'crew', 'murder', 'utter', 'budge', 'authorise', 'soprano',\
    'peel', 'us', 'behave', 'wall', 'expert']

# This function will print letter by letter instead of the whole line at once
def pLine(text, waitTime = 0.07, newLine = True):
    for i in text:
        print(i, end = '', flush = True)
        sleep(waitTime)

    if newLine:
        print('')

# Clear screen
system('cls')

# Welcoming the user and then giving them options to add more words to the pool if they have more than 3 wins

# Greet the user
pLine('Hello, welcome to my Hangman Game!')
print('')
pLine(f'Your wins: {wins} wins')
print('')

pLine('Please choose one of the following options by typing in the appropriate number')
pLine('1. Play', 0.05)
sleep(0.5)
pLine(f'2. Add word to word pool (currently at {len(words)} words) - Locked to 3 wins', 0.05)

while True:
    try:
        userChoice = int(input('Choice: '))
    except ValueError:
        pLine('Please input an integer! (Positive whole number)', 0.05)
        continue

    if userChoice > 2 or userChoice < 1:
        pLine('That is not a valid option!', 0.05)
        continue
    break

# Setup game


# Get a new word
word = choice(words)