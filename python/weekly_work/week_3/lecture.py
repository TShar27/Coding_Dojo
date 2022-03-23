goku = {'name': 'Goku', 'universe': 'Dragonball Z', 'health': 100, 'power': 30, 'defense': 10}
ironman = {'name': 'Tony Stark', 'universe': 'Marvel', 'health': 120, 'power': 30, 'defense': 20}
captain_america = {'name': 'Steve', 'universe': 'Marvel', 'health': 150, 'power': 20, 'defense': 30}

class Character:
    def __init__(self):
        self.name = "Goku"
        self.universe = "Dragonball Z"
        self.health = 150
        self.power = 30
        self.defense = 10
#Manual way of inputting data - no good ^

class Character:
    all_chars = []
    def __init__(self, name, universe, health, power, defense, sidekick = "None"):
         self.name = name
         self.universe = universe
         self.health = health
         self.power = power
         self.defense = defense
         self.sidekick = sidekick
         Character.all_chars.append(self)
    
    def change_health(self,health):
        self.health = health
        return self
    
    def change_power(self,power):
        self.power = power
        return self

    def change_defense(self,defense):
        self.defense = defense
        return self

    def change_name(self,name):
        self.name = name
        return self
    
    def print_character(self):
        print(f"name = {self.name}, universe = {self.universe} health = {self.health}, power = {self.power}, defense = {self.defense}")

#  A function inside of a class is called a method ^

goku = Character("Goku", "Dragonball Z", 150, 30, 10)
print(goku.health)

goku.change_health(120)
print(goku.health)

goku.change_name("Vegeta")
print(goku.name)



# OOP Abstraction


class Player:
    def __init__(self,name):
        self.name = name
        self.character = None
    
    def pick_character(self,character):
        self.character = character

    def punch(self,player2):
        if player2.character == None:
            print(f"{player2.name} has not selected a character yet")
            return self
        player2.character.health -= self.character.power
        print(f"{self.character.name} punched {player2.character.name} for {self.character.power} damage {player2.character.name } has {player2.character.health} health left")
        if (self.character.health <= 0):
            print(f"{player2.name} won the game")
        elif(player2.character.health <= 0):
            print(f"{self.name} won the game")
        return self 

    def special(self,player2):
        player2.character.health -=self.character.power + 20
        self.character.health -= 20
        print(f"{self.character.name} used special on {player2.character.name} for {self.character.power + 20} damage {player2.character.name } has {player2.character.health} health left")
        if (self.character.health <= 0):
            print(f"{player2.name} won the game")
        elif(player2.character.health <= 0):
            print(f"{self.name} won the game")
        return self 
        


class Character:
    all_chars = []
    def __init__(self, name, universe, health, power, defense, sidekick = "None"):
         self.name = name
         self.universe = universe
         self.health = health
         self.power = power
         self.defense = defense
         self.sidekick = sidekick
         Character.all_chars.append(self)
    
    def change_health(self,health):
        self.health = health
        return self
    
    def change_power(self,power):
        self.power = power
        return self

    def change_defense(self,defense):
        self.defense = defense
        return self

    def change_name(self,name):
        self.name = name
        return self
    
    def print_character(self):
        print(f"name = {self.name}, universe = {self.universe} health = {self.health}, power = {self.power}, defense = {self.defense}")

# using all_chars[] in class 
# cls refers to class we are using
    @classmethod
    def print_all_chars(cls):
        for char in cls.all_chars:
            char.print_character()


# different way to obtain values
goku = Character("Goku","DragonBall Z",150,30,10)
new_ironman = Character(ironman['name'],ironman['universe'],ironman['health'],ironman['power'],ironman['defense'])
# print(new_ironman.sidekick)

captain_america = Character(power = 20,health = 150, defense = 30, name = "Steve",universe = "Marvel", sidekick = "Wing")
# print(captain_america.sidekick)

# #Chaining
# captain_america.change_defense(20).change_health(30).change_name("Joey")
# Character.print_all_chars()
timmy = Player("timmy")
tony = Player("tony")
timmy.pick_character(goku)
tony.pick_character(new_ironman)

# print(timmy.character.name)
# print(tony.character.name)

tony.punch(timmy)
timmy.special(tony).special(tony).special(tony)