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
        self.fleet = Fleet()
        self.fleet.create_fleet(self.killtron)
        self.fleet.create_fleet(self.destructor)
        self.fleet.create_fleet(self.mfst_paperclip)


        self.t_rex = Dinosaur('t-rex',100,100)
        self.v_raptor = Dinosaur('velociraptor',100,100)
        self.bronto = Dinosaur('brontosaurus',100,100)
        self.herd = Herd()
        self.herd.create_herd(self.t_rex)
        self.herd.create_herd(self.v_raptor)
        self.herd.create_herd(self.bronto)


        self.turn_count = 0

    def run_game(self):
        self.display_welcome()
        print("\n")
        self.battle()

    def display_welcome(self):
        print("*******************************\nWelcome to Robots vs. Dinosaurs\n*******************************")
        
    def battle(self):
        while(len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0):
            self.herd.display_herd()
            print("\n")
            self.fleet.display_fleet()
            if self.turn_count % 2 == 0:
                self.dino_turn()
                self.fleet.robots = list(filter(lambda x: x.health != 0, self.fleet.robots))
                self.turn_count += 1
            else:
                self.robot_turn()
                self.herd.dinosaurs = list(filter(lambda x: x.health != 0, self.herd.dinosaurs))
                self.turn_count += 1
        self.display_winners()
 
    def dino_turn(self):
        self.dino_input = int(input('choose a dinosaur to attack with: '))
        self.dino_choice = self.herd.dinosaurs[self.dino_input]
        self.robot_input = int(input('choose a robot to attack: '))
        self.robot_choice = self.fleet.robots[self.robot_input]
        self.dino_choice.attack(self.robot_choice)

    def robot_turn(self):
        self.robot_input = int(input('choose a robot to attack with: '))
        self.robot_choice = self.fleet.robots[self.robot_input]
        self.dino_input = int(input('choose a dinosaur to attack: '))
        self.dino_choice = self.herd.dinosaurs[self.dino_input]
        self.robot_choice.attack(self.dino_choice)

    def show_dino_opponent_options(self):
        self.herd.display_herd()
        
    def show_robot_opponent_options(self):
        self.fleet.display_fleet()
    
    # def filter_out(self,arr):
    #     for i in range(0,len(arr)):
    #         if arr[i] == 0:
    #             return True 
    #         else:
    #             return False
            
    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print('robots win!')
        elif len(self.fleet.robots) == 0:
            print('dinosaurs win!')


# effectively filter out dead dinos/robots CHECK
# filter/lambda works. now where to put it? 
    #I can run a function to simply identify the health zeros to return index and delete outside of the for loop 
# display winners 

