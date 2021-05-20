from nonogram import Nonogram, clues
import numpy as np
import tkinter as tk

GAMESIZE = 10 # do 10 by 10 games by default

window = tk.Tk()

def game():
    key = np.random.randint(1,3, size=(GAMESIZE, GAMESIZE))
    board = Nonogram(GAMESIZE, key)
    clue = clues(GAMESIZE, key)
    tk.Label(window, text="Nonogram")
    def clicked(i:int,j:int) -> None:
        if board.reveal(i,j):
            tk.Button(window, bg = 'black', height=2, width=4).grid(row=i+2,column=j+1)
        else:
            tk.Button(window, bg = 'white', height=2, width=4).grid(row=i+2,column=j+1)

    for i in range(GAMESIZE):
        tk.Label(window, text=str('\n'.join(clue[0][i]))).grid(row=1, column=i+1)
    for i in range(GAMESIZE):
        tk.Label(window, text=str(' '.join(clue[1][i]))).grid(row=i+2, column=0)
    for i in range(GAMESIZE):
        for j in range(GAMESIZE):
            if board.game[i,j] == 0:
                tk.Button(window, activebackground='blue', bg = 'white', height=2, width=4, command=clicked(i,j)).grid(row=i+2,column=j+1)
            elif board.game[i,j] == 1:
                tk.Button(window, bg = 'white', height=2, width=4, command=clicked(i,j)).grid(row=i+2,column=j+1)
            else:
                tk.Button(window, bg = 'black', height=2, width=4, command=clicked(i,j)).grid(row=i+2,column=j+1)

    window.mainloop()

game()