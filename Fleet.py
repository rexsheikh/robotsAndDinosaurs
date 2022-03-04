from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self,robot):
        self.robots.append(robot)
    
    def display_fleet(self,robots):
        for i in range(0,len(robots)):
            print(f" name/health:{robots[i].name}/{robots[i].health}")
 