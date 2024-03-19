name = input("What is your name?")
age = int(input("Hur gammal är du?"))
#int cause whole number
height = float(input("Hur lång är du i cm?"))
#float cause decimals possible

print("Hej", name,"du är",age,"år gammal och",height,"cm lång")
#prints name, age, height

ordtal=input("Input number")
print(5*ordtal)
#prints inputinputinputinputinput


tal= int(input ("Input number"))
print(5 * tal)
#since its an int this time and not a string it will actually print 5*inputted number

fee= 358.3
#Specify price per hour
namn=input("Hej! Välkommen till BananaFitness, vad är ditt namn?")
#grabs name
hours=float(input("Hur många timmar i veckan tänkte du att träna med oss?"))
#grabs hours per week, float in case half hours
print("Vad kul", namn+"!", "För att träna", hours, "timmar i veckan så skulle det kosta", hours*fee,"kr per vecka")
#prints some nice words while saying their name, amount of hours and cost per week by doing hours * fee
print (round (1337.1337,2))
print (round (1337.1337))
#Rounds up numbers, if you type (1337.1337) and round it it will round down, however if you add a comma with a number it will 
#show that many decimal points.
name=input("Vad är ditt namn?")
print("Hej",name+"!")

age=int(input("Hur gammal är du?"))
print("Om 5 år så är du", age+5,"år gammal")
#age plus five

längd=float(input("Hur lång är du i meter?"))
print("Du är",längd*100,"cm lång")
#simple code to convert meters to cm

print(round (188.987123,2))
print(round (188.987123,1))
print(round(188.987123))

maxpulse=220
age=int(input("Hur gammal är du?"))
print("Din max puls borde vara", maxpulse-age,"BPM")
#Calculates max pulse - age 

multi1=float(input("nummer 1 :"))
#Specify first number to be multiplied
multi2=float(input("nummer 2 :"))
#Specify second number to be multiplied
multi3=float(input("nummer 3 :"))
multi4=float(input("nummer 4 :"))
result = multi1*multi2*multi3*multi4
print("produkten är",result)
#result
print(round(result))

for n in range(5):
    print("hej")
#for all variables in range (indentation), repeat 5x

for n in range(5):
print("hej")
#No indentation so doesnt work

for x in range(1,6):
    print(x)
#loop to print 1-5, if you do range(6)it prints a zero to 5, so 6 loops. Ergo you always add one extra
#if i want it to print up to 5, i write 6
#if you want it to print up to 10, you write 11
#In this case we specify we want it to start as 1, it is the first variable that X is, instead of the default 0
#Therefore we get 1-5 instead of 0-5
    