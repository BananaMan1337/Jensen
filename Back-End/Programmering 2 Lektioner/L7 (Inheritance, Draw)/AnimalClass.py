

class Animal:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    
    def Eat(self):
        print(f"{self.Name} is eating.")
    def Sleep(self):
        print(f"{self.Name} is sleeping.")
    def Wash(self):
        print(f"{self.Name} is washing itself.")
    def Sound(self):
        print(f"{self.Name} is making sounds.")

class Cat(Animal):
    def __init__(self, Name, Age, Breed):
        super().__init__(Name, Age)
        #inherits name and age from parent
        self.Breed = Breed
    def Meow(self):
        print(f"{self.Name} is meowing.")
    def Sound(self):
        self.Meow()
    #This replaces Sound with Meow
