import tkinter as GUI

def VictoryScreen():
    def close_window():
        WinScreen.destroy()
    WinScreen = GUI.Tk()
    WinScreen.title("Congratulations!")
    button = GUI.Button(WinScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    canvas = GUI.Canvas(WinScreen, width = 300, height = 300)
    canvas.pack()
    img = GUI.PhotoImage(file="Victory.png")
    canvas.create_image(20,20, image=img)
    WinScreen.mainloop()


VictoryScreen()