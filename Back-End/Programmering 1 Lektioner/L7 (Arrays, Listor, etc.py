#Skriv ett programm för att hitta en lösning till ekvationen (använd for-sats):
#4x -2 = 38
for x in range(1,40):
  if 4*x - 2 ==38:
    print("x är",x)


#Skriv ett programm för att hitta en lösning till ekvationen (använd While-sats):
#4y -2 = 38
y = 0
while 4*y-2!=38:
    y=y+1
print("y = ",y)

# En lista används för att lagra flera värden i en enda variabel:
cars = ["Ford", "Volvo", "BMW"]
print(cars)
['Ford', 'Volvo', 'BMW']

 # Du refererar till lista element genom att hänvisa till indexnumret.
cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
#printar ford

# Använd len() metoden för att returnera antalet av element i en lista.
cars = ["Ford", "Volvo", "BMW"]
print(len(cars))
#printar 3 för det är 3st element


# Du kan använda en for-loop för att gå igenom alla element i en lista.
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
#printar ut alla element
    
# Du kan använda metoden append () för att lägga till ett element i en lista.
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
#lägger till honda i listan på slutet (4)

# Metoden insert() lägger till ett element i en plats som du väljer. Du anger 2 värden. Första inmatningen
#är elementets index, och andra inmatningen är elements värde.
cars = ["Ford", "Volvo", "BMW"]
cars.insert(1,"Volkswagen")
# ”Volkswagen” infogas vid index 1 (andra plats). Alla element som kommer senare flyttas ett steg till höger.
print(cars)


# Du kan använda pop () metoden för att ta bort ett element från en lista.
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1) # I pop() metoden anges indexnumret.
print(cars)
#Detta tar bort volvo då ford=0, volvo = 1, bmw = 2

# Du kan också använda metoden remove () för att ta bort ett element från en lista.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo") # I remove() metoden anges elementets värde.
print(cars)

# Att ändra ett element i en lista
cars = ["Ford", "Volvo", "BMW", "Volkswagen"]
cars[0] = "Mercedes"
cars[3] = "Toyota"
print(cars)

# Metoden clear () tar bort alla element från en lista.
cars = ["Ford", "Volvo", "BMW"]
cars.clear()
print(cars)


#Skapa följande lista: städer = [“Stockholm”,“Sundsvall”,“Göteborg”]
#Skriv kod som:
#1. Lägger till elementet ”Motala” i slutet av listan.
#2. Lägger till elementet ”Västerås” i platsen med index ”2”.
#3. Tar bort elementet med index 0. Använd en lämplig metod.
#4. Tar bort elementet ”Motala”.
#5. Ändra elementet ”Västerås” med ”Eskilstuna”.
#6. Tar bort alla element i lisan.
#OBS! Skriv ”print(städer)” efter varje punkt.
städer = ["Stockholm","Sundsvall","Göteborg"]
print(städer)
städer.append("Motala")
print(städer)
städer.insert(2,"Västerås")
print(städer)
städer.pop(0)
print(städer)
städer.remove("Motala")
print(städer)
städer[1] = "Eskilstuna"
print(städer)
städer.clear()
print(städer)


#Skriv ett program för att ta reda om elementet Apple finns i listan eller inte.
fruits = ["orange", "Apple", "Banana"]
if "apple" in fruits:
   print("Apple exists")
else:   
   print("Apple does not exist")


#1. Printar (skriva ut) antalet element i listan. Använd en lämplig metod.
#2. Lägger till elementet ”programmering” i slutet av listan.
#3. Lägger till elementet ”natverksteknologier” i platsen med index ”1”.
#4. Tar bort elementet med index 2. Använd en lämplig metod.
#5. Tar bort elementet ”matte” från listan.
#6. Printar alla element i listan. Varje element ska hamna på en egen rad.
#Använd en for loop.
#7. Tar bort alla element i lisan.

ämnen = ["matte","datorteknik","nätverksteknik"]
print(len(ämnen))
ämnen.append("programmering")
print(ämnen)
ämnen.insert(1,"nätverksteknologier")
print(ämnen)
ämnen.pop(2)
print(ämnen)
ämnen.remove("matte")
print(ämnen)
for x in ämnen:
    print(x)
ämnen.clear()
print(ämnen)



#Skriv ett program som låter användaren gissa ett heltal mellan 1 och 100
#(Anvävd en while-slinga).
while True:
    nummer = int(input("Vilket nummer tänker jag på mellan 1-100?"))
    if nummer != 37:
        print("Fel!")
        continue
    if nummer == 37:
        print("Rätt, grattis!")
        break