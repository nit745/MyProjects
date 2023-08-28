# importing the required libraries and modules
from tkinter import *
import random

# creating the GUI for the application
guiWindow = Tk()
guiWindow.title("The Rock Paper Scissors Game")
guiWindow.geometry("980x1650")
guiWindow.config(bg="#450954")


# adding a label to the window using the Label() widget
heading = Label(
    guiWindow,
    text='''Lest's play RPS game
    Rule of game:- You choose(rock,paper or scissor)
      rock <> scissor =win rock
      rock <> paper = win paper
      scissor <> paper = win scissor
      .that's it ''',
    font='arial 24 bold',
    bg='#450954',
    fg='red',
     
).pack()

# creating column for user selection

uI = StringVar()


subHeading = Label(
    guiWindow,
    text='Select any one from rock, paper, scissors',
    font='calibri 30 bold',
    bg='#96CEB4',
    width=45
).place(
    x=355,
    y=300
)

Entry(
    guiWindow,
    font='calibri 20',
    textvariable=uI,
    bd=10,
    width=34,
    bg='#008789'

).place(
    x=500,
    y=450
)

l = ["rock", "paper", "scissor"]

# creating function to begin the game
res = StringVar()


def letsPlay():

    userSelection = uI.get()
    compSelection = random.choice(l)
    
    if userSelection == compSelection:
        res.set("It's a Tie!  same choice ")

    elif userSelection == 'rock':
        if (compSelection == 'paper'):
            res.set("Oops! You Lose.")
        else:
            res.set("Congrates! you win")

    elif (userSelection == 'rock'):
        if (compSelection == 'scissors'):
            res.set("Congrats! You Win.")
        else:
            res.set("Oops! you lose")

    elif (userSelection == 'paper'):
        if (compSelection == 'scissors'):
            res.set("Oops! you lose.")
        else:
            res.set("Congrats! You Win.")

    else:
        res.set(" an invalid input! Consider selecting from - rock, paper & scissors")

#Restart Game
def resetGame():
    res.set("")
    uI.set("")

#Exit game
def exitGame():
    guiWindow.destroy()

#Show result
displayResult = Label(
    guiWindow,
    textvariable=res,
    font='calibri 18 bold',
    width=60,

    bg='Yellow'
).place(
    x=350,
    y=650
)

#play button
playButton = Button(
    guiWindow,
    font='calibri 14 bold',
    text='PLAY',
    padx=10,
    width=15,


    activebackground='yellow',
    command=letsPlay
).place(
    x=480,
    y=550
)

#reset button
resetButton = Button(
    guiWindow,
    font='calibri 14 bold',
    text='RESET',
    padx=10,
    width=15,


    activebackground='yellow',
    command=resetGame
).place(
    x=660,
    y=550
)

#exit button
exitButton = Button(
    guiWindow,
    font='calibri 14 bold',
    text='EXIT',
    padx=10,
    width=15,


    activebackground='yellow',
    command=exitGame
).place(
    x=840,
    y=550
)


guiWindow.mainloop()
