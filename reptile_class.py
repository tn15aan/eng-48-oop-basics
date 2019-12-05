from animal_class import *

class Reptile(Animal):

    def __init__(self, name, eyes, legs, n_chamber_hearts, age = 0):
        super().__init__(name, eyes, legs, age)
        self.scales = True
        self.cold_blood = True
        self.n_chamber_heart = n_chamber_hearts

    def mate_calling(self): # Change method for reptile class using polymorphism
        return 'Look at my scales! They look good!'

    def seek_heat(self):
        return 'hummm bit chilly, lets get some sun'

    def seek_share(self):
        return 'Who turned on the heating in this world? --> going to find some shade'

    def prey(self):
        return 'Waiittt for it... waiiitttt... AND POUNCE!!!'

    def lay_eggs(self):
        return 'What you looking at? Never seen a lizard lay eggs?'