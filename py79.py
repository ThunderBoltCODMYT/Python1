# import necessary libraries
import tkinter as tk
from tkinter import *

#Create Window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

#Event Handler for keypress
def handle_keypress(event):
    """Print the character associated w=with the key pressed"""
    print(event.char)

#Bind Keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

#Event Handler for button click
def handle_click(event):
    print("\nThe Button was clicked!")

button = Button(text = "Click me!")
button.pack()

#Bind click event to handle_click()
button.bind("<Button-1>",handle_click)
window.mainloop()