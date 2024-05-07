

#region Function for list with square root
#This function takes the inputted list of numbers and returns the square root of the same numbers.
def listfunction(list):
    #Defines and names the function
    newlist= []
    #Make a new list to put new numbers in
    for element in list:
        #For every element in the list, do the following
        newelement = pow(element,2)
        #set newelement to multiplication of the element by itself
        newlist.append(newelement)
        #add newelement to the new list
    return newlist
#returns newlist as the answer
    

print(listfunction([2,4,5,6,7,10]))
#endregion


#region Function to remove åäö from a string
def letterchange(sentence):
    #defines function and the string
    Changedsentence = ""
    #new sentence when we are done
    for letter in sentence:
        #for every letter in the sentence do the following
        if letter == "Ö":
            Changedsentence= Changedsentence +"O"
        elif letter == "ö":
            Changedsentence= Changedsentence +"o"
        elif letter == "Ä":
            Changedsentence= Changedsentence +"A"
        elif letter == "ä":
            Changedsentence= Changedsentence +"a"
        elif letter == "Å":
            Changedsentence= Changedsentence +"A"
        elif letter == "å":
            Changedsentence= Changedsentence +"a"         
            #all of the above removes the Swedish letters   
        else:
            Changedsentence = Changedsentence  + letter
            #If it wasnt a Swedish letter, just add the same letter that was inputted
    return Changedsentence
#Returns the edited sentence
print(letterchange("Ön nära östermalm. Passa dig för ålar!"))
#endregion


#region Function to remove åäö from a list
def letterchange(wordlist):
    #Defines the function and the list
    Changedwordlist = []
    #Our new list
    for letter in wordlist:
        if letter == "Ö":
            Changedwordlist.append("O")
        elif letter == "ö":
            Changedwordlist.append("o")
        elif letter == "Ä":
            Changedwordlist.append("A")
        elif letter == "ä":
            Changedwordlist.append("a")
        elif letter == "Å":
            Changedwordlist.append("A")
        elif letter == "å":
            Changedwordlist.append("a")          
            #Here we have to use append instead since its a list
        else:
            Changedwordlist.append(letter)
            #If its not a Swedish letter, just add it into the new list
    return ''.join(Changedwordlist)
#Turns the list into a string, not really sure how it works.
print(letterchange("Ön nära östermalm. Passa dig för ålar!"))
#endregion


#region Function to calculate average number from a list

def SalaryAverage(Salary):
    #defines function
    Salarynumber= len(Salary)
    #Salarynumber is the length of salary
    if Salarynumber == 0:
        #If zero print below
        print("No salary given")
    average = sum(Salary) / Salarynumber    
    #average is the sum of salary divided by salary number
    return average
#returns average
    

Salarynumber = int(input("Input number of salaries"))
# integer input asking for amount of salaries
Salary = []
#Turns salary into a list

for i in range(Salarynumber):
    #for the number of salaries inputted, ask for that many amounts
    Salaryamount = float(input(f"Input salary amount"))
#"f" är en prefix för en så kallad "f-string" i Python. Den tillåter dig att inkludera variabler direkt inuti en sträng genom att placera dem inom klammerparentes {}.
    Salary.append(Salaryamount)
    #appends salary with salaryamount

average = SalaryAverage(Salary)
#sets average

print("Average salary is ", average)
#endregion
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!This was a bit hard to do, ill need to revise this in the future!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#region calculator
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
#endregion
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!I want to be able to multiply and divide several numbers but im bad at math!!!
#!!!So i dont know how to make that work well                                  !!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

