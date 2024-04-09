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


#exercise3
import math
def CircleArea (radius):
    svar = math.pi * pow(radius,2)
    return svar


print(CircleArea(3))
#same as triangle but using import math and math.pi to calculate the area of a circle
#exercise4
def LargestNumber (tal1,tal2,tal3):
    svar = max(tal1,tal2,tal3)
    return svar

print(LargestNumber(3,55,-5))


def LargestNumber (tal1,tal2,tal3):
    return max(tal1,tal2,tal3)

print(LargestNumber(3,55,-5))
#behöver ej svar här
#exercise 5
def my_function(food):
    for x in food:
        print(x)
    return x

my_function("jensen")
#text lists every letter in the word since its for x

#exercise6
def my_function(food):
    for x in food:
        print(x)
    return x

my_function(["Apple","banana","cherry"])
#in this case, food is defined as a list and so it will list the different fruits in the list


#exercise7
def my_function(list1):
    return max(list1, key=len)
print(my_function(["bok","linjal"]))


#or
 
def my_function(ord1,ord2):
    return max(ord1,ord2, key=len)
print(my_function("linjal","bok"))

#list or ord1, ord2
#We had not done key yet so the way they did it was
def my_functuin(ord1,ord2):
    if len(ord1) >= len(ord2):
        return ord1
    else:
        return ord2
print(my_function("bok","linjal"))


#exercise 8
def my_function(list):
   result= sum(list) + 100
   return result

print(my_function([100,300,400,3]))


