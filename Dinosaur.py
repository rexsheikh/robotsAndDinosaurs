from Weapon import Weapon

class Dinosaur:
    def __init__(self,name,health,attack_power,energy):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.energy = energy

    def attack(self,robot,attack):
        robot.health -= attack
        self.energy -= 10