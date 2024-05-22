import tkinter as GUI
from tkinter import messagebox

def greeting():
    user_input = message.get()
    messagebox.showinfo(":)",f"Hello {user_input}")
#Text is needed first as a title and then separated with a comma with the text you want in the box
#If you dont have the smiley it will show "Hello {user_input} in the title instead"
#It was one of the only issues i didnt figure out 
window = GUI.Tk()
window.title("Greeting")
message = GUI.Entry(window)
message.focus()
message.pack()
text = GUI.Label(window, text="Type your name")
text.pack()
button = GUI.Button(window, text="Done", command=greeting)
button.pack()
window.mainloop()