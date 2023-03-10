## Functions in Python
# Functions are used to make a set of code reusable and to decrease the code complexity






def onefunction():                  #Creating a function
    a=input("Enter your name : ")
    print(f"Hello { a } ")

print("Start")
onefunction()                       #Calling a funciton
print("Stop\n\n")







# Passing Arguments in Functions
# Arguments are specified after the function name, inside the parentheses

def my_function(fname):
      print(f"Hii, This is { fname }" )

my_function("Joe")
my_function("Rishi")
my_function("Putin")


print("\n\n\n")




# Passing multiple agrguments
def my_function2(fname, lname):
      print(fname + " " + lname)

my_function2("Shyam", "Pratap")






print("\n\n\n")
# We can also set default parameter value, if 
# no argument has passed, then the defalut value
# will be issued

def _name(name = "Shyam"):
      print("I am from " + name)

_name("Narendra")
_name("Modi")
_name()
_name("Joe")





# The Return Statement
# It is used when you want your function to return values
def multi(x):
      return 2 * x

print(multi(3))
print(multi(5))
print(multi(9))



# The Pass statement 
# When you don't need a function but you might need in future
# Then, we can use pass statement to skip it for now
 
def Function_one():
    pass