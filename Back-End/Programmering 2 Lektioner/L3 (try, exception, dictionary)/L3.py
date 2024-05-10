#Try except is almost like if else
#If you run code in try that fails, instead of crashing it will do the except code

def read_wholenumber():
#function
    try:
        wholenumber= int(input("Write a number without decimals:"))
        print("You wrote", wholenumber)
        #wholenumber is an int so if you input decimals it wont work
    except:
        print("You did not input a number without decimals")
    #error message if wrong input
read_wholenumber()
#call the function


try:
    num = int(input("Write a whole number that will be divided by 10"))
    result = 10 / num
    #try asking for a whole number and assign that number to the variable num
    #result is 10 divided by the inputted number
except ValueError:
    print("Bad input, only put in whole numbers")
    #ValueError runs if there is an error in the value given, if it has decimals etc

except ZeroDivisionError:
    print("Division by zero is not allowed")
    #This runs if they input zero as that doesnt work
except Exception as e:
    print("An unexpected error occured", e)
    #If there is another error, this takes the error and assigns it to the variable e. We then print out e to the user.
else:
    print("No error occured, result of 10 /", num, "is:", result)
    #This runs if no errors occurs
finally:
    print("The program is finished")
#This always runs after all of the above



try:
    with open("1.txt","r") as file:
        content = file.read()
except Exception as e:
    print("An unexpected error has occured", e)


#Exercise 1

try:
    num = input(print("Input a whole number"))
    result = pow(num,2)
except ValueError:
    print("Bad input")

#exercise 2
try:
    num = int(input(print("Input a whole number")))
    result = pow(num, 2)
except ValueError:
    print("Bad input")
else: 
    print(num, "squared is", result)



#exercise 3
while True:
    try:
        num1 = int(input("Input your first number"))
        num2 = int(input("Input your second number"))
        print (num1, "divided by", num2, "is", num1/num2)
        break
    

    except ValueError:
        print("Bad input, try again")
        continue
#This works but is not that good of a way


def divisionfunction ():
    try:
        num1 = int(input("Input your first number"))
        num2 = int(input("Input your second number"))
        print (num1, "divided by", num2, "is", num1/num2)
        divisionfunction()
    except ValueError:
        print("Bad input, try again")
        divisionfunction()        

divisionfunction()



pensionage = 65
def pensionagefunction ():
    try:
        age = int(input("Input your age."))
        result = pensionage - age
        if 1 <= age <= 64:
            print(result,"years left until pension")
            pensionagefunction ()
        elif age >= 65:
            print("You are already pension age")
            pensionagefunction ()
        else:
            print("Are you not born yet? Try again.")
            pensionagefunction ()

    except ValueError:
        print("Bad input, try again")
        pensionagefunction()        

pensionagefunction()
#potential to remove the function fron if and elif and put a finally at the end
#finally:
#   print("Program has finished running")




#Extra uppgift
#Calculates average grade with inputted amount of classes and their points
def AverageScore():
    try:
        ClassNumber = int(input("Input number of classes"))
        Grade = []
        for i in range(ClassNumber):
            GradeAmount = float(input(f"Input class points"))
            Grade.append(GradeAmount)
        average = sum(Grade) / ClassNumber    
        print("You had an average of", average,"points")
    except ValueError:
        AverageScore()



AverageScore()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DICTONARY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Dictionary use {} and doesnt let you define orderered elements. Instead you have a key/value for the elements
#Dictionaries are ordered and changable but doesnt allow duplicates
Dic = {"Brand", "Volvo","Model", "XC60", "year", 2024}
print(Dic)

#Both lists and dictionaries can be spread over several lines like so
Dic = {"Brand", 
       "Volvo",
       "Model", 
       "XC60", 
       "year",
        2024}

#key looks like this 
Person = {"Name": "Lisa", "Lastname": "Tepes"}
#Here the keys are name and lastname
#whilst elements would be Lisa and Tepes
print(Person["Name"])
#This would print Lisa

Person = {"Name": "Lisa", "Lastname": "Tepes", "Age": "30"}
var = input("Input attribute")
try:
    print(Person[var])
except KeyError:
    print("Error, attribute doesnt exist")
#This code asks for an input, if you type Name, Lastname or Age, it will return the answer


Person = {"Name": "Lisa", "Lastname": "Tepes", "Age": "30"}
print("Hi, my name is", Person["Name"], "and I am", Person["Age"], "years old" )
#Here we take the name and age of the person from the dictionary
#If we didnt have "30" and instead had 30
#we would need to do this
print("Hi, my name is", Person["Name"], "and I am", str(Person["Age"]), "years old" )
#Here we convert age into a string


#To add elements
Person = {"Name": "Lisa", "Lastname": "Tepes", "Age": "30"}
Person["Hair"] = "Blonde"

#del to delete

