#since its an int this time and not a string it will actually print 5*inputted number

fee= 358.3
#Specify price per hour
namn=input("Hej! Välkommen till BananaFitness, vad är ditt namn?")
#grabs name
hours=float(input("Hur många timmar i veckan tänkte du att träna med oss?"))
#grabs hours per week, float in case half hours
print("Vad kul", namn+"!", "För att träna", hours, "timmar i veckan så skulle det kosta", hours*fee,"kr per vecka")
#prints some nice words while saying their name, amount of hours and cost per week by doing hours * fee