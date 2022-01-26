import random

min_rand = 5
max_rand = 10


class Board:
    bio = "A fresh new world"
    board_floor = "_"
    board_obstacle = "#"
    board_hero = "&"
    board_chest = "$"

    def __init__(self, height, width, board={}):
        self.height = height
        self.width = width
        self.board = board

    def generate_new(self):
        self.board.clear()
        print("A fresh new world is created!")
        for h in range(self.height):
            self.board[h] = []
            for w in range(self.width):
                self.board[h].append(self.board_floor)

    def place_obstacles(self):
        obstacle = 0
        print("Placing obstacles...")
        for h in range(self.height):
            for w in range(self.width):
                obstacle = random.randint(w-1, w+1)
                if obstacle == w:
                    if h < 2 and w < 2:
                        continue
                    if self.board[h].count(self.board_obstacle) > self.width/2:
                        continue
                    self.board[h][w] = self.board_obstacle

    def place_hero(self):
        print("A hero is born...")
        hero_position = [random.randrange(2), random.randrange(2)]
        self.board[hero_position[0]][hero_position[1]] = self.board_hero
    
    def place_chest(self):
        print("...and a prize for him")
        self.board[self.height - 1][self.width - 1] = self.board_chest

    def show_board(self):
        for h in self.board:
            print(''.join(self.board[h]))


class Item:
    bio = "Anything, really anything you can interact with"

    def __init__(self, name, attack, defence, durability=100):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.durability = durability

    def show_state(self):
        print(f"{self.name} durability {self.durability}")    


def generate_board():
    global cur_board
    cur_board = Board(random.randint(min_rand, max_rand), random.randint(min_rand, max_rand))
    cur_board.generate_new()
    cur_board.place_obstacles()
    cur_board.place_hero()
    cur_board.place_chest()
    show_board()


def show_board():
    cur_board.show_board()


def main():
    
    commands = {
        "g": generate_board,
        "s": show_board,

    }

    while True:
        print("\nFor help type 'h'")
        command = ""
        while not bool(command):
            command = input("\nInput action: ")
        for key in commands:
            if command == key:
                # if command == "h":
                #     commands[command](main)
                #     break
                # elif command == "m":
                #     commands[command](height, width)        
                # else:
                commands[command]()
                break
        if command == "q":
            print("\nQuiting...")
            break
        elif command not in commands:
            print("\nThere's no such command")
            continue
        # print("\nReturning to menu...")


main()
