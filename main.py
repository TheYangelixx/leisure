import customtkinter as ctk
from PIL import Image
import subprocess
import sys

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("630x340")
app.title("Games")

def close_then_open(program, exit_code=0):
    # Start the external program
    subprocess.Popen(program)
    # Stop currwnt program
    sys.exit(exit_code)

def button_callback(game_name):
    if game_name == 'chess':
        close_then_open(['python', 'Chess\main.py'])
    elif game_name == 'hangman':
        close_then_open(['python', 'Hangman\hangman_pro.py'])
    elif game_name == 'memorygame':
        close_then_open(['python', 'MemoryGame\memory.py'])
    elif game_name == 'pacman':
        close_then_open(['python', 'Pacman\Pacman.py'])
    elif game_name == 'pong':
        close_then_open(['python', 'Pong\pong.py'])
    elif game_name == 'snakegame':
        close_then_open(['python', 'SnakeGame\snake.py'])
    elif game_name == 'sudoko':
        close_then_open(['python', 'Sudoku\sudoku_gui.py'])
    elif game_name == 'tictactoe':
        close_then_open(['python', 'TicTacToe\Tic-Tac-Toe.py'])
    elif game_name == 'typing':
        close_then_open(['python', 'Typing\Typing.py'])

# Labels
label1 = ctk.CTkLabel(master=app, text="Let's play a game!", font=("Arial", 18),
                               width=120, height=25,
                               fg_color=("white", "gray"),
                               corner_radius=8)

label2 = ctk.CTkLabel(master=app, text="Click on any game you want", font=("Arial", 18),
                               width=120, height=25,
                               fg_color=("white", "gray"), 
                               corner_radius=8)

label1.grid(row=0, column=1, padx=20, pady=20)
label2.grid(row=1, column=1, padx=20, pady=20)


# create button
button_chess = ctk.CTkButton(master=app, text="chess", command=lambda:button_callback('chess'))
button_hangman = ctk.CTkButton(master=app, text="hangman", command=lambda:button_callback('hangman'))
button_memoryGame = ctk.CTkButton(master=app, text="memory game", command=lambda:button_callback('memorygame'))
button_pacman = ctk.CTkButton(master=app, text="pacman", command=lambda:button_callback('pacman'))
button_pong = ctk.CTkButton(master=app, text="pong", command=lambda:button_callback('pong'))
button_snakeGame = ctk.CTkButton(master=app, text="snake game", command=lambda:button_callback('snakegame'))
button_soduko = ctk.CTkButton(master=app, text="soduko", command=lambda:button_callback('sudoko'))
button_tictactoe = ctk.CTkButton(master=app, text="tic tac toe", command=lambda:button_callback('tictactoe'))
button_typing = ctk.CTkButton(master=app, text="typing", command=lambda:button_callback('typing'))

# Placing the buttons
button_chess.grid(row=2, column=0, padx=20, pady=20)
button_hangman.grid(row=2, column=1, padx=20, pady=20)
button_memoryGame.grid(row=2, column=2, padx=20, pady=20)
button_pacman.grid(row=3, column=0, padx=20, pady=20)
button_pong.grid(row=3, column=1, padx=20, pady=20)
button_snakeGame.grid(row=3, column=2, padx=20, pady=20)
button_soduko.grid(row=4, column=0, padx=20, pady=20)
button_tictactoe.grid(row=4, column=1, padx=20, pady=20)
button_typing.grid(row=4, column=2, padx=20, pady=20)

app.mainloop()
