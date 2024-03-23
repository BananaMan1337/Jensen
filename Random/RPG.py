name=input("What is your name?")
while True:
    try:
        age=int(input("How old are you?"))
        strength=int(input("On a scale of 1-10 how strong are you?"))
        intellect=int(input("On a scale of 1-10 how smart are you?"))
        agility=int(input("On a scale of 1-10 how agile are you?"))
        charisma=int(input("On a scale of 1-10 how good are you with people?"))
        break
    except ValueError:
        print("Please enter only numbers and without decimals.")
        continue


print("You awaken in a locked room. You cannot remember anything, but you know you dont want to stay here.")
while True:
    print("There is a door, a window, and a bookshelf.\n There seems to be someone on the other side of the door.")
    start=input("Which point of interest do you pick?").lower()
    accepted_strings = {"door", "window", "bookshelf"}
    if start=="door":
        print("The door is made out of wood and looks quite sturdy.")
        doorchoice=input("What do you want to do?\n Break the door down.\t Go back.").lower()
        accepted_strings={"break","break door","break down door", "break the door down"}
        if doorchoice in accepted_strings:
            if strength >=9:
                print("Breaking the door proves a trivial task for you.")       
            elif 6< strength <=8:
                print("Your break the door down with moderate ease.")
            elif 5<= strength <=6:
                print("You barely manage to break the door down.")
            elif strength <5:
                print("You are not strong enough to break the door down")
                continue
        else: continue
        print("Stepping out into the corridor you see that the door fell on top of the guard you heard through the door. He has been knocked out.")
        while True:
            corridor=input("You are standing in the corridor.\n Go left? \t Go right?").lower()
            accepted_strings={"go left","go right","left","right"}
            if corridor in accepted_strings:
                print("You continue walking until you find a door that leads outside.")
                break
            else: continue
        break
    
    if start=="window":
        print("The window is quite high up, it seems to be a thin pane of glass.")
        windowchoice=input("What do you want to do?\n Climb the wall.\t Go back.").lower()
        accepted_strings={"climb","climb wall","climb the wall"}
        if windowchoice in accepted_strings:
            if 8<= agility :
                print("Your level of agility makes climbing the wall a simple task.")
            elif 5<=agility <=7 :
                print("You climb the wall.")
            elif 3<= agility <=4:
                print("After a lot of attempts you finally make it up, your fingers hurt.")
            elif agility <4:
                print("You try to climb the wall but you cant even make it close.")
                continue
        else: continue
        print("You break the glass and climb out")
        break

    if start=="bookshelf":
        print("The bookshelf is filled with a curious assortment of books.")
        bookshelfchoice=input("What do you want to do?\n Look for interesting books.\t Try to push the bookshelf.\t Go back.").lower()
        accepted_strings={"look for interesting books","look for books","books"}
        accepted_strings2={"push","try to push","try to push the bookshelf"}
        if bookshelfchoice in accepted_strings2:
            if strength >=9:
                print("The bookshelf weighs nothing to you, you push it and reveal a door.")       
            elif 6< strength <=8:
                print("You push the bookshelf and reveal a door.")
            elif 5<= strength <=6:
                print("You struggle a little to push it but it reveals a door")
            elif 2<= strength <5:
                print("After a lot of pushing and swearing, you finally manage to get it moving and reveal a door.")
            elif 0<= strength <2:
                print("You are too weak to push it")
                continue
            else:continue
        elif bookshelfchoice in accepted_strings:
            if 8<= intellect:
                print("You easily spot a fake book among the many books you've already read. Pulling it out reveals a level which moves the bookcase and reveals a door")
            elif 5<= intellect <8:
                print("After some pondering you notice a book that doesnt seem to fit in with the rest. Pulling it out reveals a lever which moves the bookcase and reveals a door")
            elif 0<= intellect <5:
                print("After playing around and using the books as toys, you manage to fall and hit a suspicious book which reveals a lever that moves the bookcase and reveals a door")
        else:continue
        print("You open the door and realise that it leads outside")  
        break  
print("You feel the fresh air fill your lungs as you look to the sky. You have escaped.")
