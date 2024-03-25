x = 1
while x < 15:
    print(x)
    x = x + 2
#While x is less than 15 it will print x along with doing x + 2, this way it will print every odd number between 1 and 15
    
x = 2
while x < 200:
    print(x)
    x = x + 2
#while x is less than 200 it will print x along with doing x + 2, this way it will print every even number between 1 and 200




#Skriv tre program som skriver ut de positiva jämna heltalen: (Använd While sats)
#a) mindre än eller lika med 200
#b) större än eller lika med 20 men mindre än eller lika med 40
#c) utan att sluta 
x=2
while x <= 200:
    print(x)
    x = x + 2

x=20
while x <= 40:
    print(x)
    x = x+2

x=2
while True:
    print(x)
    x = x+2




#Skriv ett program för att hitta en lösning till ekvationen (använd for- sats): 2y +4 = 14
for y in range(1,100):
    if 2 * y + 4 ==14:
        print("y=",y)


while True:
    n=int(input("Vad är ditt nummer?"))
    summan = 0
    counter = 1
    while counter <= n:
        summan = summan + counter
        counter = counter + 1
    print("The sum is:", summan)
    #Förstår ej riktigt vad detta gör.