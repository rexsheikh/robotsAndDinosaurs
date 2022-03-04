from os import kill
from Dinosaur import Dinosaur
from Fleet import Fleet
from Herd import Herd
from Robot import Robot
from Weapon import Weapon


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        pass
    
    def robot_turn(self,robot):
        pass
    
    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass

sword = Weapon('sword',20)
killtron = Robot('killtron',100,sword)
destructor = Robot('destructor',100,sword)
mfst_paperclip = Robot('mfst_paperclip',100,sword)

t_rex = Dinosaur('t-rex',20,100)
v_raptor = Dinosaur('velociraptor',10,100)
bronto = Dinosaur('brontosaurus',30,100)


fleet = Fleet()
fleet.create_fleet(killtron)
fleet.create_fleet(destructor)
fleet.create_fleet(mfst_paperclip)
fleet.display_fleet(fleet.robots)

herd = Herd()
herd.create_herd(t_rex)
herd.create_herd(v_raptor)
herd.create_herd(bronto)
herd.display_herd(herd.dinosaurs)


killtron.attack(t_rex)
herd.display_herd(herd.dinosaurs)




