name = input("What is your name?")
print("Greetings", name)

purpose= input("What is thy purpose?")
if purpose.lower()=="banana":
    print("YES, YOU UNDERSTAND THE GOSPEL OF GOD")
    print("Good boy, you may now leave")
else:
    print("If its not banana,", name+", then i dont want to hear it" )
    path= input("Do you want to become a banana enjoyer?")
if path.lower()=="yes":
    print("Good boy!")
else:
    print("THEN PAY WITH YOUR BLOOD")
    fight= input("Fight\t Magic\n Item\t Run")
    if fight.lower()=="fight"