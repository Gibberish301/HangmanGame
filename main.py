from os import system
from time import sleep
from random import choice

# Setup wins variable to keep track of the number of wins
# and make tries variable to setup how many times the user can guess before failing
# and also make a boolean to know if the game should keep running or not
wins = 0
continueGame = True

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

def blankify(word):
    wordList = list(word)

    for i in range(len(wordList)):
        wordList[i] = '_'

    blankWord = ''.join(wordList)

    return blankWord

def getGuess():
    while True:
        guess = input('Guess a letter: ')

        if guess == 'quit':
            break
        elif len(guess) > 1 or len(guess) < 1:
            pLine('Must be exactly one character!', 0.05)
            continue
        try:
            if float(guess):
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
    
def fillWord(word, guess, blankWord):
    wordList = list(word)
    blankList = list(blankWord)
    indices = []

    for i,v in enumerate(wordList):
        if v == guess:
            indices.append(i)

    for index in indices:
        blankList[index] = guess

    blankWord = ''.join(blankList)
    return blankWord

def checkWord(visibleWord):

    letters = []

    for letter in visibleWord:
        letters.append(letter)

    if '_' in letters:
        return False
    return True

def guessedLetters(guessed):
    # String is the letters guessed
    string = ''

    for letter in guessed:
        string += f'{letter}, '

    return string

def editWordPool():
    global words

    while True:
        # Menu
        pLine('Welcome to the word pool editor!')
        pLine('Please select one of the following options:')
        print('')

        pLine('Current word pool:')
        pLine(f'{words}', 0.001)
        print('')
        
        pLine('1. Add word to word pool')
        pLine('2. Delete word from word pool')
        pLine('3. Exit')

        while True:
            try:
                userChoice = float(input('Choice: '))
            except ValueError:
                pLine('Please input an integer! (Positive whole number)')
                continue
            break

        # Let the user add words to the word pool
        if userChoice == 1:
            add = input('Word to add to the word pool: ')
            try:
                float(add)
                pLine('The word cannot be a number!')
            except ValueError:
                if len(add) < 2:
                    pLine('Word cannot be less than or equal to 1 character!')
                elif add in words:
                    pLine('That word is already in the word pool!')
                else:
                    words.append(add)
                    pLine(f'Word {add} has been added to the word pool')
            sleep(0.5)
            system('cls')

        # Let the user remove words from the word pool if it is in it
        elif userChoice == 2:
            remove = input('Word to delete from the word pool: ')
            try:
                words.remove(remove)
            except ValueError:
                pLine('That is not a word in the word pool!')

            sleep(0.5)
            system('cls')

        elif userChoice == 3:
            break

# Clear screen
system('cls')

# Welcoming the user and then giving them options to add more words to the pool if they have more than 1 win

# Menu
def menu():
    global wins, continueGame
    while True:
        pLine('Hello, welcome to my Hangman Game!')
        print('')
        pLine(f'Your wins: {wins} wins')
        print('')

        pLine('Please choose one of the following options by typing in the appropriate number')
        pLine('1. Play', 0.05)
        sleep(0.1)
        pLine(f'2. Edit word pool (currently at {len(words)} words) - Locked to 1 win')
        sleep(0.1)
        pLine('3. Quit')

        try:
            userChoice = int(input('Choice: '))
        except ValueError:
            pLine('Please input an integer! (Positive whole number)')
            sleep(0.5)
            system('cls')
            continue
        if userChoice > 3 or userChoice < 1:
            pLine('That is not a valid option!')
            sleep(0.5)
            system('cls')
            continue
        elif userChoice == 2 and wins < 1:
            pLine('You do not have enough wins to edit the word pool!')
            sleep(0.5)
            system('cls')
            continue
        elif userChoice == 2 and wins > 0:
            system('cls')            
            editWordPool()
            system('cls')
            continue
        elif userChoice == 3:
            pLine('Goodbye!')
            sleep(0.5)
            system('cls')
            continueGame = False

        break

# Ask user for guesses
def gameLoop():
    
    # setup
    global wins, continueGame

    # Setup game
    system('cls')
    sleep(1)

    # Get a new word
    word = choice(words)
    visibleWord = blankify(word)
    tries = len(word) + 1

    # Setup letters user has already picked
    guessed = []

    while True:

        if tries < 1:
            pLine('You ran out of tries!')
            pLine(f'The word was: {word}')
            sleep(0.5)
            system('cls')
            break

        pLine('Enter "quit" to exit the program')
        pLine(f'You have {tries} tries left')
        print('')

        pLine(visibleWord)
        print('')

        lettersGuessed = guessedLetters(guessed)
        pLine(f'Letters guessed: {lettersGuessed}')
        print('')

        # Check if there are still hidden letters
        wonGame = checkWord(visibleWord)
        if wonGame:
            pLine('Congratulations, you have won!')
            sleep(1)
            wins += 1
            system('cls')
            break

        guess = getGuess()

        if guess == 'quit':
            pLine('Goodbye!')
            system('cls')
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

        visibleWord = fillWord(word, guess, visibleWord)

# Main loop to run the game loop while the game should be continued
while True:
    menu()
    if continueGame == False:
            break
    gameLoop()