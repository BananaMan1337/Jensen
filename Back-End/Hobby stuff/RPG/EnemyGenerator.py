import random
#from RPG import Player.Health, PlayerLevel, Experience

class Enemy:
    def __init__(self, EnemyRace, EnemyClass, EnemyLevel, EnemyHealth):
        self.EnemyRace = EnemyRace
        self.EnemyClass = EnemyClass
        self.EnemyLevel = EnemyLevel
        self.EnemyHealth = EnemyHealth
    def EnemyAttack(self):
        if self.EnemyClass == "Warrior":
            print(f"The enemy {self.EnemyRace} swings its axe.")
            Damage = 5 + self.EnemyLevel
            Player.Health = Player.Health - Damage
            print(f"You take {Damage} damage.")
            return f"You have {Player.Health} HP Remaining"
        elif self.EnemyClass == "Rogue":
            print(f"The enemy {self.EnemyRace} shoots its bow")
            Damage = 5 + self.EnemyLevel
            Player.Health = Player.Health - Damage
            print(f"You take {Damage} damage.")
            return f"You have {Player.Health} HP Remaining"
        elif self.EnemyClass == "Mage":
            print(f"The enemy {self.EnemyRace} casts fireball")
            Damage = 5 + self.EnemyLevel
            Player.Health = Player.Health - Damage
            print(f"You take {Damage} fire damage.")
            return f"You have {Player.Health} HP Remaining"
    def Inspect(self):
        return f"{self.EnemyRace} {self.EnemyClass} at level {self.EnemyLevel} with {self.EnemyHealth} HP"

def Generate():
    global PlayerLevel
    Race = ['Goblin', 'Human', 'Elf', 'Ogre', 'Bandit']
    Class = ['Warrior', 'Rogue', 'Mage']
    Level = PlayerLevel + random.randint(0, 3)
    MobHealth = 30 + Level
    Enemy1 = Enemy(random.choice(Race), random.choice(Class), Level, MobHealth)
    return Enemy1
