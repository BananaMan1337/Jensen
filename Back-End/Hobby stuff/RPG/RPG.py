
#File handling för att göra ett inventory dokument?


#battle sequence adds exp to experience variable. 
#If experiece >= 100 
#   experience = 0
#   Level = 2

import PlayerFile
Player = PlayerFile.PlayerGenerate()
Player.InspectPlayer()
#region Wallet & Money
wallet = 0
def purchase (wallet, price):
    if wallet >= price:
        wallet = wallet - price
        print(wallet,"gold left")
        return True, wallet
    else:
        print("Not enough gold")
        return False, wallet
#endregion

#region Start Choice
print("You awaken in a locked room. You cannot remember anything, but you know you dont want to stay here.")
while True:
    print("There is a door, a window, and a bookshelf.\n There seems to be someone on the other side of the door.\n You realise you still have your wallet")
    start=input("Which point of interest do you pick?").lower()
    accepted_strings = ("door", "window", "bookshelf","wallet")
    
#endregion

#region Door Choice
    if start=="door":
        print("The door is made out of wood and looks quite sturdy.")
        doorchoice=input("What do you want to do?\n Break the door down.\t Try to talk to the person on the other side.\t Go back.").lower()
        accepted_strings=("break","break door","break down door", "break the door down")
        accepted_strings2=("talk","talk to person","talk to door","speak","talk to the person on the other side")

        if doorchoice in accepted_strings:
            if Player.Strength >=9:
                print("Breaking the door proves a trivial task for you.")       
            elif 6< Player.Strength <=8: 
                print("Your break the door down with moderate ease.")
            elif 5<= Player.Strength <=6:      
                print("You barely manage to break the door down.")
            elif Player.Strength <5:
                print("You are not strong enough to break the door down")
                continue
        elif doorchoice in accepted_strings2:
            
            print("You ask them where you are, they respond with\n \"Be quiet prisoner\"")
            guardchoice = input("What do you want to do?\n Try to bribe the guard.\t Go back.").lower()
            accepted_strings=("bribe","bribe the guard","try to bribe","try to bribe the guard")
            if guardchoice in accepted_strings:
                result = purchase(wallet, 50)
                BribeCheck = result[0]
                wallet = result[1]
                if BribeCheck == True and Player.Charisma >= 6:
                    print("\"Fine, ill let you out. I better never see you again.\"")
                elif BribeCheck == True and Player.Charisma < 6:                    
                    print("\"Hah, thanks for the gold\"")
                    continue
                elif BribeCheck == False:                   
                    print("\"Get back to your cell prisoner. You dont have enough gold.\"")
                    continue
                else: continue
            else: continue
        else: continue
  
        while True:
            print("You exit the room and find yourself in a corridor.")
            corridor=input("You are standing in the corridor.\n Go left? \t Go right?").lower()
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
        windowchoice=input("What do you want to do?\n Climb the wall.\t Go back.").lower()
        accepted_strings=("climb","climb wall","climb the wall")
        if windowchoice in accepted_strings:
            if 8<= Player.Agility :
                print("Your level of Player.Agility makes climbing the wall a simple task.")
            elif 5<=Player.Agility <=7 :
                print("You climb the wall.")
            elif 3<= Player.Agility <=4:
                print("After a lot of attempts you finally make it up, your fingers hurt.")
            elif Player.Agility <4:
                print("You try to climb the wall but you cant even make it close.")
                continue
        else: continue     
        print("You break the glass and climb out")
        break
#endregion
#region Bookshelf
    if start=="bookshelf":     
        print("The bookshelf is filled with a curious assortment of books.")
        bookshelfchoice=input("What do you want to do?\n Look for interesting books.\t Try to push the bookshelf.\t Loot.\t Go back.").lower()
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
            print("You find some gold")
            wallet = wallet + 50
            print("You now have", wallet, "gold")
            continue
        else:continue
        print("You open the door and realise that it leads outside")  
        break  
#endregion

    if start =="wallet":
        print("The wallet contains",wallet,"gold")
        continue
print("You feel the fresh air fill your lungs as you look to the sky. You have escaped.")