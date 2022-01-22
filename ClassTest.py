import random
import time

hero_names = ["Jack", "Lana", "Peter", "Mary", "Robert"]
hero_types = ["Pirate", "Archer", "Berserk"]
enemy_names = ["Босоножко", "Обидулька", "Подсранко", "Золупышка", "Лопоушко"]

class Creature:
    species = "Human"
    bio = "Anyone can be a human or the other way around?"
    def __init__(self, name, attack, health, exp=0, lvl=1):
        self.name = name
        self.attack = attack
        self.health = health
        self.experience = exp
        self.level = lvl
    
    def __str__(self) -> str:
        return f"{self.name} emerged and has {self.attack} attack and {self.health} health"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Pirate(Creature):
    bio = "A thunder in the sea"
    def speak(self, sound="Ahoy!"):
        return super().speak(sound)

class Archer(Creature):
    bio = "Silent arrow"
    def speak(self, sound="Mmmm"):
        return super().speak(sound)

class Berserk(Creature):
    bio = "Biiiig swords..."
    def speak(self, sound="Roar!"):
        return super().speak(sound)

class Zombie(Creature):
    bio = "Braaainzzz..."
    def speak(self, sound="*growr*"):
        return super().speak(sound)


def recreate_characters():
    create_hero()
    create_enemy()


def create_hero():
    global hero
    hero_name = ""
    hero_pro = ""
    counter = 0
    while True: # not bool(hero_name) and not bool(hero_pro):
        # hero_name = input("Name your hero(leave blank for random name or 'q' to quit): ")
        # if hero_name == "q":
        #     return
        # hero_pro = input("What type of hero you want to call for? A Pirate, an Archer or maybe Berserk? (leave blank for random profession or 'q' to quit) ")
        # if hero_pro == "q":
        #     return
        if not bool(hero_name) and not bool(hero_pro):
            hero_name = hero_names[random.randint(0, len(hero_names) - 1)]
            hero_pro = hero_types[random.randint(0, len(hero_types) - 1)]
            break
        if hero_name and (hero_pro in hero_types):
            break
        counter += 1
        if counter > 2:
            print("Cmon already, name him and choose speciality...")
    if hero_pro == hero_types[0]:   
        hero = Pirate(hero_name, random.randint(2, 3), random.randint(20, 30))
    elif hero_pro == hero_types[1]:
        hero = Archer(hero_name, random.randint(3, 5), random.randint(15, 25))
    elif hero_pro == hero_types[2]:
        hero = Berserk(hero_name, random.randint(4, 5), random.randint(15, 20))
    show_stats(hero)
    return hero

def create_enemy():
    global enemy
    enemy_name = enemy_names[random.randint(0, len(enemy_names) - 1)]
    enemy = Zombie(enemy_name, random.randint(1,3), random.randint(10,20), random.randint(2,5))
    show_stats(enemy)

def show_stats(type="all"):
    if type == "all":
        print(hero)
        print(enemy)
    else:    
        print(type)

def attack():
    enemy_power = enemy.attack + random.randint(-1,1)
    hero.health -= enemy_power
    print(f"\n{enemy.name} stroke {hero.name} with {enemy_power} leaving {hero.name} with {hero.health} health")
    hero_power = hero.attack + random.randint(-1,1)
    enemy.health -= hero_power
    print(f"{hero.name} stroke {enemy.name} with {hero_power} leaving {enemy.name} with {enemy.health} health")
    if hero.health <= 0 and enemy.health <= 0:
        hero.speak()
        print("\nA draw...")
        hero.health = 0
        enemy.health = 0 
    if hero.health <= 0:
        hero.speak()
        print("\nYour hero died in fierce combat")
        hero.health = 0
    elif enemy.health <= 0:
        enemy.speak("")
        print(f"\nYour hero killed {enemy.name} and earned {enemy.experience} exp") 
        enemy.health = 0 

def auto_attack():
    kills = 0
    while True:
        attack()
        time.sleep(1)
        if hero.health == 0:
            print(f"{hero.name} level {hero.level} killed {kills} enemies before vanishing")
            return
        elif enemy.health == 0:
            kills += 1
            hero.health += 5
            hero.experience += enemy.experience
            create_enemy()
        if hero.experience >= 10*hero.level:
            hero.experience = hero.experience - 10*hero.level
            hero.level += 1
            print(f"{hero.name} in now level {hero.level}!")
            hero.attack += random.randint(1,2)
            hero.health += 10



def main():
    '''
Small dungeon crawler.
ch - create new hero
e - create new enemy
rc - recreate characters
s - print current stats of your hero and enemy
a - attack
h - help
q - quit
'''

    commands = {
        # "ch": create_hero,
        # "e": create_enemy,
        "rc": recreate_characters,
        "s": show_stats,
        "a": attack,
        "aa": auto_attack,
        "h": help
      }
    create_hero()
    create_enemy()
    auto_attack()

    while True:
        print("\nFor help type 'h'")
        command = ""
        while not bool(command):
            command = input("\nInput action: ")
        for key in commands:
            if command == key:
                if command == "h":
                    commands[command](main)
                    break
                # elif command == "m":
                #     commands[command]()        
                else:
                    commands[command]()
                    break
        if command == "q":
            print("\nQuiting...")
            break
        elif command not in commands:
            print("\nThere's no such command")
            continue
    del hero
    del enemy
        # print("\nReturning to menu...")

main()
