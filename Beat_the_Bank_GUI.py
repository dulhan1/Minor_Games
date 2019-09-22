# Beat The Bank GUI
# Dulhan

from tkinter import *
import random


def button1clicked():

    return

def button2clicked():
    window1.destroy()
    return

window1 = Tk()
window1.title("Beat the Bank")
window1.geometry('650x200')

label1 = Label(window1, text="")
label1.grid(column=0, row=0)
label2 = Label(window1, text="Menu")
label2.grid(column=0, row=1)
button1 = Button(window1, text="Play Beat the Bank", command=button1clicked)
button1.grid(column=0, row=2)
button2 = Button(window1, text="Exit", command=button2clicked)
button2.grid(column=0, row=3)

window1.mainloop()

total = 0
def button1clicked():

    global num
    global cash2
    global cash
    global total
    global total2


    num = random.randint(0,10)
    cash = 100*num
    cash2 = str(cash)
    total = total + cash
    total2 = str(total)

    if num > 0:
        label1.configure(text=("You earned " + cash2 + " dollars!"))
        label2.configure(text=("Your total is " + total2 + "!"))

    if num == 0:
        label1.configure(text=("Oh no! You got 0 dollars! You are bankrupt and you lose :("))
        label2.configure(text="")
        cash = 0
        total = 0
    return



def button2clicked():


    label1.configure(text=("Congrats! You ended up with " + total2 + " dollars"))
    cash = 0
    total = 0


    return


window2 = Tk()

window2.title("Beat the Bank")
window2.geometry('650x200')

label1 = Label(window2, text="")
label1.grid(column=0, row=0)
label2 = Label(window2, text="Press 'Open Vault' for a chance to get money. Press 'stop' to stop playing and recieve the money.")
label2.grid(column=0, row=1)
button1 = Button(window2, text="Open Vault", command=button1clicked)
button1.grid(column=0, row=2)
button2 = Button(window2, text="Stop Playing", command=button2clicked)
button2.grid(column=0, row=3)

window2.mainloop()
