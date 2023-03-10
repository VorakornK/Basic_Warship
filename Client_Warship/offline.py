import random as rd
import time
import os

number_of_player = 2
number_of_ship = 3
x = 0

class Ship:
    def __init__(self, id, hp, atk):
        self.id = id
        self.Hp = hp
        self.Atk = atk
    def attack(self, target):
        target.Hp -= self.Atk
    def heal(self):
        self.Hp += self.Atk


class Player:
    def __init__(self, name):
        self.name = name
        self.front = 0
        self.ships = []
        self.survive = number_of_ship
        for i in range(number_of_ship):
            self.ships.append(Ship(i, rd.randint(20, 100), rd.randint(5, 20)))
    def attack(self, target):
        self.ships[self.front].attack(target.ships[target.front])
    def heal(self):
        self.ships[self.front].heal()
    def switch(self, id):
        self.front = id
    def Status(self):
        for i in range(3):
            if self.ships[i].Hp > 0:
                return True
        return False
        
class Board:
    def __init__(self):
        self.id = 0
        self.player = []
        self.complete = False
    def add_player(self):
        for i in range(number_of_player):
            self.player.append(Player(input(f"Please enter the name of Player {i + 1}: ")))
    def status(self):
        print(30*"=")
        for i in range(len(self.player)):
            print("Player", self.player[i].name, "Ship Status:")
            for j in range(number_of_ship):
                print("Ship", j + 1, "Hp:", self.player[i].ships[j].Hp if self.player[i].ships[j].Hp > 0 else 0, "Atk:", self.player[i].ships[j].Atk, "(front)" if (j == self.player[i].front and self.player[i].ships[j].Hp > 0) else "" + "(destroy)" if self.player[i].ships[j].Hp <= 0 else "")
        print(30*"=")
    def play(self):
        self.add_player()
        os.system("clear")
        Players = self.player
        player = 0
        while True:
            self.status()
            print(f"It's Player {Players[player].name}'s turn.")
            print("What R U gonna do? \n(1 for attack, 2 for heal and 3 for switch front ship)")
            x = int(input())
            while (x not in [1, 2, 3] or (Players[player].survive == 1 and x == 3)):
                if (Players[player].survive == 1 and x == 3):
                    print("You can't switch ship when you only have one ship left")
                else: print("Invalid input")
                x = int(input())
            if x == 1:
                print("Attack!!")
                enemy = Players[(player + 1) % number_of_player]
                Players[player].attack(enemy)
                print("Ship", Players[player].front, "From player:", Players[player].name, "attack Ship", enemy.front, "From player:", enemy.name)
                print("Ship", enemy.front, "Hp:", 0 if enemy.ships[enemy.front].Hp < 0 else enemy.ships[enemy.front].Hp)
                #Check status and is defend lose or not
                if (enemy.ships[enemy.front].Hp <= 0):
                    print("Player", enemy.name, "ship", enemy.front, "is destroyed")
                    enemy.survive -= 1
                    count = 0
                    while (enemy.ships[enemy.front].Hp <= 0 and count < number_of_ship):
                        count += 1
                        enemy.front += 1; enemy.front %= number_of_ship
                    if (enemy.survive > 0):
                        print("Now,", "Ship", enemy.front, "From:", enemy.name, "is now at front")
                if (enemy.survive == 0):
                    os.system("clear")
                    self.status()
                    print("Player", Players[player].name , "win")
                    break
            elif x == 2:
                Players[player].heal()
                print("Ship", Players[player].front + 1, "Hp:", Players[player].ships[Players[player].front].Hp, f"(+{Players[player].ships[Players[player].front].Atk})")
            elif x == 3:
                x = int(input("What ship U want to switch to front: ")); x -= 1
                while (x not in range(number_of_ship) or x == Players[player].front or Players[player].ships[x].Hp <= 0):
                    if x == Players[player].front:
                        print("You can't switch to the same ship")
                    elif Players[player].ships[x].Hp <= 0:
                        print ("You can't switch to a destroyed ship")
                    else: print("Invalid input")
                    x = int(input("What Ship U want to switch to front: ")); x -= 1
                Players[player].switch(x)
                print(f"Now {Players[player].name}'s front ship switch to Ship", x + 1)
            player += 1
            player %= number_of_player
            #time.sleep(5)
            os.system("clear")


Board().play()