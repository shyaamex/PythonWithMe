# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.


#Creating a class 
class Myclass:
    def hello(self):
        
        print("Hello, This is Shyam")

    


# Creating an object of above class (Myclass)
a = Myclass()


# Calling a method of the class through its object
a.hello()



# You can modify properties of class with objects like this:
a.var=30
print(a.var)



# You can delete the properties of objects as well
del a.var
