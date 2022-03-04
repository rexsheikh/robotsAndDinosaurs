from Dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs = []

    def create_herd(self,dinosaur):
        self.dinosaurs.append(dinosaur)
        
    def display_herd(self,dinosaurs):
        for i in range(0,len(dinosaurs)):
            print(f" name/health: {dinosaurs[i].name}/{dinosaurs[i].health}")
            