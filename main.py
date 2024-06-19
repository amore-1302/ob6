
import random

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other_gero):
        curent_power = self.attack_power
        other_gero.health = other_gero.health - curent_power
        # новое значение для следующей атаки
        self.attack_power = random.randint(0, 10)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game():
    def __init__(self):
        self.gamer = Hero("Игрок")
        self.comp = Hero("Комп")

    def start(self):
        step = 0
        while True:
            print(f"Атакует {self.gamer.name} ")
            self.gamer.attack(self.comp)
            if not(self.comp.is_alive()):
                print(f"Убит  {self.comp.name}  и он проиграл ")
                break

            print(f"Атакует {self.comp.name} ")
            self.gamer.attack(self.gamer)
            if not(self.gamer.is_alive()):
                print(f"Убит  {self.gamer.name}  и он проиграл ")
                break

            step = step + 1
            print(f"Шаг Игры = {step}")
            print(f"У игрока {self.gamer.name} здоровья = {self.gamer.health} ")
            print(f"У игрока {self.comp.name} здоровья = {self.comp.health} ")

            print(" ")


g = Game()
g.start()