from readline import read_init_file
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
        self.missiles = Weapon('missile',40)
        self.weapons = [self.rifle,self.laser_beam,self.sword,self.missiles]

        # self.killtron = Robot('killtron',100,self.sword)
        # self.destructor = Robot('destructor',100,self.sword)
        # self.mfst_paperclip = Robot('mfst_paperclip',100,self.sword)
        self.fleet = Fleet()
        # self.fleet.create_fleet(self.killtron)
        # self.fleet.create_fleet(self.destructor)
        # self.fleet.create_fleet(self.mfst_paperclip)


        self.attacks = {"punch" : 20,
        "kick": 30,
        "tackle" : 50
        }

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
        self.equip_robots()
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
        self.attack_input = input(f'type the attack you would like {self.attacks}: ')
        self.attack_choice = self.attacks[self.attack_input]
        self.robot_input = int(input('choose a robot to attack: '))
        self.robot_choice = self.fleet.robots[self.robot_input]
        self.dino_choice.attack(self.robot_choice,self.attack_choice)

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
    
    def equip_robots(self):
        print("equip your robots")
        self.robot_name_list = ["killtron","destructor","mfst_paperclip"]
        for i in range(0,len(self.robot_name_list)):
            self.equip_input = int(input(f"choose a weapon for {self.robot_name_list[i]}\n \
                Press 0 for {self.weapons[0].name}\n\
                Press 1 for {self.weapons[1].name}\n\
                Press 2 for {self.weapons[2].name}\n\
                Press 3 for {self.weapons[3].name} --> "))
            self.robot_name_list[i] = Robot(self.robot_name_list[i],100,self.weapons[self.equip_input])
            self.fleet.create_fleet(self.robot_name_list[i])

            

        #iterate through the list of robots. print the robot's name. have the user select the weapon 
        #from the weapon inventory
        #will then need to create the fleet from the robots
        pass
    def robot_attack_option(self):
        pass

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print('robots win!')
        elif len(self.fleet.robots) == 0:
            print('dinosaurs win!')


# effectively filter out dead dinos/robots CHECK
# filter/lambda works. now where to put it? 
    #I can run a function to simply identify the health zeros to return index and delete outside of the for loop 
# display winners 

