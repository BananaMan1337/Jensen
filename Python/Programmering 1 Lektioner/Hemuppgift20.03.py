#svar=float(input("Vad är produkten av 12 och 13?"))
#if svar == 156:
#    print("Rätt.")
#else:
# print("Fel.")
#https://docs.google.com/document/d/1f8XPT5YAXksC3Cuv309kl2wubnEIXBRnJ0jzz6nNf98/edit

while True:
    betyg=int(input("Skriv in dina poäng i ämnet"))
    if 0<= betyg <= 49:
        print("Ej godkänt")
    elif 50<= betyg <=59:
        print("Ditt betyg är: E")
    elif 60<= betyg <=69:
        print("Ditt betyg är: D")
    elif 70<= betyg <=79:
        print("Ditt betyg är: C")
    elif 80<= betyg <=89:
        print("Ditt betyg är: B")
    elif 90<= betyg <=100:
        print("Ditt betyg är: A")
    else:
        print("Du skrev fel, gör igen")
        continue


