from Weapon import Weapon
from Dinosaur import Dinosaur


class Robot:
    def __init__(self,name,health,weapon,energy):
        self.name = name
        self.health = health
        self.weapon = Weapon(weapon.name,weapon.attack_power)
        self.energy = energy

    def attack(self,dinosaur):
        dinosaur.health -= int(self.weapon.attack_power)
        self.energy -= 10


