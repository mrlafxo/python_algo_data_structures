#use recursion to implement a countdown counter

def countDown(x):

    if x == 0:
        print("Countodwn done!")
        return

    else:
        print(x, "...")
        countDown(x-1)
        #print ("releasing stack")


countDown(5)
