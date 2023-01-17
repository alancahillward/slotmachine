import tkinter as tk 
from tkinter import *
import random

window = tk.Tk()
window.title("Slots by Alan Ward")
window.geometry("900x400")
window.resizable(False, False)
#list of slot choices
slot_choices = ["cherry","7","apple",]
def quit():
    exit()

def winCheck(lst):
    element = lst[0]
    check = True

    for item in lst:
        if element != item:
            check = False
            break
    if check == True:
        if element == "7":
            return("Jackpot!")
        else:
            return("Match")

    else:
        return ("You Lose :(")
def play():
    check = []
    for i in range (3):
        slot = Label(window, text=random.choice(slot_choices), font=('consolas', 40))
        check.append(slot.cget("text"))
        slot.pack()
    result = Label(window, text=winCheck(check), font=('consolas', 40))
    result.pack()

#Game Header
Header = Label(window, text="Slots", font=('consolas', 40))
Header.pack()

playButton = tk.Button(window, bg="white", text="Play!", width=50, command=play)
playButton.pack()

quitButton = tk.Button(window, bg="white" ,text="Quit", width=50, command = quit)
quitButton.pack()



window.mainloop()