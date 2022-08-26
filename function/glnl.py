
#Declaring Global variable
"""
x = "global"

def f():
    print("x inside:", x)


f()
print("x outside:", x)

"""

"""

x = "global"

def f():
    x = x * 2
    print(x)

f()

"""

#Creating local variable
"""
def f():
    y = "local"
    print(y)

f()

"""
"""
#For nested function
x=60
def harry():
    x = 20
    def rohan():
        global x
        x = 70
        print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)


"""
