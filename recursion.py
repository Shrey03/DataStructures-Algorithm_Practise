
# ############################################################
# DAY 1 
# Recursion Algorithm 
# just an example how it works

# ############################################################
# ############################################################
# ############################################################
def fun1():
    fun2()
    print('This is first function')

def fun2():
    fun3()
    print('this is second function ')

def fun3():
    fun4()
    print('this is 3rd function')

def fun4():
    print('this is fourth function')



# fun1()
# ############################################################
# ############################################################
# ############################################################
def recursiveMethod(n):
    if n<1:
        print(f'{n} is less then 1')
    else:
        recursiveMethod(n-1)
        print(n)

# recursiveMethod(5)


# ############################################################
# ############################################################
# Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 6 (denoted as 6!) 6*5*4*3*2*1

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))