from Weapon import Weapon

class Dinosaur:
    def __init__(self,name,attack_power,health) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack(self,robot):
        robot.health -= attack_power