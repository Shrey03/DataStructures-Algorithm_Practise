
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

recursiveMethod(5)