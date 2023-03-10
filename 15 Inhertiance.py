# Inheritance in python
# Using inheritance, a child class can access objects of parents class


# This is an empty class


class first:
    pass #Pass means nothing



# Here, it is the base class
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
        
        
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
        
        
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
        
        
# Implementing the inheritance       
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  


