
from tkinter import *
from tkinter import messagebox
# this module contains the English letters from A to Z only in uppercase as a string
from string import ascii_uppercase
from playsound import playsound
import random

root = Tk()
root.title('Hangman')
WORDS= ("SAMPAD", "FARZANEGAN", "INTERSTELLAR", "JANE EYRE", 
         "PYTHON", "GONE WITH THE WIND", "THE MARTIAN", 
         "HARRY POTTER", "CASABLANCA", "PUZZLE", 
         "YASNA JOON", "HANGMAN", "MATHEMATICS", "GILAN")
            
photos = [PhotoImage(file="F:\Games\Hangman\images\hang0.png"), PhotoImage(file="F:\Games\Hangman\images\hang1.png"), PhotoImage(file="F:\Games\Hangman\images\hang2.png"),
            PhotoImage(file="F:\Games\Hangman\images\hang3.png"), PhotoImage(file="F:\Games\Hangman\images\hang4.png"), PhotoImage(file="F:\Games\Hangman\images\hang5.png"),
            PhotoImage(file="F:\Games\Hangman\images\hang6.png"), PhotoImage(file="F:\Games\Hangman\images\hang7.png"), PhotoImage(file="F:\Games\Hangman\images\hang8.png"),
            PhotoImage(file="F:\Games\Hangman\images\hang9.png"), PhotoImage(file="F:\Games\Hangman\images\hang10.png"), PhotoImage(file="F:\Games\Hangman\images\hang11.png")]

def start():
    global the_word_withSpaces, numberOfGuesses
    numberOfGuesses = 0
    the_word=random.choice(WORDS)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_"*len(the_word)))

def guess(letter):
	global numberOfGuesses
	if numberOfGuesses < 11:	
		txt = list(the_word_withSpaces)
		guessed = list(lblWord.get())
		if the_word_withSpaces.count(letter)>0:
			for c in range(len(txt)):
				if txt[c]==letter:
					guessed[c]=letter
				lblWord.set("".join(guessed))
				if lblWord.get()==the_word_withSpaces:
					playsound('F:\Games\Hangman\sound_effect\\victory.mp3')

		else:
			numberOfGuesses += 1
			imgLabel.config(image=photos[numberOfGuesses])
			if numberOfGuesses==11:
					playsound('F:\Games\Hangman\sound_effect\haha.mp3')

imgLabel=Label(root)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)

lblWord = StringVar()
Label(root, textvariable =lblWord, font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)

n=0
for c in ascii_uppercase:
    Button(root, text=c, command=lambda c=c: guess(c), font=('Helvetica 18'), width=4).grid(row=1+n//7,column=n%7)
    n+=1

Button(root, text="New\nGame", command=start, font=("Helvetica 10 bold")).grid(row=4, column=6)
Button(root, text="Exit", command=exit, font=("Helvetica 10 bold")).grid(row=4, column=5)

start()
root.mainloop()
