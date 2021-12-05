
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
    #############################
    """Setting assert rule , so that thet conditions are set and it will not use all the stack memory, before using assert , 
    recrusion method will accept non onteger numbers and negative number
    and it will give error """
    assert x >= 0 and type(x) == int, 'The number must be positive integers only'
    if x == 1: 
        return 1
    else:
        return (x * factorial(x-1))


num = 4
final =  factorial(num)
# print("The factorial of", num, "is", final )



# ############################################################
# ############################################################
# write a recursive function to find fibonacci series 
# 0 , 1 , 1 , 2,3,5,8,13,21
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integers only'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 5
# print(fibonacci(6))

# ############################################################
# ############################################################
# write a recursive function to find sum of digits of a positive integer 
# 
def sum(n):
    """Assert will check the number is inserted is positive or not and is integer only
    Then if loop will check that if n is equals to 0 then it will stop recursive funtion
    otherwise it will check remainder"""
    assert n >= 0 and type(n) == int, 'The number must be positive integers only'
    if n == 0:
        return 0
    else:
        return int(n%10) + sum(int(n/10))

# print(sum(52))



# HACKER RANK 
# Find the number of ways that a given integer,X , can be expressed as the sum of the Nth powers of unique, natural numbers.
import random


def powerSum(x,n):
    N = random.randint(0,100)
    N2 = random.randint(0,100)
    totalSum = (N**n) + (N2**n)
    # print(totalSum)
    # print(x)
    if(x != totalSum):
        return powerSum(x,n)

    else:
        
        print(N , N2)
        print(totalSum)
    

   

powerSum(5,2)



        



