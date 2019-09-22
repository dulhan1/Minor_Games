from tkinter import *

master = Tk()
import random


y = 0
output = ""
gameLoop = True



wordlist = []
wrong_letters = []
file = open("names.txt", "r")
names = file.readlines()
guessList = []


def hangman(event):
    global word
    global var
    global wordlist
    global w
    global y
    global B1
    global gameLoop
    global leftArm
    global rightArm
    global head
    global body
    global leftLeg
    global rightLeg

    letterLoop = True
    letter = event.char
    if gameLoop:
        for x in range(0, len(wordlist)):
            if word[x] == letter:
                wordlist[x] = letter
                validity.set("You guessed the correct letter!")
                var.set(wordlist)
                letterLoop = False
        if letterLoop and letter not in guessList:
            validity.set("You guessed the wrong letter - You lost a body part!")
            guessList.append(letter)
            guessed.set(guessList)

            if y == 0:
                head = w.create_oval(100, 40, 160, 100)
            if y == 1:
                body = w.create_rectangle(100, 100, 160, 200)
            if y == 2:
                leftArm = w.create_line(20, 50, 100, 100)
            if y == 3:
                rightArm = w.create_line(240, 50, 160, 100)
            if y == 4:
                leftLeg = w.create_line(100, 200, 100, 300)
            if y == 5:
                rightLeg = w.create_line(160, 200, 160, 300)

            y = y + 1

            if y == 6:
                var.set("")
                validity.set("YOU RAN OUT OF BODY PARTS AND LOST THE GAME!")
                guessed.set("")
                guess.set("")
                incorrect.set("")
                B1 = Button(master, text="Play Again", command=restart)
                B1.place(x=200, y=675)
                gameLoop = False
        else:
            validity.set("You already guessed that letter!")
        if "_" not in wordlist:
            var.set("")
            validity.set("YOU WON THE GAME!")
            guessed.set("")
            guess.set("")
            incorrect.set("")
            B1 = Button(master, text="Play Again", command=restart)
            B1.place(x=200, y=675)
            gameLoop = False
    return


def restart():
    global word
    global bodylist
    global var
    global wordlist
    global w
    global y
    global gameLoop
    global wrong_letters
    global guessList
    global leftArm
    global rightArm
    global head
    global body
    global leftLeg
    global rightLeg

    B1.destroy()

    y = 0

    gameLoop = True

    wordlist = []
    wrong_letters = []
    file = open("names.txt", "r")
    names = file.readlines()
    guessList = []

    generator()

    incorrect.set("Incorrectly guessed letters:")
    guess.set("GUESS A LETTER:")
    validity.set("")

    var.set(wordlist)

    w.delete(leftArm)
    w.delete(rightArm)
    w.delete(leftLeg)
    w.delete(rightLeg)
    w.delete(body)
    w.delete(head)

    return


def generator():
    global word
    global wordlist
    global names
    for x in range(0, len(names) - 1):
        names[x] = names[x].rstrip()

    del names[-1]
    del names[-1]

    word = names[random.randint(0, len(names) - 1)]

    for x in range(0, len(word)):
        if word[x] == " ":
            wordlist.append(" ")
        else:
            wordlist.append("_")

    return


generator()

w = Canvas(master, width=500, height=600, bg="grey", highlightbackground="blue")
w.title = "Hangman... by Dulhan Naidappuwa Waduge"

w.create_line(130, 40, 130, 10)
w.create_line(130, 10, 450, 10)
w.create_line(450, 10, 450, 450)
w.create_rectangle(400, 450, 500, 500)

incorrect = StringVar()
incorrect.set("Incorrectly guessed letters:")

guess = StringVar()
guess.set("GUESS A LETTER:")

var = StringVar()
var.set(wordlist)

validity = StringVar()

guessed = StringVar()



L4 = Label(master, textvariable=guessed)
L4.pack(side=BOTTOM)

L5 = Label(master, textvariable=incorrect)
L5.pack(side=BOTTOM)

L3 = Label(master, textvariable=validity)
L3.pack(side=BOTTOM)

L2 = Label(master, textvariable=var)
L2.pack(side=BOTTOM)

L1 = Label(master, textvariable=guess)
L1.pack(side=BOTTOM)

y = 0

master.bind("<Key>", hangman)

w.pack(side=LEFT)
master.mainloop()
