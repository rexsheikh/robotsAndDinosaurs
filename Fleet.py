from Robot import Robot
from Weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self,robot):
        self.robots.append(robot)



    def display_fleet(self):
        print('Here are the robots\n                      name/health/weapon/energy')
        for i in range(0,len(self.robots)):
            print(f"Press {i} to select --> {self.robots[i].name}/{self.robots[i].health}/{self.robots[i].weapon.name}/{self.robots[i].energy}")
 
