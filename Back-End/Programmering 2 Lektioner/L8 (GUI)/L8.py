#You should also be able to import tkinter along with
#from tkinter import *
#this should make it so you dont have to type Tk everytime?
#quick 30 second test didnt work, need to try further at home.
#test

import tkinter as GUI
from tkinter import *
#import tkinter (GUI) as (name)
def change_text():
    text.config(text="Hello human!")
#function to change the name. "name".config to edit

window = GUI.Tk()
#window = (name.Tk()), we save the window as variable
window.title("Hello window")
#title of the window
text = GUI.Label(window, text="Click the button!")
#New variable that is the "Label", which is the text above the button
text.pack()
#adds the text to the window
button = GUI.Button(window, text="Hello", command=change_text)
#button to change text on label
button.pack(pady=20)
#places the button in the window with some padding
window.mainloop()
#starts main loop to run the application

