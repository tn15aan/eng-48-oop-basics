from animal_class import *
from reptile_class import * #can import this only as it imports from animal

# How to create an object
# Creating an instance of Animal Class
simba = Animal('simba', 3, 1, 8)

#Creating a reptile
ringo = Reptile('Ringo', 3, 1, 8)

# Checking data type
# print(simba)
# print(type(simba))

# Calling methods on an object
print(simba.eat('foooood'))
print(simba.go_potty())
print(simba.sleep()) # Behaviours
# every time it's run it creates new instance of the object

# Call the attributes of an object
print(simba.age)
print(simba.number_legs)

# Reptile
print(ringo.eat('fooood'))
print(ringo.seek_heat())

# Animal class doesn't have seek_heat
print(simba.mate_calling())
print(ringo.mate_calling())