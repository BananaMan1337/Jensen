import tkinter as GUI
counter = 0
def count_increase():
    global counter
    #global means it can be accessed from anywhere
    counter += 1 

    text.config(text=str(counter))

window = GUI.tk()
window.title("Simple Counter")

text = GUI.Label(window, text="0", font=("arial", 30))
text.pack()


