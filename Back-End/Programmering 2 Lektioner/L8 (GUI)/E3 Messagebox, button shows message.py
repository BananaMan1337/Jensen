import tkinter as GUI
from tkinter import messagebox
#import tkinter (GUI) as (name)
def show_window():
    user_input = message.get()
    #Assigns text that is inputted in the messagebox with "name".get to a variable
    messagebox.showinfo("Hello", f"You wrote: {user_input}")
    #shows the info from the messagebox, you need to have two texts, first is the title, then whats after the comma
    #actually shows up in the box
   
#function to close the window

window = GUI.Tk()
#window = (name.Tk()), we save the window as variable?
window.title("Window with input and button")
#title of the window
message = GUI.Entry(window, width=30)
#messagebox in the window with a width of 30 characters
message.focus()
#adds the blinking thing to show that you can type in the box
#Makes a text input box
message.pack()
#Puts the box in the window
button = GUI.Button(window, text="Show Message", command=show_window)
#button to close window
#text is the label and command calls the function to destroy window(our window)
button.pack(pady=7)
#places the button in the window with some padding
window.mainloop()
#starts main loop to run the application
