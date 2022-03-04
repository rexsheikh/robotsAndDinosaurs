from Weapon import Weapon
from Dinosaur import Dinosaur


class Robot:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = Weapon(weapon.name,weapon.attack_power)

    def attack(self,dinosaur):
        dinosaur.health -= int(self.weapon.attack_power)
