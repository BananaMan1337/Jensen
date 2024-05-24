import random
#from RPG import Health, PlayerLevel, Experience
Health = 100
PlayerLevel = 1

class Enemy:
    def __init__(self, EnemyRace, EnemyClass, EnemyLevel, EnemyHealth):
        self.EnemyRace = EnemyRace
        self.EnemyClass = EnemyClass
        self.EnemyLevel = EnemyLevel
        self.EnemyHealth = EnemyHealth
    def EnemyAttack(self):
        global Health
        if self.EnemyClass == "Warrior":
            print(f"The enemy {self.EnemyRace} swings its axe.")
            Damage = 5 + self.EnemyLevel
            Health = Health - Damage
            print(f"You take {Damage} damage.")
            return f"You have {Health} HP Remaining"
        elif self.EnemyClass == "Rogue":
            print(f"The enemy {self.EnemyRace} shoots its bow")
            Damage = 5 + self.EnemyLevel
            Health = Health - Damage
            print(f"You take {Damage} damage.")
            return f"You have {Health} HP Remaining"
        elif self.EnemyClass == "Mage":
            print(f"The enemy {self.EnemyRace} casts fireball")
            Damage = 5 + self.EnemyLevel
            Health = Health - Damage
            print(f"You take {Damage} fire damage.")
            return f"You have {Health} HP Remaining"
    def Inspect(self):
        return f"{self.EnemyRace} {self.EnemyClass} at level {self.EnemyLevel} with {self.EnemyHealth} HP"

def Generate():
    Race = ['Goblin', 'Human', 'Elf', 'Ogre', 'Bandit']
    Class = ['Warrior', 'Rogue', 'Mage']
    Level = PlayerLevel + random.randint(0, 3)
    MobHealth = 30 + Level
    Enemy1 = Enemy(random.choice(Race), random.choice(Class), Level, MobHealth)
    return Enemy1


Enemy1= Generate()
print(Enemy1.Inspect())
print(Enemy1.EnemyAttack())
