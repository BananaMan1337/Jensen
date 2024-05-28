
#battle sequence adds exp to experience variable. 
#If experiece >= 100 
#   experience = 0
#   Level = 2
#fix potion in battle sequence

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = "inventory.txt"
file_path = os.path.join(current_dir, filename)

Victory_path = os.path.join(current_dir, 'Victory.ppm')
Gameover_path = os.path.join(current_dir, 'Gameover.ppm')

if os.path.exists(file_path):
    os.remove(file_path)
    with open(file_path, 'a') as file:
        print("Inventory purged")
else:
    with open(file_path, 'a') as file:
        print("Inventory created")
    

def spacing():
    print("\n" * 3)
    print("_________________________________________________")
#region Player
class PlayerGen:
    def __init__(self, Name, Age, PlayerLevel, Health, Experience, Strength, Intellect, Agility, Charisma):
        self.Name = Name
        self.Age = Age
        self.Level = PlayerLevel
        self.Health = Health
        self.Experience = Experience
        self.Strength = Strength
        self.Intellect = Intellect
        self.Agility = Agility
        self.Charisma = Charisma
    def Attack(self, enemy):
        print(f"You attack the enemy {enemy.Race}")
        Damage = self.Strength + self.Level
        enemy.Health = enemy.Health - Damage
        print(f"You deal {Damage} damage to the enemy {enemy.Race}")
    def Inspect(self):
        return print(f"Name: {self.Name}\nAge: {self.Age}\nLevel: {self.Level}\nHealth: {self.Health} HP")
 
def PlayerGenerate():
 
        Name = input("What is your name?\n")
        Age = int(ValidatedInput("How old are you?\n", 18, 99))
        Strength = int(ValidatedInput("On a scale of 1-10 how strong are you?\n", 1, 10))
        Intellect = int(ValidatedInput("On a scale of 1-10 how smart are you?\n", 1, 10))
        Agility = int(ValidatedInput("On a scale of 1-10 how agile are you?\n", 1, 10))
        Charisma = int(ValidatedInput("On a scale of 1-10 how good are you with people?\n", 1, 10))
        PlayerLevel = 1
        Health = 30
        Experience = 0
        spacing()
        return PlayerGen(Name, Age, PlayerLevel, Health, Experience, Strength, Intellect, Agility, Charisma)
 
 
def ValidatedInput(msg, min, max):
    try:
        inputVal = int(input(msg))
        while inputVal > max or inputVal < min:
            if inputVal > max:
                print(">> Number too big")
                inputVal = int(input(msg))
            if inputVal < min:
                print(">> Number too small")
                inputVal = int(input(msg))
        return int(inputVal)
    except ValueError:
            print(">> Please enter only numbers and without decimals.")
            ValidatedInput(msg, min, max)
    except TypeError:
            print(">> Please enter only numbers and without decimals.")
            ValidatedInput(msg, min, max)
#endregion
 
#region Battle gen
import time

def Battle(player, enemy):
    spacing()
    print("Battle Commences")
    print("Enemy")
    print(enemy.Inspect())
    print("Player") 
    print(player.Inspect())
    time.sleep(3)
    while True:
        if player.Health <= 0:
            with open(file_path, 'r+') as file:
                content = file.read()
                if "potion" in content.lower():
                    file.seek(0)
                    PotionRemove = content.replace("potion", "")
                    file.write(PotionRemove)
                    Player.Health = Player.Health + 20
                    spacing()
                    print("You cheat death by drinking your potion and restoring 20 hp")
                    time.sleep(2)
                else:
                    Gameover()
                    break
        elif enemy.Health <= 0:
            VictoryScreen()
            global wallet
            wallet = wallet + 50
            print(f"The enemy {enemy.Race} dies.")
            print(f"You loot 50 gold off the {enemy.Race}, your wallet now contains {wallet} gold.")
            break
        else:
            try: 
                spacing()
                print("What would you like to do?\n Attack\tInspect\tRun")
                Battlechoice = input().lower()
                match Battlechoice:
                    case "attack":
                        spacing()
                        player.Attack(enemy)
                        enemy.Attack(player)
                        time.sleep(3)
                        continue
                    case "inspect":
                        spacing()
                        print(enemy.Inspect())
                        time.sleep(2)
                        continue
                    case "run":
                        print("You cannot escape!")
                        time.sleep(1)
                        continue
                    case _:
                        print("Bad input, try again!")
                        time.sleep(1)
                        continue
            except Exception as e:
                print("An unexpected error occured", e)
                print("Please try again")
                continue
#region Battle GUI     
import tkinter as GUI
def VictoryScreen():
    def close_window():
        WinScreen.destroy()
    WinScreen = GUI.Tk()
    WinScreen.title("Congratulations!")
    canvas = GUI.Canvas(WinScreen, width = 500, height = 500)
    canvas.pack()
    img = GUI.PhotoImage(file=Victory_path)
    canvas.create_image(50,50, anchor=GUI.NW , image=img)
    button = GUI.Button(WinScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    WinScreen.attributes("-topmost", True)
    WinScreen.mainloop()
 
def Gameover():
    def close_window():
        DeadScreen.destroy()
        exit()
    DeadScreen = GUI.Tk()
    DeadScreen.title("Gameover!")
    canvas = GUI.Canvas(DeadScreen, width = 650, height = 500)
    canvas.pack()
    img = GUI.PhotoImage(file=Gameover_path)
    canvas.create_image(50,50, anchor=GUI.NW , image=img)
    button = GUI.Button(DeadScreen, text="Finished", command=close_window)
    button.pack(pady=20)
    DeadScreen.attributes("-topmost", True)
    DeadScreen.mainloop()
 #endregion
#region Enemy
import random
 
class Enemy:
    def __init__(self, EnemyRace, EnemyClass, EnemyLevel, EnemyHealth):
        self.Race = EnemyRace
        self.Class = EnemyClass
        self.Level = EnemyLevel
        self.Health = EnemyHealth
    def Attack(self, Player):
        attack = ""
        element = ""
        match self.Class:
            case "Warrior":
                attack = " swings its axe"
                element = " physical"
            case "Rogue":
                attack = " shoots its bow"
                element = " ranged"
            case "Mage":
                attack = " casts fireball"
                element = " fire"
        Damage = 5 + self.Level
        Player.Health = Player.Health - Damage
        print(f"The enemy {self.Race}{attack}.")
        print(f"You take {Damage}{element} damage.")
        return print(f"You have {Player.Health} HP Remaining")
    def Inspect(self):
        return f"{self.Race} {self.Class} at level {self.Level} with {self.Health} HP"
    
def Generate(player):
    Race = ['Goblin', 'Human', 'Elf', 'Ogre', 'Bandit']
    Class = ['Warrior', 'Rogue', 'Mage']
    Level = player.Level + random.randint(0, 3)
    MobHealth = 30 + Level
    return Enemy(random.choice(Race), random.choice(Class), Level, MobHealth)
#endregion
 
#region Wallet & Inventory
wallet = 0
def purchase (wallet, price):
    if wallet >= price:
        wallet = wallet - price
        print(wallet,"gold left")
        return True, wallet
    else:
        print("Not enough gold")
        return False, wallet
    
def write_to_inventory(item):
    with open(file_path, 'a') as file:
        file.write(item + "\n")    

#endregion

 
Player = PlayerGenerate()
Player.Inspect()
time.sleep(3)
enemy = Generate(Player)
Guard = Enemy("Human", "Warrior", 2, 20)

#other code
#region Start Choice
spacing()
print("You awaken in a locked room. You cannot remember anything, but you know you dont want to stay here.\n")
while True:
    print("There is a door, a window, and a bookshelf.\nThere seems to be someone on the other side of the door.\nYou realise you still have your wallet")
    start=input("Which point of interest do you pick?\n").lower()
    accepted_strings = ("door", "window", "bookshelf","wallet")
#endregion
#region Door Choice
    if start=="door":
        spacing()
        print("The door is made out of wood and looks quite sturdy.")
        doorchoice=input("What do you want to do?\n Break the door down.\t Try to talk to the person on the other side.\t Go back.\n").lower()
        accepted_strings=("break","break door","break down door", "break the door down")
        accepted_strings2=("talk","talk to person","talk to door","speak","talk to the person on the other side")
        spacing()
 
        if doorchoice in accepted_strings:
            if Player.Strength >=9:
                print("Breaking the door proves a trivial task for you.\n The guard attacks!")       
                time.sleep(3)
                Battle(Player, Guard)                
            elif 6< Player.Strength <=8: 
                print("Your break the door down with moderate ease.\n The guard attacks!")
                time.sleep(3)
                Battle(Player, Guard)
            elif 5<= Player.Strength <=6:      
                print("You barely manage to break the door down.\n The guard attacks!")
                time.sleep(3)
                Battle(Player, Guard)
            elif Player.Strength <5:
                print("You are not strong enough to break the door down")
                continue
        elif doorchoice in accepted_strings2:
            spacing()   
            print("You ask them where you are, they respond with\n \"Be quiet prisoner\"")
            guardchoice = input("What do you want to do?\n Try to bribe the guard.\t Go back.\n").lower()
            accepted_strings=("bribe","bribe the guard","try to bribe","try to bribe the guard")
            spacing()
            if guardchoice in accepted_strings:
                result = purchase(wallet, 50)
                BribeCheck = result[0]
                wallet = result[1]
                if BribeCheck == True and Player.Charisma >= 6:
                    print("\"Fine, ill let you out. I better never see you again.\"")
                    time.sleep(2)
                elif BribeCheck == True and Player.Charisma < 6:                 
                    print("\"Hah, thanks for the gold\"")
                    time.sleep(2)
                    continue
                elif BribeCheck == False:                   
                    print("\"Get back to your cell prisoner. You dont have enough gold.\"")
                    time.sleep(2)
                    continue
                else: continue
            else: continue
        else: continue
 
        while True:
            print("You exit the room and find yourself in a corridor.")
            corridor=input("You are standing in the corridor.\n Go left? \t Go right?\n").lower()
            accepted_strings=("go left","go right","left","right")
            if corridor in accepted_strings:
                print("You continue walking until you find a door that leads outside.")
                break
            else: continue
        break
#endregion
#region Window Choice
    if start=="window":      
        print("The window is quite high up, it seems to be a thin pane of glass.")
        windowchoice=input("What do you want to do?\n Climb the wall.\t Go back.\n").lower()
        accepted_strings=("climb","climb wall","climb the wall")
        spacing()
        if windowchoice in accepted_strings:
            if 8<= Player.Agility :
                print("Your level of Player.Agility makes climbing the wall a simple task.")
            elif 5<=Player.Agility <=7 :
                print("You climb the wall.")
            elif 3<= Player.Agility <=4:
                print("After a lot of attempts you finally make it up, your fingers hurt.")
            elif Player.Agility <4:
                print("You try to climb the wall but you cant even make it close.")
                time.sleep(2)
                continue
        else: continue     
        print("You break the glass and climb out")
        break
#endregion
#region Bookshelf
    if start=="bookshelf":
        spacing()     
        print("The bookshelf is filled with a curious assortment of books.")
        bookshelfchoice=input("What do you want to do?\n Look for interesting books.\t Try to push the bookshelf.\t Loot.\t Go back.\n").lower()
        spacing()
        accepted_strings=("look for interesting books","look for books","books")
        accepted_strings2=("push","try to push","try to push the bookshelf")
 
        if bookshelfchoice in accepted_strings2:
            if Player.Strength >=9:
                print("The bookshelf weighs nothing to you, you push it and reveal a door.")       
            elif 6< Player.Strength <=8:
                print("You push the bookshelf and reveal a door.")
            elif 5<= Player.Strength <=6:
                print("You struggle a little to push it but it reveals a door")
            elif 2<= Player.Strength <5:
                print("After a lot of pushing and swearing, you finally manage to get it moving and reveal a door.")
            elif 0<= Player.Strength <2:
                print("You are too weak to push it")
                time.sleep(2)
                continue
            else:continue
 
        elif bookshelfchoice in accepted_strings:
            if 8<= Player.Intellect:
                print("You easily spot a fake book among the many books you've already read. Pulling it out reveals a level which moves the bookcase and reveals a door")
            elif 5<= Player.Intellect <8:
                print("After some pondering you notice a book that doesnt seem to fit in with the rest. Pulling it out reveals a lever which moves the bookcase and reveals a door")
            elif 0<= Player.Intellect <5:
                print("After playing around and using the books as toys, you manage to fall and hit a suspicious book which reveals a lever that moves the bookcase and reveals a door")      
 
        elif bookshelfchoice == "loot":
            spacing()
            print("You find some gold")
            wallet = wallet + 50
            print("You now have", wallet, "gold")
            time.sleep(2)
            continue
        else:continue
        print("You open the door and realise that it leads outside")  
        break  
#endregion
 
    if start =="wallet":
        print("The wallet contains",wallet,"gold")
        time.sleep(3)
        spacing()
        continue
#region Escape + Town    
time.sleep(2)
spacing() 
print("You feel the fresh air fill your lungs as you look to the sky. You have escaped.")
while True:
    spacing()
    TownChoice = input("You find yourself in a town.\n Where would you like to go?\n Shop\t Inn\t Leave town\n").lower()
    accepted_strings=("leave", "leave town")
    spacing()
    if TownChoice == "shop":
        print("You enter a dusty little shop in an old building.\n An old woman hails you as you enter.")
        print("Good day to you sir! Fancy any of my wares?")
        print("*Most of the items here look terrible, however you do spot something of use*")
        Shop = {"Potion":"10g", "Short Sword":"100g"}
        print(Shop, "leave")
        ShopChoice = input().lower()
        if ShopChoice == "potion":
            result = purchase(wallet,10)
            ShopCheck = result[0]
            wallet = result[1]
            if ShopCheck == True:
                print("Potion bought!")
                write_to_inventory("Potion")
                time.sleep(2)
            elif ShopCheck == False:
                print("You return to town with no potion.")
                time.sleep(2)
                continue
        elif ShopChoice == "short sword" "sword":
            purchase(wallet, 100)
            time.sleep(3)
            continue
        else: continue
    elif TownChoice == "inn":
        print("The floorboards creak underneath you as you walk up to the old man by the counter")
        print("\"Greetings! Looking for a room?\"")
        InnChoice = input("Room (10g)\t Leave").lower()
        if InnChoice == "room":
            result = purchase(wallet, 10)
            InnCheck = result[0]
            wallet = result[1]
            if InnCheck == True:
                spacing()
                print(wallet,"gold remaining")
                print("You rest for a bit and wake up feeling refreshed. \n *Health restored*")
                Player.Health = 50
                print("You return to town.")
                time.sleep(3)
                continue
            elif InnCheck == False:
                print("You return to town unrested.")
                time.sleep(3)
                continue
            else:
                continue
    elif TownChoice in accepted_strings:
        break   
    else: 
        continue
print("You exit the town and find yourself in a forest.\n You hear rustling in the bushes behind you and something pops out!")
time.sleep(2)
Battle(Player, enemy)
#endregion