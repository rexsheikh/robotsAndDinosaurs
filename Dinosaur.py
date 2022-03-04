from Weapon import Weapon

class Dinosaur:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack(self,robot):
        robot.health -= self.attack_power