#region Maze spel
class Map():
    def __init__(self, x_max, y_max, treasure_x, treasure_y):
        self.x_max = x_max  # Maximal x-koordinat på kartan
        self.y_max = y_max  # Maximal y-koordinat på kartan
        self.treasure_x = treasure_x  # x-koordinat för skatten
        self.treasure_y = treasure_y  # y-koordinat för skatten

class Player():
    def __init__(self, name, map):
        self.name = name  # Spelarens namn
        self.x = 0  # Startposition x
        self.y = 0  # Startposition y
        self.map = map  # Referens till kartan
         
    def move_up(self):
        # Gå upp, om spelaren inte redan är höst upp
        if self.y < self.map.y_max:
            self.y += 1
        
    def move_down(self):
        # Gå ner, om spelaren inte redan är längst ner
        if self.y > 0:
            self.y -= 1
            
    def move_right(self):
        # Gå höger, om spelaren inte redan är längst till höger
        if self.x < self.map.x_max:
            self.x += 1
        
    def move_left(self):
        # Gå vänster, om spelaren inte redan är längst till vänster
        if self.x > 0:
            self.x -= 1
            
    def pick_treasure(self):
        # Kontrollera om spelaren har hittat skatten
        # Om spelarens x-koordinat är samma som skattens x-koordinat, och spelarens y-koordinat är samma som skattens y-koordinat 
        if self.x == self.map.treasure_x and self.y == self.map.treasure_y:
            print(self.name, "hittade skatten!")
        else:
            print(self.name, "kunde inte hitta skatten")
            
####################################################### # Outside Class
# Skapa en karta och två spelare utanför klassdefinitionerna
map_object = Map(5, 4, 2, 1) # (x_max, y_max, treasure_x, treasure_y)         
player_1 = Player('Isaak', map_object)
player_2 = Player('Maria', map_object)

# Flytta spelarna och skriv ut deras positioner
player_1.move_up()
player_2.move_up()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

player_1.move_up()
player_2.move_right()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

player_1.move_up()
player_2.move_right()
print(player_1.name, ":", player_1.x, ", ", player_1.y, ", ", player_2.name, ":", player_2.x, ", ",player_2.y)

# Låt spelarna försöka plocka upp skatten
player_1.pick_treasure()
player_2.pick_treasure()


class Maze(): # Definierar en klass för labyrinten
    def __init__(self, goal_x, goal_y, traps, treasures):
        self.goal_x = goal_x  # Målets X-koordinat
        self.goal_y = goal_y  # Målets Y-koordinat
        self.traps = traps  # Lista över koordinater för fällor
        self.treasures = treasures  # Lista över koordinater för skatter

class Player():  # Definierar en klass för spelaren
    def __init__(self, name, maze_parameter):
        self.name = name  # Spelarens namn
        self.x = 0  # Startposition X-koordinat
        self.y = 0  # Startposition Y-koordinat
        self.score = 0  # Startpoäng
        self.maze = maze_parameter

    def move(self, direction):
        # Flytta spelaren baserat på riktningen
        if direction == "up":
            self.y += 1  # Öka Y-koordinaten för att flytta uppåt
        elif direction == "down":
            self.y -= 1  # Minska Y-koordinaten för att flytta nedåt
        elif direction == "left":
            self.x -= 1  # Minska X-koordinaten för att flytta åt vänster
        elif direction == "right":
            self.x += 1  # Öka X-koordinaten för att flytta åt höger
        self.check_position()  # Kontrollera spelarens nya position

    def check_position(self):
        # Kontrollera om spelaren har träffat en skatt eller fälla
        if (self.x, self.y) in self.maze.treasures:
            self.score += 10  # Öka poängen
            self.maze.treasures.remove((self.x, self.y))  # Ta bort skatten från listan
            print(f"{self.name} found a treasure! Score: {self.score}")
        elif (self.x, self.y) in self.maze.traps:
            self.score -= 5  # Minska poängen för träffad fälla
            print(f"{self.name} hit a trap! Score: {self.score}")

        # Kontrollera om målet är nått
        if (self.x, self.y) == (self.maze.goal_x, self.maze.goal_y):
            print(f"{self.name} reached the goal! Final Score: {self.score}")


#######################################################
# Skapa en labyrint och en spelare utanför klassdefinitionerna
traps = [(2, 1), (1, 2)]  # Definiera FÄLLORNAS positioner (x,y),tupler 
treasures = [(1, 1), (2, 2)]  # Definiera skatternas positioner
maze_object = Maze(3, 3, traps, treasures)  # Skapa en labyrintinstans
player = Player("Pierre", maze_object)  # Skapa en spelarinstans

# Spellogik för att flytta spelaren
player.move("right")  # Spelaren rör sig åt höger
player.move("up")  # Spelaren rör sig uppåt
player.move("right")  # Spelaren rör sig åt höger igen
player.move("right")  # Spelaren rör sig åt höger ännu en gång
#endregion

#Encapsulation hides the details of classes and provides only whats necessary.
#Encapsulation works by defining the classes data attribute as private and giving methods known as getter and setters to integrate attributes.
#Getter gives access to attributes
#setter makes changing attributes possible

#Privating is done by a double underscore
#self.__car like so



class Car:
    def __init__(self, brand, model):
# Private attribut = parameter
        self.__brand = brand # Skyddat attribut för tillverkaren av bilen
        self.__model = model # Skyddat attribut för modellen av bilen


def get_brand(self):
# Getter method: Utanför klassen, kan användare läsa värdet av
#self._brand genom denna metod. Men de kan inte ändra dess värde.
    return self.__brand # Returnerar tillverkaren av bilen

def set_brand(self, brand):
    self.__brand = brand # Tillåter att tillverkarens namn ändras.

def get_model(self):
# Getter method: Utanför klassen, kan användare läsa värdet av
#self._model genom denna metod. Men de kan inte ändra dess värde.
    return self.__model # Returnerar modellen av bilen

def set_model(self, model):
# Setter method: Utanför klassen, kan användare ändra värdet av
#self._model genom denna metod.
    self.__model = model # Tillåter att modellens namn ändras



class Student:
    def __init__(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade
    def Details(self):
        return f"Name: {self.__name} Age: {self.__age} Grade: {self.__grade}"

Person1 = Student("Sam","23","A")
print(Person1.Details())
from Class import Bank






class Bank:
    def __init__(self, Account, Balance):
        self.__Account = Account
        self.__Balance = Balance
    def CheckBalance(self):
        return f"You have {self.__Balance} in account {self.__Account}"
    def Deposit(self):
        Cash = float(input("How much would you like to add?"))
        self.__Balance = self.__Balance + Cash
        return f"{Cash} added, you now have {self.__Balance} in account {self.__Account}"
    def Withdraw(self):
        try:
            Cash = float(input("How much would you like to withdraw?"))
            if self.__Balance > Cash:
                self.__Balance = self.__Balance - Cash
                return f"Withdrawal successful, you have {self.__Balance} left in your account"
            else: 
                return "Not enough balance in account"
        except ValueError:
            print("Bad input, only put in whole numbers")




account1 = Bank("Lönekonto37", 0)
print(account1.CheckBalance())
print(account1.Deposit())
print(account1.Withdraw())