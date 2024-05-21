#Inheritance

#Inheritance lets us define a class that inherits all methods and properties of another class
#parent or base class -> child or sub class


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#Normal class that will become parent

class Student(Person):
    pass
#Pass is used if you dont want to add any properties or methods to the class. This will now be the same as Person which is our parent

z = Student("Sam","Khan")
z.printname()



# super() function
#Super() makes it so that the child inherits all the properties from the parent


class Person:
# Konstruktor för Person-klassen, tar förnamn och efternamn som argument.
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  # Metod för att skriva ut personens fullständiga namn.
  def printname(self):
    print(self.firstname, self.lastname)
    
 # Definierar subklassen Student som ärver från Person.
class Student(Person):
# Konstruktor för Student-klassen, tar förnamn och efternamn som argument.
   def __init__(self, fname, lname):
    super().__init__(fname, lname) # Anropar basklassens konstruktor för att initiera firstname och lastname. 
x = Student("Mike", "Olsen")
x.printname()




import turtle
var = turtle.Turtle()
for _ in range(4):
    var.forward(100)
    var.right(90)

turtle.done()
#This draws a square

import turtle
var = turtle.Turtle()
# Rita en cirkel
var.circle(100)  # Rita en cirkel med radien 100
# Avsluta ritningen
turtle.done()
#circle

import turtle
var = turtle.Turtle()

# Rita en blomma
for _ in range(36):
    var.circle(50)    # Rita en cirkel med radien 50
    var.right(10)     # Sväng höger 10 grader

# Avsluta ritningen
turtle.done()
#flower
