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
    while True:
        print("There is a door, a window, and a bookshelf.\n There seems to be someone on the other side of the door.")
        start=input("Which point of interest do you pick?").lower()
        accepted_strings = {"door", "window", "bookshelf"}
        if start in accepted_strings:
            break
        else: continue
    if start=="door":
        print("The door is made out of wood and looks quite sturdy.")
        doorchoice=input("What do you want to do?\n Break the door down.\t Go back.").lower()
        accepted_strings={"break","break door","break down door", "break the door down","go back","back"}
    if doorchoice=="back":
        continue
    if doorchoice=="go back":
        continue
    if doorchoice in accepted_strings:
        if strength < 8 >= 6:
            print("You barely manage to break the door down.")
            break
        elif strength >6 <=8:
            print("Your break the door down with moderate ease.")
            break
        elif strength >8:
            print("Breaking the door proves a trivial task for you.")
            break
        elif print("You are not strong enough to break the door down"):
            continue
        print("Stepping out into the corridor you see that the door fell on top of the guard you heard through the door. He has been knocked out.")
        while True:
            corridor=input("You are standing in the corridor.\n Go left? \t Go right?").lower()
            accepted_strings={"go left","go right","left","right"}
            if corridor in accepted_strings:
                print("You continue walking until you find a door that leads outside.")
                break
            else: continue

    if start=="window":
        print("The window is quite high up, it seems to be a thin pane of glass.")
        windowchoice=input("What do you want to do?\n Climb the wall.\t Go back.").lower()
        accepted_strings={"climb","climb wall","climb the wall","go back","back"}
        if windowchoice=="go back":
            continue
        if windowchoice=="back":
            continue
        if windowchoice in accepted_strings:
            if agility >=3:
                print("After a lot of attempts you finally make it up, your fingers hurt.")
                break
            elif agility >=6:
                print("You climb the wall.")
                break
            elif agility >=8:
                print("Your level of agility makes climbing the wall a simple task.")
                break
            else: print("You try to climb the wall but you cant even make it close.")
            continue  
    print("You break the glass and climb out")

#if start=="bookshelf":
#    print("The bookshelf is filled with a curious assortment of books.")
 #   bookshelfchoice=input("What do you want to do?\n Look for interesting books.\t Try to push the bookshelf.\t Go back.").lower()
  #  accepted_strings={"look for interesting books","look for books","books,"}
   # if bookshelfchoice in accepted_strings: