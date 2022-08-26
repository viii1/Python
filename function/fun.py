# Module Package and Library

print("Hello")
"""
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans 
    else:
        high = ans
    ans = (high + low)/2.0

"""
    
#print('numGuesses =', numGuesses)

#print(ans, 'is close to square root of', x)

#FORMAL PARAMETERS
"""
def sum(a,b):
    return a+b
print(sum)

"""
#Actual Parameters

#positional parameter



def results(name,marks):
    print("Name of the stuent:",name)
    CGPA = marks/10
    print("CGPA is:",CGPA)

#results("geek",45)
#result(45,"geek")
#results(45,45)

#Keyword parameters

#results(name="geek", marks=45)

#Default parameters

"""
def result(name, marks = 95):
    print("Name of student : ", name)
    cgpa = marks/10
    print("CGPA is : ", cgpa)

# calling above function 
result("Geek") # Invocation 1 
result("Geek", 90) # Invocation 2
"""

#Variable length parameter

"""
def square_of_numbers(farg, *args):
    print("Type of arg is ", type(args))
    print("farg is : ", farg)
    for each_arg in args: 
        print("args is : ", each_arg)
square_of_numbers(1, 5, 10, 15)

#HOW many FRAG and *ARGs(Variable length parameter)?
"""
#Built in NAMESPACE
#dir(__builtins__)
"""
def f():
    print('Start F()')
    
    def g():
        print('Start g()')
        print('End g()')
        return
    g()
    
    print('End f()')
    return
f()
"""
    
#g() is the local namespace
#f() is the enclosing namespace

#variable scope
"""
x = 'global'
def f():
    x = 'enclosing'

    def g():
       x = 'local'
      print(x)

     g()

f()
local
"""
def radians_to_degrees(theta):
    """
    Returns: theta converted to degrees
     
    Value return has type float
     
    Parameter theta: the angle in radians
    Precondition: theta is a float
    """
    return theta * (180/3.14159)
radians_to_degrees(90.0)