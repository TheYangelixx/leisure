import tkinter as tk
from tkinter.constants import N, NORMAL
import tkinter.messagebox
from tkinter import ttk
import sys

root = tk.Tk()
root.title('Tic-Tac-Toe')
root.resizable(0, 0)

tab_parent = ttk.Notebook(root)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text='Tic Tac Toe') 
tab_parent.add(tab2, text='Info and others')

tab_parent.pack(expand=1, fill='both')

bt1 = tk.StringVar()
bt2 = tk.StringVar()
bt3 = tk.StringVar()
bt4 = tk.StringVar()
bt5 = tk.StringVar()
bt6 = tk.StringVar()
bt7 = tk.StringVar()
bt8 = tk.StringVar()
bt9 = tk.StringVar()

button1 = tk.Button(tab1,textvariable=bt1, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('1'))
button1.grid(row=3, column=0)

button2 = tk.Button(tab1,textvariable=bt2, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('2'))
button2.grid(row=3, column=1)

button3 = tk.Button(tab1,textvariable=bt3, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('3'))
button3.grid(row=3, column=2)

button4 = tk.Button(tab1,textvariable=bt4, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('4'))
button4.grid(row=4, column=0)

button5 = tk.Button(tab1,textvariable=bt5, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('5'))
button5.grid(row=4, column=1)

button6 = tk.Button(tab1,textvariable=bt6, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('6'))
button6.grid(row=4, column=2)

button7 = tk.Button(tab1,textvariable=bt7, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('7'))
button7.grid(row=5, column=0)

button8 = tk.Button(tab1,textvariable=bt8, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('8'))
button8.grid(row=5, column=1)

button9 = tk.Button(tab1,textvariable=bt9, bg='grey', fg='white', height=4, width=8, command=lambda: btnclick('9'))
button9.grid(row=5, column=2)


playera = tk.StringVar()
playerb = tk.StringVar()

p1 = tk.StringVar()
p2 = tk.StringVar()

player1_name = tk.Entry(tab2, textvariable=p1, bd=5)
player2_name = tk.Entry(tab2, textvariable=p2, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name.grid(row=2, column=1, columnspan=8)

def retry_now():
    res = tkinter.messagebox.askyesno(title='Retrying', message='Wanna play again?')
    if res == True:
        button1['state'] = NORMAL
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        button4['state'] = NORMAL
        button5['state'] = NORMAL
        button6['state'] = NORMAL
        button7['state'] = NORMAL
        button8['state'] = NORMAL
        button9['state'] = NORMAL
        bt1.set("")
        bt2.set("")
        bt3.set("")
        bt4.set("")
        bt5.set("")
        bt6.set("")
        bt7.set("")
        bt8.set("")
        bt9.set("")
    else:
        pass

retry_button = tk.Button(tab2, text='Play again', command=retry_now)
retry_button.grid(row=4, column=2)

def exit_now():
    res = tkinter.messagebox.askyesno(title='Exiting', message='Do u wanna exit?')
    if res == True:
        sys.exit()
    else:
        pass
exit_button = tk.Button(tab2, text='Exit', command=exit_now)
exit_button.grid(row=5, column=2)

bclick = True


def disableButton():
    button1['state'] = 'disabled'
    button2['state'] = 'disabled'
    button3['state'] = 'disabled'
    button4['state'] = 'disabled'
    button5['state'] = 'disabled'
    button6['state'] = 'disabled'
    button7['state'] = 'disabled'
    button8['state'] = 'disabled'
    button9['state'] = 'disabled'

buttons = tk.StringVar()
def btnclick(n):
    global bclick, player1_name, player2_name, playerb, playera, button1, button2, button3, button4, button5, button6, button7, button8, button9
    if n == '1' and button1.cget('text') == "" and bclick == True:
        bt1.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        
    
    elif n == '2' and button2.cget('text') == "" and bclick == True:
        bt2.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '3' and button3.cget('text') == "" and bclick == True:
        bt3.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '4' and button4.cget('text') == "" and bclick == True:
        bt4.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '5' and button5.cget('text') == "" and bclick == True:
        bt5.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        
    
    elif n == '6' and button6.cget('text') == "" and bclick == True:
        bt6.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '7' and button7.cget('text') == "" and bclick == True:
        bt7.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '8' and button8.cget('text') == "" and bclick == True:
        bt8.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '9' and button9.cget('text') == "" and bclick == True:
        bt9.set('X')
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '1' and button1.cget('text') == "" and bclick == False:
        bt1.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        
    
    elif n == '2' and button2.cget('text') == "" and bclick == False:
        bt2.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '3' and button3.cget('text') == "" and bclick == False:
        bt3.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '4' and button4.cget('text') == "" and bclick == False:
        bt4.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        
    
    elif n == '5' and button5.cget('text') == "" and bclick == False:
        bt5.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '6' and button6.cget('text') == "" and bclick == False:
        bt6.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '7' and button7.cget('text') == "" and bclick == False:
        bt7.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '8' and button8.cget('text') == "" and bclick == False:
        bt8.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif n == '9' and button9.cget('text') == "" and bclick == False:
        bt9.set('O')
        bclick = True
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkforWin()
        check_it()
        

    elif (n == '1' and button1.cget('text') == "X" or n == '1' and button1.cget('text') == "O" or
        n == '2' and button2.cget('text') == "X" or n == '2' and button2.cget('text') == "O" or
        n == '3' and button3.cget('text') == "X" or n == '3' and button3.cget('text') == "O" or
        n == '4' and button4.cget('text') == "X" or n == '4' and button4.cget('text') == "O" or
        n == '5' and button5.cget('text') == "X" or n == '5' and button5.cget('text') == "O" or
        n == '6' and button6.cget('text') == "X" or n == '6' and button6.cget('text') == "O" or
        n == '7' and button7.cget('text') == "X" or n == '7' and button7.cget('text') == "O" or
        n == '8' and button8.cget('text') == "X" or n == '8' and button8.cget('text') == "O" or
        n == '9' and button9.cget('text') == "X" or n == '9' and button9.cget('text') == "O"):
        tkinter.messagebox.showinfo(title='Tic-Tac-Toe', message='Button Already Clicked')

def checkforWin():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    if(button1.cget('text') == 'X' and button2.cget('text') == 'X' and button3.cget('text') == 'X' or
        button4.cget('text') == 'X' and button5.cget('text') == 'X' and button6.cget('text') == 'X' or
        button7.cget('text') == 'X' and button8.cget('text') == 'X' and button9.cget('text') == 'X' or
        button1.cget('text') == 'X' and button4.cget('text') == 'X' and button7.cget('text') == 'X' or
        button2.cget('text') == 'X' and button5.cget('text') == 'X' and button8.cget('text') == 'X' or
        button3.cget('text') == 'X' and button6.cget('text') == 'X' and button9.cget('text') == 'X' or
        button1.cget('text') == 'X' and button5.cget('text') == 'X' and button9.cget('text') == 'X' or
        button3.cget('text') == 'X' and button5.cget('text') == 'X' and button7.cget('text') == 'X'):
            disableButton()
            tkinter.messagebox.showinfo(title='Tic-Tac-Toe', message=playera)

    elif(button1.cget('text') == 'O' and button2.cget('text') == 'O' and button3.cget('text') == 'O' or
        button4.cget('text') == 'O' and button5.cget('text') == 'O' and button6.cget('text') == 'O' or
        button7.cget('text') == 'O' and button8.cget('text') == 'O' and button9.cget('text') == 'O' or
        button1.cget('text') == 'O' and button4.cget('text') == 'O' and button7.cget('text') == 'O' or
        button2.cget('text') == 'O' and button5.cget('text') == 'O' and button8.cget('text') == 'O' or
        button3.cget('text') == 'O' and button6.cget('text') == 'O' and button9.cget('text') == 'O' or
        button1.cget('text') == 'O' and button5.cget('text') == 'O' and button9.cget('text') == 'O' or
        button3.cget('text') == 'O' and button5.cget('text') == 'O' and button7.cget('text') == 'O'):
            disableButton()
            tkinter.messagebox.showinfo(title='Tic-Tac-Toe', message=playerb)
    
def check_it():
    if((button1.cget('text') == 'O' or button1.cget('text') == 'X') and
        (button2.cget('text') == 'O' or button2.cget('text') == 'X') and
        (button3.cget('text') == 'O' or button3.cget('text') == 'X') and
        (button4.cget('text') == 'O' or button4.cget('text') == 'X') and
        (button5.cget('text') == 'O' or button5.cget('text') == 'X') and
        (button6.cget('text') == 'O' or button6.cget('text') == 'X') and
        (button7.cget('text') == 'O' or button7.cget('text') == 'X') and
        (button8.cget('text') == 'O' or button8.cget('text') == 'X') and
        (button9.cget('text') == 'O' or button9.cget('text') == 'X')):
            disableButton()
            res = tkinter.messagebox.askyesno(title='Tic-Tac-Toe', message="Opsss... It seems no one has won the game! Wanna try again?")
            if res == True:
                button1['state'] = NORMAL
                button2['state'] = NORMAL
                button3['state'] = NORMAL
                button4['state'] = NORMAL
                button5['state'] = NORMAL
                button6['state'] = NORMAL
                button7['state'] = NORMAL
                button8['state'] = NORMAL
                button9['state'] = NORMAL
                bt1.set("")
                bt2.set("")
                bt3.set("")
                bt4.set("")
                bt5.set("")
                bt6.set("")
                bt7.set("")
                bt8.set("")
                bt9.set("")
label1 = tk.Label(tab2, text='Playe1: ', bg = 'white', fg = 'black', height=1, width=8)
label1.grid(row=1, column=0)
label2 = tk.Label(tab2, text='Playe2: ', bg = 'white', fg = 'black', height=1, width=8)
label2.grid(row=2, column=0)

tk.mainloop()
