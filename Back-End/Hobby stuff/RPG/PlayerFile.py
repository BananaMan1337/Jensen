
class PlayerGen:
    def __init__(self, Name, Age, PlayerLevel, Health, Experience, Strength, Intellect, Agility, Charisma):
        self.Name = Name
        self.Age = Age
        self.PlayerLevel = PlayerLevel
        self.Health = Health
        self.Experience = Experience
        self.Strength = Strength
        self.Intellect = Intellect
        self.Agility = Agility
        self.Charisma = Charisma
    def PlayerAttack(self):
        from EnemyGenerator import Enemy1
        print(f"You attack the enemy {Enemy1.EnemyRace}")
        Damage = self.Strength + self.PlayerLevel
        Enemy1.EnemyHealth = Enemy1.EnemyHealth - Damage
        print(f"You deal {Damage} damage to the enemy {Enemy1.EnemyRace}")
    def InspectPlayer(self):
        return print(f"Name: {self.Name}\nAge: {self.Age}\nLevel: {self.PlayerLevel}\nHealth: {self.Health} HP")
    def PlayerBattle(self):
        from BattleSequence import Battle
        global Player
        Battle()
   
def PlayerGenerate():
    try:
        Name = input("What is your name?")
        Age = int(input("How old are you?"))
        Strength = int(input("On a scale of 1-10 how strong are you?"))
        Intellect = int(input("On a scale of 1-10 how smart are you?"))
        Agility = int(input("On a scale of 1-10 how agile are you?"))
        Charisma = int(input("On a scale of 1-10 how good are you with people?"))
        PlayerLevel = 1
        Health = 50
        Experience = 0
        Player = PlayerGen(Name, Age, PlayerLevel, Health, Experience, Strength, Intellect, Agility, Charisma)
        return Player
    except ValueError:
        print("Please enter only numbers and without decimals.")
        PlayerGenerate()
  