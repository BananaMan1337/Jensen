from EnemyGenerator import Generate
import tkinter as GUI

def Battle():
    Enemy1 = Generate()
    print("Battle Commences")
    print(Enemy1.Inspect())
    print(Player.InspectPlayer())
    while True:
        if Player.Health <= 0:
            Gameover()
            break
        elif Enemy1.EnemyHealth <= 0:
            VictoryScreen()
            break
        else:
            try: 
                Battlechoice = input(print("What would you like to do?\n Attack\tInspect\tRun")).lower()
                if Battlechoice == "attack":
                    Player.PlayerAttack()
                    Enemy1.EnemyAttack()
                    continue
                elif Battlechoice == "inspect":
                    print(Enemy1.Inspect())
                    continue
                elif Battlechoice == "run":
                    print("You cannot escape!")
                    continue
                else:
                    print("Bad input, try again!")
                    continue
            except Exception as e:
                print("An unexpected error occured", e)
                print("Please try again")
                continue
        






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
        DeadScreen.destroy()
    DeadScreen = GUI.Tk()
    DeadScreen.title("Gameover!")
    canvas = GUI.Canvas(DeadScreen, width = 650, height = 500)
    canvas.pack()
    img = GUI.PhotoImage(file="E:\GitHub\Jensen\Back-End\Hobby stuff\RPG\Gameover.ppm")
    canvas.create_image(50,50, anchor=GUI.NW , image=img)
    button = GUI.Button(DeadScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    DeadScreen.mainloop()
# if Enemy1.EnemyHealth < 1
#   Victoryscreen()

# if Player.Health < 1
#   Gameover()
