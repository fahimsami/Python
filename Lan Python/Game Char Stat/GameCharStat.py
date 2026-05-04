class GameCharacter:
    def __init__(self, name, health=100, mana=50, level=1):
        self._name = name
        self._health = health
        self._mana = mana
        self._level = level
        
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
   
        self._health = value
        
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            value = 0
        elif value > 50:
            value = 50

        self._mana = value
    
    @property
    def level(self):
        return self._level
    def level_up(self):
       
       self._level += 1
       print(f"{self._name} leveled up to level {self._level}") 
       self.mana += 50
       self.health += 100
        
    
    def __str__(self):
        return f"Name : {self._name}\n Level : {self._level}\n Health : {self._health}\n Mana : {self._mana}\n"  
    
hero = GameCharacter("Kratos") 
print(hero) 

hero._health -= 10
hero._mana -= 30
print(hero)

hero.level_up()
hero.health -= 20
print(hero)
hero.level_up()
print(hero)

