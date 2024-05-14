class Book:
    def __init__(self, title, author, year):
        #(self always first, attribute, attribute)
        self.title = title
        self.author = author
        self.year = year
    
    def describe(self):
        return f"{self.title} by {self.author}, published in {self.year}"
#Self needs to be written first in everything
#regarding classes for it to know its in the
#class    


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Greeting(self):
        return f"Hello! My name is {self.name} and im {self.age} years old."

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def Introduction(self):
        return f"Hello! My name is {self.name} and im in grade {self.year}"

class Car:
    def __init__(self, Brand, Model, Year, Speed):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year
        self.Speed = Speed
    def drive(self, value):
        print(f"The {self.Model} is at {self.Speed} km/h, you accelerate")
        self.Speed = self.Speed + value
        print(f"You are now driving at {self.Speed}")
        self.Speed = self.Speed + value 
        print(f"You are now driving at {self.Speed}")
        self.Speed = self.Speed + value     
        return f"The car has reached max speed at {self.Speed}, pretty good for a car from {self.Year}" 
    def stop(self, value):
        self.Speed = value
        return f"The {self.Model} has stopped, its now at {self.Speed}"