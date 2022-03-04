from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robot import Robot
from Weapon import Weapon

class Battlefield:

    def __init__(self):
        self.rifle = Weapon('rifle',20)
        self.laser_beam = Weapon('laser beam',50)
        self.sword = Weapon('sword',100)
        self.killtron = Robot('killtron',100,self.sword)
        self.destructor = Robot('destructor',100,self.sword)
        self.mfst_paperclip = Robot('mfst_paperclip',100,self.sword)
        self.robots = [self.killtron,self.destructor,self.mfst_paperclip]
        self.fleet = Fleet(self.robots)

        self.t_rex = Dinosaur('t-rex',100,100)
        self.v_raptor = Dinosaur('velociraptor',100,100)
        self.bronto = Dinosaur('brontosaurus',100,100)
        self.dinosaurs = [self.t_rex,self.v_raptor,self.bronto]
        self.herd = Herd(self.dinosaurs)

        self.turn_count = 0


    def run_game(self):
        self.battle()

    def display_welcome(self):
        print("*******************************\nWelcome to Robots vs. Dinosaurs\n*******************************")
        
    def battle(self):
        while(len(self.dinosaurs) > 0 and len(self.robots) > 0):
            if self.turn_count % 2 == 0:
                self.dino_turn()
                self.turn_count += 1
            else:
                self.robot_turn()
                self.turn_count += 1

            for i in range(0,len(self.fleet.robots)):
                if self.fleet.robots[i].health == 0:
                    self.robots.remove(self.robots[i])
                else:
                    break
            for j in range(0,len(self.herd.dinosaurs)):
                if self.herd.dinosaurs[i].health == 0:
                    self.herd.dinosaurs.remove(self.herd.dinosaurs[i])
                else:
                    break
            self.display_winners()
 

    def dino_turn(self):
        self.herd.display_herd()
        self.fleet.display_fleet()
        self.dino_input = int(input('choose a dinosaur to attack with: '))
        self.dino_choice = self.herd.dinosaurs[self.dino_input]
        self.robot_input = int(input('choose a robot to attack: '))
        self.robot_choice = self.fleet.robots[self.robot_input]
        self.dino_choice.attack(self.robot_choice)

        


    def robot_turn(self):
        self.herd.display_herd()
        self.fleet.display_fleet()
        self.robot_input = int(input('choose a robot to attack with: '))
        self.robot_choice = self.robots[self.robot_input]
        self.dino_input = int(input('choose a dinosaur to attack: '))
        self.dino_choice = self.dinosaurs[self.dino_input]
        self.robot_choice.attack(self.dino_choice)


    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass
    
    def display_winners(self):
        if len(self.dinosaurs) == 0:
            print('robots win!')
        elif len(self.robots) == 0:
            print('dinosaurs win!')





#attack examples
# killtron.attack(t_rex)
# t_rex.attack(killtron)





# 1. print welcome
# 2. show current herd and fleet.
# 3. pick a dinosaur to attack with and a robot to attack