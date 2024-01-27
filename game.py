import random
import tkinter as tk
from tkinter import messagebox

def table():
    card = ['Queen','King','Jocker']
    user = input_var.get().capitalize()
    if user not in card:
        messagebox.showinfo("Invalid Input", "Pick again")
    return user

def choice():
    return random.choice(['Kill','Forgive','Promote'])

def fate(user_choice,choice):
    if user_choice == choice:
        return 'Impossible Fate'
    elif user_choice == 'King':
        return 'To Get a Promotion'
    elif user_choice == 'Queen':
        return 'To Be Forgiven'
    elif user_choice == 'Jocker':
        return 'You got Terminated'
    else: return 'Game Terminated'

def game():
    user_card = table()
    computer_card = choice()
    result = fate(user_card, computer_card)
    messagebox.showinfo("Result", f"You Picked: {user_card}\nYour fate is: {result}")

root = tk.Tk()
root.geometry = ('500x500')
root.maxsize(500, 500)
root.minsize(500, 500)
root.title('Fate_Game')
input_var = tk.StringVar()
entry = tk.Entry(root, textvariable = input_var)
entry.pack()
button = tk.Button(root, text = "Submit", command = game)
button.pack()
root.mainloop()
