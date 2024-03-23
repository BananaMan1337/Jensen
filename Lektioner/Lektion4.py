for x in range(1,6):
    print("Jag fyller", x, "år!")
#prints "Jag fyller x år" 5 times, with increasing age each time
for n in range(1,17,3):
    print(n)
#third number is the step, the distance it jumps everytime, so it runs 1->4->7 etc in the pattern of 3
for n in range(1,5):
    print("Jensen1")
    #Same as the bottom one except 1,5
for n in range(4):
    print("Jensen2")
    #Since its text and doesnt count you can just write 4 instead of 1,5
for a in range(1,12):
    print(a)
for b in range(1,101):
    print(b)
for c in range(-100,6):
    print(c)




#Anton exercise
for n in range(0,51):
    print(2*n)
#Anton wants to it to paste every even number between 1-100,
#Instead of doing
for n in range(0,101,2):
    print(n)
#which would be to print 0-100 in steps of 2
#he instead goes 0-51 with no step, but with the print multiplying the variable n
#therefore it goes 2*n = 0, loops around so n is 1, 2*n = 2, loops around so n is 2, 2*n = 4 and so forth
    


for n in range(1,11):
    print(n*7)
#Multiplication table for 7 up to 10. 7*1, 7*2, 7*3 and so forth.
#start at 1, end at 11 since its counting, this way it ends after 10.
#n*7 makes n multiply 7 by the amount of loops
#10 loops = 10 times
    
for n in range(1,11):
    print(n,"* 7 =",n*7)
    #added another n at the beginning to show the looping number
    #then added text to say * 7 = just to show the equation
    #this now prints 1 * 7 = and the result, all the way up to 10



Number=int(input("Vilket är ditt nummer?"))
                
for n in range(1,11):
    print(Number,"*", n ,"=",n*Number)
#Now we instead have the user input the desired number to show that numbers multiplication table
    for a in range(1,11):
        print("Table",a)
    for b in range(1,11):
        print(a*b)
#prints the table number in between the two "for" arguments as the table number is the first for.
for n in range(1,11):
    print(n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10)
#makes a big table, quite messy? Better way to format it insteaed of 10 separate calculations
    
    age=input("är patienten ett barn? Y/N")
if age.lower()=="y": 
    print("Patienten är ett barn och ska ta 500 mg per dag")
else: 
    print("Patienten vuxen och ska ta 750 mg per dag")
    #If age = y/Y(upper or lowercase does not matter cause of .lower()), it will print 500mg
    #if its not a y it will print 750 mg.
    
    age=input("är patienten ett barn? Y/N")
if age.lower()=="y": 
    print("Patienten är ett barn och ska ta 500 mg per dag")
else: 
    print("Patienten vuxen och ska ta 750 mg per dag")
    #If age = y/Y(upper or lowercase does not matter cause of .lower()), it will print 500mg
    #if its not a y it will print 750 mg.


    age=input("är patienten ett barn? Y/N")
if age.lower()=="y": 
    print("Patienten är ett barn och ska ta 500 mg per dag")
elif age.lower()=="n":
    print("Patienten är vuxen och ska ta 750m per dag")
else: 
    print("Bad input")
    #If age = y/Y(upper or lowercase does not matter cause of .lower()), it will print 500mg
    #if age = n/N(upper or lowercase does not matter cause of .lower()), it will print 750mg
    #if none of the above are inputted it will print "bad input"
    #instead of putting lower after each if you can put it at the start when you define age
    #So you can do age=input("är patienten ett barn? Y/N").lower and then have the answers in the ifs 
    #(if age=="y") <----- these be in lowercase and it will still work
    #like below
age=input("är patienten ett barn? Y/N").lower()
if age=="y": 
    print("Patienten är ett barn och ska ta 500 mg per dag")
elif age=="n":
    print("Patienten är vuxen och ska ta 750m per dag")
else: 
    print("Bad input")

    #Asks for patients weight and then comparares the input to what meds it should give
vikt = float(input("Hur mycket KG väger patienten?"))
if vikt < 20:
    #If the weight is lower than 20
    print("Patienten ska ges 500mg per dag.")
elif 20 <= vikt <= 40:
    #if the weight is above or equal to 20 but lower than 40
    print("Patienten ska ges 750mg per dag.")
elif 41 <= vikt <= 60:
    #if the weight is above or equal to 41 but lower than 60
    print("Patienten ska ges 1000 mg per dag.")
else:
    #if none of the above applies, print
    print("Patienten ska ges 1500mg per dag.")
    #Order is important, always if followed by elif elif elif then else.
    #if this happens, else if this happens, else if this happens, if all these dont work? Then else do this
