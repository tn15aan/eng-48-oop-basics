# Define Animal Class

class Animal():
    # Class is a cookie cutter for objects
        # wraps the characteristics and it's behaviours

    # Define some characteristics
    def __init__(self, name, eyes, legs, age = 0):
        self.name = name
        self.bones = True
        self.alive = True
        self.number_eyes = eyes
        self.number_legs = legs
        self.age = age

    # Define some behaviours - Methods
        # Things an instance of what an object can do
        # Functions that are dependent on an object type

    def eat(self, munch):
        return 'Nom NOM NOM!' + munch

    def mating(self):
        return ' <3 '

    def mate_calling(self):
        return 'Swipe right ;)'

    def sleep(self):
        return 'zzzzz'

    def go_potty(self):
        return 'HHUMMMM!!!! .... 0.0 ! -.-   --- zen '

