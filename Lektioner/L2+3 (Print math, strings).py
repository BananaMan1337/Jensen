print(7**2)
#7 to the power of 2
print(7//2)
#7 divided by 2 but whole numbers, no decimals
print(49**0.5)
#0.5 = square root so this is the square root of 49
print(2**2)
#2 to the power of 2
print(2**4)
#2 to the power of 4
print(2**6)
#2 to the power of 6

print(9/2, "och", 9//2)
# 9 divided by 2 and 9 divided by 2 but whole numbers
print(11/6, "och", 11//6)
#11 divided by 6 and 11 divided by 6 but whole numbers
print(21/8, "och", 21//8)
#21 divided by 8 and 21 divided by 8 but whole numbers



print("En rektangel har bredden 3 cm och längden 4cm.")
#beskrivning
print("Omkretsen är", (3+4)*2, "centimeter")
# 3+4 = short and long side added * 2 cause it has 4 sides
print("Arean är", 3*4, "kvadratcentimeter")
#3*4 = long side and short side multiplied to get area

b=3
#Width is now a variable so that its easily changeable
l=4
#Length is now a variable so its easily changeable
print("en rektangel har bredden",b, "och längden",l)
#same as above but with variable
print("omkretsen är", (b+l)*2,"centimeter")
#same as above but with variable
print("arean är",b*l,"kvadratcentimeter")
#same as above but with variable

b2=92
l2=230
print((b2+l2)*2,"cm omkrets")
print(b2*l2, "kvadrat cm")

tal1=25
tal2=60
print("produkten av", tal1, "och", tal2, "är", tal1*tal2)



B=float(input("Vad är bredden"))
#makes the person input what the width is
L=float(input("Vad är längden"))
#makes the person input what the length is
print("en rektangel har bredden",B, "och längden",L)
#Same as above but with user input numbers
print("omkretsen är", (B+L)*2,"centimeter")
#same as above but with user input numbers
print("arean är",B*L,"kvadratcentimeter")
#same as above but with user input numbers


multi1=float(input("nummer 1"))
#Specify first number to be multiplied
multi2=float(input("nummer 2"))
#Specify second number to be multiplied
print("produkten är",multi1*multi2)
#result



Tribas=5
#triangle base
Trihöjd=10
#triangle height
print((Tribas*Trihöjd)/2, "arean av triangeln")
#Calculate area of triangle means base * height / 2

base=float(input("What is the base"))
#Specify triangle base
height=float(input("what is the height"))
#specify triange height
print((base*height)/2,"arean av triangeln")
#Triangle height * base /2 to get area
