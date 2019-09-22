# Dulhan
# Connect4
import functools
from tkinter import *

drop = 5
color = "red"
win = False

def restart():
    global win
    global b2
    global color

    w.delete("all")
    w.create_rectangle(x, x, Cwidth - x, Cheight - x)
    if win:
        b2.destroy()
    for i in range(6):
        for j in range(7):
            board[i][j] = w.create_oval(((Cwidth - 2 * x) / 7) * j + x, x + ((Cheight - 2 * x) / 6) * i,
                                        (((Cwidth - 2 * x) / 7) * j + x) + (Cwidth - 2 * x) / 7,
                                        x + ((Cheight - 2 * x) / 6) * i + (Cheight - 2 * x) / 6)
            if i == 1:
                w.create_line(((Cwidth - 2 * x) / 7) * j + x, x, ((Cwidth - 2 * x) / 7) * j + x, Cheight - x)
                click[j] = Button(master, text="Drop", command=functools.partial(clicked, j), bg="blue")
                click[j].place(x=((Cwidth - 2 * x) / 7) * j + x, y=x / 4)
    color = "red"
    win = False

    return

def check():
    global b2
    global win
    c = ["r", "y"]
    cFull = ["RED", "YELLOW"]
    if not win:      # Checks vertically
        for x in range(2):
            for j in range(7):
                for i in range(3):
                    if board[i + 3][j] == c[x-1] and board[i + 2][j] == c[x-1] and board[i + 1][j] == c[x-1] and board[i][j] == c[x-1]:
                        bottom.set(cFull[x - 1] + " WINS")
                        win = True

    if not win:     # Checks horizontally
        for x in range(2):
            for i in range(6):
                for j in range(4):
                    if board[i][j + 3] == c[x-1] and board[i][j + 2] == c[x-1] and board[i][j + 1] == c[x-1] and board[i][j] == c[x-1]:
                        bottom.set(cFull[x - 1] + " WINS")
                        win = True

    if not win:     # Checks diagonal 1
        for x in range(2):
            for i in range(3):
                for j in range(4):
                    if board[i][j] == c[x-1] and board[i+1][j + 1] == c[x-1] and board[i + 2][j + 2] == c[x-1] and board[i + 3][j + 3] == c[x-1]:
                        bottom.set(cFull[x - 1] + " WINS")
                        win = True

    if not win:     # Checks diagonal 2
        for x in range(2):
            for i in range(4,6):
                for j in range(4):
                    if board[i][j] == c[x-1] and board[i-1][j + 1] == c[x-1] and board[i - 2][j + 2] == c[x-1] and board[i - 3][j + 3] == c[x-1]:
                        bottom.set(cFull[x - 1] + " WINS")
                        win = True

    if not win:
        counter = 0
        for i in range(6):
            for j in range(7):
                if board[i][j] == "r" or board[i][j] == "y":
                    counter = counter + 1

        if counter == 42:
            bottom.set("Game is a draw")
            b2 = Button(master, text="Play Again", command=restart, bg="blue")
            b2.pack(side = BOTTOM)

    if win:
        b2 = Button(master, text="Play Again", command=restart, bg="blue")
        b2.pack(side = BOTTOM)

    return

def clicked(j):
    global win
    global drop
    global color
    if not win:
        while (board[drop][j] == "r" or board[drop][j] == "y") and drop > -1:
            drop = drop - 1
        if drop >= 0:
            w.itemconfig(board[drop][j], fill=color)
            if color == "red":
                color = "yellow"
                bottom.set("Yellow's move")
                board[drop][j] = "r"
            else:
                color = "red"
                bottom.set("Red's move")
                board[drop][j] = "y"
            check()
        drop = 5
    return

click = []
board = []
board = [["_" for j in range(7)] for i in range(6)]
click = ["_" for j in range(7)]

master = Tk()
Cwidth = 700
Cheight = 600
x = 100
w = Canvas(master, width=Cwidth, height=Cheight, bg="grey", highlightbackground="blue")
restart()
b1 = Button(master, text="Exit", command=exit, bg="blue")
b1.pack(side=BOTTOM)

bottom = StringVar()
bottom.set("Red's move")

L1 = Label(master, textvariable=bottom)
L1.pack(side=BOTTOM)

w.pack()
master.mainloop()
