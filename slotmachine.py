#init
import tkinter as tk 
from tkinter import *
import random

#creates tkinter window size, title and resizability
window = tk.Tk()
window.title("Slots by Alan Ward")
window.geometry("900x400")
window.resizable(False, False)
window.configure(bg="#e3fff9") 
#list of slot choices
slot_choices = ["cherry","7","apple","lemon","grape","strawberry","orange", "clover", "crown", "melon","banana","diamond","bell","date","horseshoe","BAR"]
#Allows user to close the program using a Button rather than just x'ing out of the program.
def quit():
    exit()

#Function checks for wins by adding the computer-chosen values to a list and comparing each element
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
#displays three computer-chosen slots and uses winCheck to determine a match, loss or jackpot
def play():
    check = []
    for i in range (3):
        slot = Label(window, text=random.choice(slot_choices), font=('consolas', 40), bg="#e3fff9")
        check.append(slot.cget("text"))
        slot.pack()
    result = Label(window, text=winCheck(check), font=('consolas', 40), bg="#e3fff9")
    result.pack()

#Game Header
Header = Label(window, text="Slots", font=('consolas', 40), bg="#e3fff9")
Header.pack()

#Game Widgets
playButton = tk.Button(window, bg="white", text="Play!", width=50, command=play)
playButton.pack()

quitButton = tk.Button(window, bg="white" ,text="Quit", width=50, command = quit)
quitButton.pack()



window.mainloop()