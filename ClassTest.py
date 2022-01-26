
import random
import time

hero_names = ["Jack", "Lassia", "Peter", "Mary", "Robert", "Garry", "Kirill",
                "Yes, you!"]
hero_types = ["Pirate", "Archer", "Berserk"]
enemy_names = ["Босоножко", "Обидулька", "Подсранко", "Золупышка", "Лопоушко",
                "Рукожопко", "Ленивко", "Зеленушко", "Сопливко", "Мяско"]


class Wallet:
    bio = "Your best friend in this journey"

    def __init__(self, money, game_speed, global_exp=0, global_level=1, upgrade_count=1, speed_count=1, best_kills=0):
        self.money = money
        self.attack_speed = game_speed
        self.global_exp = global_exp
        self.global_level = global_level
        self.upgrades_count = upgrade_count
        self.speed_count = speed_count
        self.best_kills = best_kills

    def __str__(self) -> str:
        return f"You have ${self.money} and {1 / self.attack_speed:.2f} game speed increase, \n \
Global level - {pocket.global_level}, EXP - {pocket.global_exp}/{5**pocket.global_level}"


class Creature:
    species = "Human"
    bio = "Anyone can be a human or the other way around?"

    def __init__(self, name, attack, max_health, health=1, money=0, exp=0, lvl=1, attack_speed=1):
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = max_health
        self.experience = exp
        self.level = lvl
        self.money = money
        self.attack_speed = attack_speed

    def __str__(self) -> str:
        return f"{self.name} level {self.level} emerged and has {self.attack} attack and {self.health} health"

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


def console_clr():
    print("\n"*50)


def rand_i(a, b):
    return random.randint(a, b)


def rand_r(a, b):
    return random.randrange(a, b)


def recreate_characters():
    pocket.upgrades_count = 1
    create_hero()
    create_enemy(0)


def create_wallet():
    global pocket
    loaded = []
    with open("autosave.txt", "r") as load:
        loaded = load.readlines()
    if bool(loaded):
        pocket = Wallet(int(loaded[0]),
                        float(loaded[1]),
                        int(loaded[2]),
                        int(loaded[3]),
                        int(loaded[4]),
                        int(loaded[5]),
                        int(loaded[6])
                        )
    else:
        pocket = Wallet(0, 1)
    create_hero(int(loaded[7]))
    return pocket


def create_hero(level=1):
    global hero
    hero_name = ""
    hero_pro = ""
    counter = 0
    while True:  # not bool(hero_name) and not bool(hero_pro):
        # hero_name = input("Name your hero(leave blank for random name or 'q' to quit): ")
        # if hero_name == "q":
        #     return
        # hero_pro = input("What type of hero you want to call for? A Pirate, an Archer or maybe Berserk? \n \
        # (leave blank for random profession or 'q' to quit) ")
        # if hero_pro == "q":
        #     return
        if not bool(hero_name) and not bool(hero_pro):
            hero_name = hero_names[rand_i(0, len(hero_names) - 1)]
            hero_pro = hero_types[rand_i(0, len(hero_types) - 1)]
            break
        if hero_name and (hero_pro in hero_types):
            break
        counter += 1
        if counter > 2:
            print("Cmon already, name him and choose speciality...")
    if hero_pro == hero_types[0]:
        hero = Pirate(hero_name, 
                    rand_i(2 + pocket.global_level, 3 + pocket.global_level) + pocket.upgrades_count*pocket.global_level,
                    rand_i(20 + pocket.global_level * 5, 30 + pocket.global_level * 5) + pocket.upgrades_count*pocket.global_level*5, 
                    lvl=level, attack_speed=1.03**level)
    elif hero_pro == hero_types[1]:
        hero = Archer(hero_name, 
                    rand_i(3 + pocket.global_level, 5 + pocket.global_level) + pocket.upgrades_count*pocket.global_level,
                    rand_i(15 + pocket.global_level * 5, 25 + pocket.global_level * 5) + pocket.upgrades_count*pocket.global_level*5, 
                    lvl=level, attack_speed=1.03**level)
    elif hero_pro == hero_types[2]:
        hero = Berserk(hero_name, 
                    rand_i(4 + pocket.global_level, 5 + pocket.global_level) + pocket.upgrades_count*pocket.global_level,
                    rand_i(15 + pocket.global_level * 5, 20 + pocket.global_level * 5) + pocket.upgrades_count*pocket.global_level*5, 
                    lvl=level, attack_speed=1.03**level)
    hero.health = hero.max_health
    # pocket.upgrades_count = 1
    show_stats(hero)
    return hero


def create_enemy(kills):
    global enemy
    enemy_name = enemy_names[random.randint(0, len(enemy_names) - 1)]
    if kills % pocket.global_level == 0 and kills != 0:
        enemy = Zombie("Foreigner " + enemy_name, 
                        rand_i(3 * pocket.global_level, 5 * pocket.global_level),
                        rand_i(20 * pocket.global_level, 40 * pocket.global_level),
                        money=rand_i(2 * pocket.global_level, 4 * pocket.global_level),
                        exp=rand_i(3 * pocket.global_level, 6 * pocket.global_level),
                        lvl=pocket.global_level, attack_speed=1.05**pocket.global_level)
        print("FOREIGN Zombie sneaked in")
    elif kills % 10 == 0 and kills != 0:
        enemy = Zombie("FATTY " + enemy_name, rand_i(5, 10), rand_i(40, 80),
                        money=rand_i(4 + pocket.global_level, 8 + pocket.global_level),
                        exp=rand_i(6 + pocket.global_level, 12 + pocket.global_level),
                        lvl=pocket.global_level, attack_speed=1.05**pocket.global_level)
        print(f"{hero.name} encountered fat zombie")
    elif kills % 50 == 0 and kills != 0:
        enemy = Zombie("BOSS " + enemy_name, rand_i(10, 20), rand_i(80, 160),
                       money=rand_i(8 + pocket.global_level, 16 + pocket.global_level),
                       exp=rand_i(12 + pocket.global_level, 24 + pocket.global_level),
                       lvl=pocket.global_level, attack_speed=1.05**pocket.global_level)
        print(f"{hero.name} encountered Boss zombie")
    else:
        enemy = Zombie(enemy_name, rand_i(1, 3), rand_i(10, 20),
                       money=rand_i(1 + pocket.global_level, 2 + pocket.global_level),
                       exp=rand_i(2 + pocket.global_level, 3 + pocket.global_level),
                       lvl=pocket.global_level, attack_speed=1.05**pocket.global_level)
    enemy.health = enemy.max_health
    show_stats(enemy)


def att_hp_upgrades():
    if hero.health == 0:
        print("Your hero is dead, resurrect him or call the new one")
        return
    if pocket.money >= 2 ** pocket.upgrades_count and hero.health > 0:
        hero.attack += pocket.global_level
        hero.health += pocket.global_level*5
        hero.max_health += pocket.global_level*5
        print(f"Hero stats got a boost: attack {pocket.global_level} and health {pocket.global_level*5}")
        pocket.money -= 2 ** pocket.upgrades_count
        pocket.upgrades_count += 1
    else:
        print("Not enough money or your hero is dead")
    return


def resurrect_potion():
    if hero.health > 0:
        print("Hero is alive")
        return
    if pocket.money >= 50 * hero.level:
        hero.health += 20 * hero.level
        if hero.health > hero.max_health:
            hero.health = hero.max_health
        pocket.money -= 50 * hero.level
        print(f"+{20*hero.level}HP, current HP - {hero.health}/{hero.max_health}")
    else:
        print("Not enough money")


def speed_upgrade():
    if pocket.money >= 2 ** pocket.speed_count:
        pocket.attack_speed *= 0.95
        pocket.money -= 2 ** pocket.speed_count
        pocket.speed_count += 1
    else:
        print("Not enough money")


def show_stats(type="all"):
    if type == "all":
        print(hero)
        print(enemy)
        print(pocket)
    else:
        print(type)


def attack(kills):
    console_clr()
    enemy_power = enemy.attack + rand_i(-1 + int(kills / 10) + enemy.level, 1 + int(kills / 10) + enemy.level)
    hero.health -= enemy_power
    time.sleep(1 * pocket.attack_speed / (hero.attack_speed+1))
    print(f"\n{enemy.name} stroke {hero.name} with {enemy_power} leaving {hero.name} with {hero.health} health")
    hit_count = hero.attack_speed/enemy.attack_speed
    # print(hit_count, hero.attack_speed, enemy.attack_speed)
    if hit_count <= 1:
        hero_power = hero.attack + rand_i(-1 + pocket.global_level, 1 + pocket.global_level)
        enemy.health -= hero_power
        time.sleep(1 * pocket.attack_speed / (hero.attack_speed+1))
        print(f"{hero.name} stroke {enemy.name} with {hero_power} leaving {enemy.name} with {enemy.health} health")
    for i in range(int(hit_count)):        
        hero_power = hero.attack + rand_i(-1 + pocket.global_level, 1 + pocket.global_level)
        enemy.health -= hero_power
        time.sleep(1 * pocket.attack_speed / (hero.attack_speed+1))
        print(f"{hero.name} stroke {enemy.name} with {hero_power} leaving {enemy.name} with {enemy.health} health")
    if hero.health <= 0 and enemy.health <= 0:
        hero.speak()
        print("\nA draw... both lay silent")
        hero.health = 0
        enemy.health = 0
    if hero.health <= 0:
        hero.speak()
        print("\nYour hero died in fierce combat")
        hero.health = 0
    elif enemy.health <= 0:
        enemy.speak("")
        print(f"\nYour hero killed {enemy.name} and earned {enemy.experience} exp and found ${enemy.money}")
        enemy.health = 0


def auto_attack():
    if hero.health == 0:
        print("Your hero is dead, resurrect him or call the new one")
        return
    kills = 0
    global money
    while True:
        attack(kills)
        time.sleep(1 * pocket.attack_speed / enemy.attack_speed)
        if hero.health == 0:
            print(f"{hero.name} level {hero.level} killed {kills} enemies before vanishing\n \
and earned you ${hero.money} for upgrades of future heroes")
            if kills > pocket.best_kills:
                pocket.best_kills = kills
                print(f"Record number of Zombies is slain - {pocket.best_kills}!")
            pocket.money += hero.money
            if pocket.money > 100000:
                print("Now you have enough for a peaceful life in your own mansion")
            saved = [
                str(pocket.money),
                str(pocket.attack_speed),
                str(pocket.global_exp),
                str(pocket.global_level),
                str(pocket.upgrades_count),
                str(pocket.speed_count),
                str(pocket.best_kills),
                str(hero.level) # Not used yet
                ]
            print("Pocked saved")
            with open("autosave.txt", "w") as save:
                save.writelines(line + "\n" for line in saved)
            return
        elif enemy.health == 0:
            kills += 1
            hero.health += 1*pocket.global_level
            if hero.health > hero.max_health:
                hero.health = hero.max_health
            hero.money += enemy.money
            hero.experience += enemy.experience
            pocket.global_exp += enemy.experience
            create_enemy(kills)
        if hero.experience >= 10 * hero.level:
            hero_levelup()
        if pocket.global_exp >= 4 ** pocket.global_level:
            world_levelup()


def world_levelup():
    pocket.global_exp -= 4 ** pocket.global_level
    pocket.global_level += 1
    print(f"Global level increased to level {pocket.global_level}")


def hero_levelup():
    hero.experience = hero.experience - 10 * hero.level
    hero.level += 1
    print(f"{hero.name} in now level {hero.level}!")
    hero.attack += rand_i(1, 2)
    hero.max_health += 10
    hero.attack_speed *= 1.03
    hero.health += hero.max_health
    if hero.health > hero.max_health:
        hero.health = hero.max_health


def main():
    """
    Auto-battler with some upgrades.
    ch - create new hero
    e - create new enemy
    b - buy upgrades to attack and health
    as - buy game speed upgrades
    rc - recreate characters, you will loose all the money
    s - print current stats of your hero and enemy
    a - attack
    h - help
    q - quit
    """

    commands = {
        # "ch": create_hero,
        # "e": create_enemy,
        "b": att_hp_upgrades,
        "as": speed_upgrade,
        "r": resurrect_potion,
        "rc": recreate_characters,
        "s": show_stats,
        # "a": attack,
        "aa": auto_attack,
        "h": help
    }
    create_wallet()
    # create_hero()
    create_enemy(0)
    auto_attack()

    while True:
        print(f"\nFor help type 'h'\n \
You have {pocket.money} to buy upgrades (Current game speed increased by {1 / pocket.attack_speed:.2f})")
        print(f"Att/HP upgrade cost: {2 ** pocket.upgrades_count}\n \
Resurrection potion cost: {50 * hero.level}\n \
Game speed boost cost: {2 ** pocket.speed_count}")
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
    # del hero
    # del enemy
    # print("\nReturning to menu...")


main()
