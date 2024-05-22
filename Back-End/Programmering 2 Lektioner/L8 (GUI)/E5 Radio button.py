import tkinter as GUI
from tkinter import messagebox

def show_option():
    selected = var.get()
    messagebox.showinfo("Chosen option", f"You chose {selected}")


window = GUI.Tk()
window.title("Radio Window")
var = GUI.StringVar()
#saves the selected option in the radio as a string variable
#can also be IntVar, DoubleVar, BooleanVar etc
var.set(None)
#sets initial value so no radio boxes are checked
radio1 = GUI.Radiobutton(window, text="Banana", variable=var, value="Banana" )
radio2 = GUI.Radiobutton(window, text="Apple", variable=var, value="Apple" )
radio3 = GUI.Radiobutton(window, text="Pear", variable=var, value="Pear")
radio1.pack()
radio2.pack()
radio3.pack()
button = GUI.Button(window, text="Show Selected Radio", command=show_option)
button.pack(pady=20)
window.mainloop()
