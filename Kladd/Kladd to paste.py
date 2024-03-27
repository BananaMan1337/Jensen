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
def bookshelffunction(var1,var2):
    strint = var1 + var2
    return strint
print(bookshelffunction(strength,intellect))