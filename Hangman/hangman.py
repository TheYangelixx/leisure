import random
from Color_Console import *

# coppied this from the internet 😶
HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

maxWrongGuess = len(HANGMAN) - 1
wrong_counter = 0
already_guessed = []

WORDS = ("SAMPAD", "FARZANEGAN", "INTERSTELLAR", "JANE EYRE", 
         "PYTHON", "GONE WITH THE WIND", "THE MARTIAN", 
         "HARRY POTTER", "CASABLANCA", "PUZZLE", 
         "YASNA JOON", "HANGMAN", "MATHEMATICS", "GILAN")

word = random.choice(WORDS)

# the_word = "-" * len(word)
the_word = ''
for i in word:
    if i == ' ':
        the_word += ' '
    else:
        the_word += '-'

ctext("This game is super roomokh, but a 'friend' had written so I had to, too... Anyway, GOOD LUCK :)", "magenta")

while wrong_counter < maxWrongGuess and the_word != word:
    
    ctext(HANGMAN[wrong_counter], 'magenta')
    ctext(f"\nYou've tried the following letters:\n {already_guessed}", "white")
    ctext(f"\nYou've just been able to guess: :\t {the_word}", "white")
    guess = input("Enter your guess:\t").upper()

    if len(guess) > 1:
        ctext("You've got to enter only ONE character", "red")
        guess = input("Guess again:\t").upper()
    elif not guess.isalpha():
        ctext('The set of guesses must be selected from the alphabet', "red")
        guess = input("Guess again:\t").upper()
    
    if guess in already_guessed:
        ctext(f"You've already guessed the letter:\t {guess}", 'white')
        guess = input("Guess again:\t").upper()
    already_guessed.append(guess)

    if guess in word:
        ctext(f"You guessed '{guess}' correctly! (Finally)", 'green')

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += the_word[i]
        the_word = new

    else:
        ctext(f"\nHaha {guess} isn't in the word😈", 'red')
        wrong_counter += 1

if wrong_counter == maxWrongGuess:
    ctext(HANGMAN[wrong_counter], 'red')
    ctext("You've been hanged!!!", 'white')

else:
    print("\nYou guessed it!")

print("\nThe word was", word)

input ("\nPress Enter key to exit")
