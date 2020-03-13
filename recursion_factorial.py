#using recursion to implement power and factorial functions

def power (num, pwr):

    #breaking case
    if pwr == 0:
        return 1

    else:
        return num * power(num, pwr -1)

def factorial (num):

    if num == 0:
        return 1
    else:
        return num * factorial(num -1)



print ("{} to the power of {} is equal to {}".format(2, 3, power(2,3)))
print ("The factorial of {} is {}".format(5, factorial(5)))
