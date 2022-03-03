from Weapon import Weapon


class Robot:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = Weapon()
        