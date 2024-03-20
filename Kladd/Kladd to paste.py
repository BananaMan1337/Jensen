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
