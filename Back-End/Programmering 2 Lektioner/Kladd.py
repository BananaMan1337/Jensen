def addition(numbers):
    result = sum(numbers)
    return result

def subtraction(MainNumber,Subtractionnumber):
    result = (MainNumber - sum(Subtractionnumber))
    return result

def divide(Mainnumber, Dividenumber):
    result= (Mainnumber / Dividenumber)
    return result

def mulitply(Mainnumber, Multiplynumber):
    result= (Mainnumber * Multiplynumber)
    return result

while True:
    path=input("What would you like to do? Add, subtract, divide, multiply, quit?").lower()
    acceptedstrings=["add","subtract","divide", "multiply","quit"]
    if path == "add":
        Addends = int(input("How many numbers are you adding?"))
        numbers = []
        for i in range(Addends):
            AddendsValue = float(input(f"Input a number"))
            numbers.append(AddendsValue)
        result= addition(numbers)
        print("The sum is ",result)
        continue

    elif path =="subtract":
        MainNumber = int(input("What number would you like to subtract from?"))
        Subtractionnumber = []
        SubtractionNumberAmount = int(input("How many different numbers are you subtracting?"))
        for i in range(SubtractionNumberAmount):
            Subtractionamount = float(input(f"Input a number"))
            Subtractionnumber.append(Subtractionamount)
        result= subtraction(MainNumber,Subtractionnumber)
        print("Answer is ",result)        
        continue

    elif path =="divide":
        Mainnumber= float(input("What number would you like to divide?"))
        Dividenumber=float(input("What would you like to divide it by?"))
        result = divide(Mainnumber, Dividenumber)
        print("Answer is ", result)
        continue

    elif path =="multiply":
        Mainnumber= float(input("What number would you like to multiply?"))
        Multiplynumber=float(input("What would you like to multiply it by?"))
        result = mulitply(Mainnumber, Multiplynumber)
        print("Answer is ", result)
        continue
    elif path =="quit":
        break
    else:
        print("Bad input")
        continue