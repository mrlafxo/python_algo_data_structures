#Find the greatest common denominator of two number
#using the Euclid's algorithm

def gcd(a,b):

    while (b != 0):
      temp = a
      a = b
      b = temp % b

    return a


#trying the function
print(gcd(20,8))
print(gcd(22,76))
