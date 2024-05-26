#from EnemyGenerator import Enemy1
#from RPG import Player
import tkinter as GUI





#Enemy1.Inspect
#Player.InspectPlayer



def VictoryScreen():
    def close_window():
        WinScreen.destroy()
    WinScreen = GUI.Tk()
    WinScreen.title("Congratulations!")
    canvas = GUI.Canvas(WinScreen, width = 500, height = 500)
    canvas.pack()
    img = GUI.PhotoImage(file="E:\GitHub\Jensen\Back-End\Hobby stuff\RPG\Victory.ppm")
    canvas.create_image(50,50, anchor=GUI.NW , image=img)
    button = GUI.Button(WinScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    WinScreen.mainloop()

def Gameover():
    def close_window():
        WinScreen.destroy()
    WinScreen = GUI.Tk()
    WinScreen.title("Gameover!")
    canvas = GUI.Canvas(WinScreen, width = 500, height = 500)
    canvas.pack()
    img = GUI.PhotoImage(file="E:\GitHub\Jensen\Back-End\Hobby stuff\RPG\Victory.ppm")
    canvas.create_image(50,50, anchor=GUI.NW , image=img)
    button = GUI.Button(WinScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    WinScreen.mainloop()
# if Enemy1.EnemyHealth < 1
#   Victoryscreen()

# if Player.Health < 1
#   Gameover()
