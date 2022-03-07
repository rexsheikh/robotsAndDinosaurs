from Dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs = []
    
    def create_herd(self,dinosaur):
        self.dinosaurs.append(dinosaur)

    def display_herd(self):
        print('Here are the dinosaurs\n                   name/health/energy')
        for i in range(0,len(self.dinosaurs)):
            print(f"Press {i} to select: {self.dinosaurs[i].name}/{self.dinosaurs[i].health}/{self.dinosaurs[i].energy}")
            