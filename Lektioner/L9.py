def minBeräkning (tal1, tal2):
    svar = tal1 * tal2 + tal1
    return svar
#Here we make a function, easiest way for me to think about this is like using it to calculate a players currency
#and to subtract for a purchase etc
#Example being like tal1 = their wallet, tal2 = their purchase amount and to subtract tal2 from tal1
#This way you can make several different items with different costs easily able to subtract from the main number.

print(minBeräkning(4,5))
print(minBeräkning(8,9))
#function in usage, 4,5 and 8,9 is tal1 and tal2 in this case, it automatically assigns what you type into the function for usage
print(minBeräkning(100,350))


#exercise1
def plusfunction (tal1, tal2):
    svar = tal1 + tal2
    return svar

print(plusfunction(2,3))

#exercise2
def TriangleArea (bas, höjd):
    svar = bas * höjd / 2
    return svar

print(TriangleArea(5,7))
#this function calculates the area of a triangle

