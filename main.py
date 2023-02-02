from os import system
from time import sleep

# List of 50 words
words = ['drill', 'attract', 'cupboard', 'slant', 'keep', 'white', 'alarm', 'push', 'cross', 'comfort', 'deprive', 'dressing', 'survival', 'wheel', 'stain',\
    'rich', 'reproduce', 'effective', 'wood', 'grace', 'agree', 'describe', 'child', 'slice', 'bless', 'hand', 'undertake', 'suspicion', 'count', 'bed',\
    'available', 'theater', 'piece', 'wealth', 'dangerous', 'lung', 'spell', 'valley', 'boat', 'crew', 'murder', 'utter', 'budge', 'authorise', 'soprano',\
    'peel', 'us', 'behave', 'wall']

# This function will print letter by letter instead of the whole line at once
def pLine(text, waitTime = 0.06, newLine = True):
    for i in text:
        print(i, end = '', flush = True)
        sleep(waitTime)

    if newLine:
        print('')

# clear screen
system('cls')