#factorial
# factorial using loop
# Python program to find the factorial of a number provided by the user.
"""
# change the value for a different result
num = 3

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

"""
"""
# Python program to find the factorial of a number provided by the user
# using recursion

def factorial(x):
    #This is a recursive function to find the factorial of an integer

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 3

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)

"""
"""
def factorial(x):
   #This is a recursive function to find the factorial of an integer

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
"""
def sum(a,b):
    return a+b
print(sum(3,4))
