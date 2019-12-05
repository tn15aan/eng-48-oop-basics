# OOP BASICS

This class is going to cover the basics of OOP.

### Covered in this class: 

**4 Pillars**:
- Abstraction
- Inheritance
- Encapsulation
- Polymorphism

### Other learning outcomes
- Git + Github
- Documentation with Mark Down
- Best practices and organisation


### Definitions
Add your definitions here:

**Class**
It is a blue print of an object
It wraps methods and attributes

**Methods != function**
Just like a function, they can take in arguments, run a block of code
However, they can only be used by an instance of its class

**Attributes**
Hold information about or specific object. Are set in the def __init__() method
with arguments like any other function

**__init__()**
AKA - Constructor or initializer.
This method runs everytime an object is created. So when you do:
''''
    animal1 = Animal('Fred', 10, 2)
''''

**self**
Refers to the object/instance

**Inheritance**
Is the ability of classes to inherit characteristic(parameters) and behaviors 
from parent class.

**Instance / object**
It is an occurance of an object

**Polymorphism**
Poly means many and morph means forms.
So polymorphism is 'Many forms'.
Polymorphism in OOP is for the ability to change methods and characteristics
instances of child classes
    - Method Polymorphism (at method level)
    
**Abstraction**
Is hiding complexity from the user.
- Heating food in the microwave with one button - what happens?
- Changing gears in a car
- Coding languages in computing

Specific to us, we will:
- Write nice documentation for how to import and use our code
- Use inheritance and importing to hide the code
- Ultimately we can package it into a module that could be imported with PIP

## Task:
Create a new project
- Create a class animal:
- characteristics:
    - alive
    - bones
- methods:
    - eat
    - sleep
    - make_sound()
    
- Create a class Dog()
- Make it inherit from Animals
- Give it all the attributes of animal plus:
    - owner
    - name
    - dog_collar
    
- methods:
    - all the other ones plus:
    - eat_bone
    - run
    - greet_owner
    - polymorph the method make_sound to return the string 'Woouff'

One of these methods needs to take a argument
Another method should have a default value

- Have a run file
    - Import all your classes
    - Create 2 animals
    - Create 2 dogs
    - Call some methods on them
    - 
