# Med ”break” kan vi stoppa slingan innan den har gått igenom alla element.
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# Med "continue" kan vi stoppa den aktuella iterationen av slingan och fortsätta med nästa.
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



#- Skriv ett program som skriver ut den följande texten.
#Du måste ha två listor, en för varje kolonn, samt använda dig av for-slingor. 
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry

description={"red","big","tasty"}
fruit={"apple","banana","cherry"}
for x in description:
    for y in fruit:
        print(x,y)
    
#Ta reda på om heltalet 1 finns i listan ”numbers” eller inte.
numbers=[1,2,3,4]
if 1 in numbers:
    print("Number 1 exists")
else:
    print("1 does not exist")

#Med hjälp av "continue" skriv ett program som går igenom listan och skriver ut alla användare (Users) i listan utom "User3".
usernames =["user1","user2","user3","user4","user5"]
for x in usernames:
    if x =="user3":
        continue
    print(x)

#- Skriv ett program som tar reda på om ”user1” finns med i listan ”users”. Om elementet ligger i listan tar programmet bort ”user1” från listan. 
users = ["user1", "user2", "user3", "user4", "user5"]
if "user1" in users:
    users.remove("user1")
    print("User1 removed")
else:
    print("User 1 does not exist")

#Du kan komma åt en del av en lista genom att använda
#operatorn : när du anger en listas index.
    #lista[i:] gör en dellista som och har med alla element
#fr.o.m. index i till slutet av listan.
    
#Enklare sagt, du kan ta en del av listorna. Till exempel om du ska printa en lista men du vill börja från tredje slotten så kan du skriva 
lista = [1, 4, 9, 16, 25, 90]
print(lista[3:])
#Detta printar då efter 9, så den printar 16,25,90

#lista[:j] gör en dellista som har med alla element från början av listan till index j. Elementet med index j inkluderas inte.



#Enklare sagt, sätt : innan slotten istället för efter så skriver den det i listan som är innan slotten.
lista = [1, 4, 9, 16, 25, 90]
print(lista[:3])
#Detta printar alltså allt innan fjärde slotten, så 1,4,9.


#lista[i:j] gör en dellista som har med alla element fr.o.m. index i till index j. Elementet med index j inkluderas inte.

#Enklare sagt, detta skriver allt mellan i och j. Så om du skriver 2:4 som exempelt under
lista = [1, 4, 9, 16, 25, 90]
print(lista[2:4])
#Så skriver den ut det imellan andra och fjärde slotten.
#alltså 9 och 16


land = "Sverige"
print(land[:2])
#printar innan 2 så SV
print(land[3:6])
#printar mellan 3:6 så rig, ej med e
print(land[5:])
#printar allt efter 5 så ge
#förstår ej varför exempelt ej har med e, det stavar ju ej sverige.
#but 3:6 till 2:6 för att få sverige


#- Funktionerna min () och max () kan användas för att hitta det lägsta eller högsta värdet i en lista:
numbers = [1,2,3,4,5]
print(min(numbers))
print(max(numbers))
#Printar 1 och 5

#Funktionen sum () summerar alla element i listan. Alla element måste vara tal om denna funktion ska användas.
numbers = [1,2,3,4,5,6]
print(sum(numbers))
#plussar ihop alla nummer tillsammans


#Funktionen ”pow” (power) används för potensberäkningar. I exemplet nedanretuneras värdet 2 upphöjt till 4 (samma som 2 * 2 * 2 * 2)
x = pow(2, 4)
x = pow(2, 4)
print(x)
#upphöjt


#- För att ta en kopia av en lista och spara det i ett annat namn skriver vi:
numbers = [1,2,3,4,5]
jensen = numbers[:]
print(numbers)
print(jensen)
#Listan ”jensen” är alltså en kopia av listan ”numbers”.


#Vi har denna lista:
#num = [1,5,-29,86,7,-8]
#Skriv ett program som:
#1. Hittar det lägsta värdet i listan.
#2. Hittar det högsta värdet i listan.
#3. Summerar alla element i listan.
#4. Kopierar listan och sparar det i listan "Stockholm".
num = [1,5,-29,86,7,-8]
print(min(num))
print(max(num))
print(sum(num))
stockholm = num[:]
print(stockholm)

#Python har också en inbyggd modul som kallas för "math", som utökar listan över matematiska funktioner.
#För att kunna använda den måste man importera matematikmodulen "math":
#Metoden math.sqrt () returnerar till exempel kvadratroten av ett tal:
import math
x = math.sqrt(64)
print(x) 



#Math.pi-konstanten returnerar värdet på PI (3.14 ...):
import math
x = math.pi
print(x)

#Vi använder pi för att exempelvis beräkna cirkelns area.

#Skriv ett program för att beräkna arean för en cirkel med radie 4 cm.
import math
x = math.pi * pow(4,2)
print(x)
#area för cirkel är formula
#area = pi * radius^2


#Utveckla programmet så att användaren kan ange radiens värde.
import math
x = float(input("Vad är radius?"))
area = math.pi * pow(x,2)
print(area)


#Skriv ett program som ber användaren att skriva ett
#heltal. Om talet är större än 20, skrivs kvadratroten av
#talet ut. Annars, skrivs kvadraten av talet ut, d.v.s
#talet upphöjt till 2. Lägg programmet i en lämplig loop.

import math
while True:
    tal = int(input("Skriv ett heltal"))
    if tal>20:
        print("square root",math.sqrt(tal))
    else: 
        print("number ^2 =",math.pow(tal,2))

