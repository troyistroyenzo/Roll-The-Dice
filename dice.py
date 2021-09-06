
'''
Dice Randomizer
Author: Troy Pastoral | @troyenzoo
'''
import random
from tkinter import *
from tkinter import ttk

# GUI Properties
root = Tk()
root.geometry("500x500")
root.title("PyDice - Roll The Dice!")
root.columnconfigure(0, weight=1)
root.resizable(False, False)
root.configure(background="#002366")

# Roll Dice


def RollDice():
    number = ['\u2680', '\u2881', '\u2682', '\u2683', '\u2684', '\u2685']
    convertedChoice = diceChoices.get()
    if(convertedChoice == choices[0]):
        label.config(text=f'{random.choice(number)}',
                     font=("Futura", 150), fg='white')
        label.grid(pady=60)

    elif(convertedChoice == choices[1]):
        label.config(text=f'{random.choice(number)}{random.choice(number)}', font=(
            "Futura", 150), fg='white')
        label.grid(pady=60)

    elif(convertedChoice == choices[2]):
        label.config(
            text=f'{random.choice(number)}{random.choice(number)}{random.choice(number)}', font=("Futura", 150), fg='white')
        label.grid(pady=60)

    else:
        label.config(text="SELECT HOW MANY DICES!",
                     font=("Futura", 20), fg='red')
        label.grid(pady=60)


# Combo Box
choices = ["One Dice", "Two Dice", "Three Dice", ]
diceChoices = ttk.Combobox(root, values=choices)
diceChoices.grid(pady=30)

# Main Label
label = Label(root, font=("Futura", 50), fg="white", bg="#002366")
label.config(text="ROLL THE \u2684")
label.grid(padx=20, pady=100)

# Button
button = Button(root, text="ROLL THE DICE", command=RollDice)
button.place(x=200, y=400)

root.mainloop()
