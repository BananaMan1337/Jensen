import tkinter as GUI
#import tkinter (GUI) as (name)
def close_window():
    root.destroy()
#function to close the root

root = GUI.Tk()
#root = (name.Tk()), we save the window as variable?
root.title("Simple Window")
#title of the window
button = GUI.Button(root, text="Close Window", command=close_window)
#button to close window
#text is the label and command calls the function to destroy root(our window)
button.pack(pady=20)
#places the button in the window with some padding
root.mainloop()
#starts main loop to run the application
