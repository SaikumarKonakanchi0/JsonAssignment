# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self,name=None,age=0,coat_color=None):
        self.name=name
        self.age=age
        self.coat_color=coat_color
    def description(self):
        return self.name, self.age
    def get_info(self):
        return self.coat_color
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    def run(self):
        return "Jack Russell Terriers can run"
    def bark(self):
        return 'Jack Russel Terriers Woof...Woof...'
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
    def eat(self):
        return "Bulldogs are good eaters."
    def kill(self):
        return 'Bulldogs will be killed by their owners.'

dog=Dog('GermanShepherd',2,'Blue')
print(dog.description())
print(dog.get_info())
jackrussellterrier=JackRussellTerrier('Jack',3,'Green')
print(jackrussellterrier.name)
print(jackrussellterrier.age)
print(jackrussellterrier.coat_color)
print(jackrussellterrier.run())
print(jackrussellterrier.bark())
bulldog=Bulldog('Bull',4,'Red')
print(bulldog.name)
print(bulldog.age)
print(bulldog.coat_color)
print(bulldog.eat())
print(bulldog.kill())


#Expected Output:
# ('GermanShepherd', 2)   ***return statement will return multiple items in the form of Tuple only***
# Blue
# Jack
# 3
# Green
# Jack Russell Terriers can run
# Jack Russel Terriers Woof...Woof...
# Bull
# 4
# Red
# Bulldogs are good eaters.
# Bulldogs will be killed by their owners.