# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):

    if len(dataset) > 1: #recursion breaking condition
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        mergesort(leftarr) #recursive calls
        mergesort(rightarr) #recursive calls

        i = 0 # index left array
        j = 0 # index right array
        k = 0 # index merged array

        print (leftarr)
        print (rightarr)
        exit()

        while i < len(leftarr) and j < len(rightarr):

            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1

            k += 1

        #if values remains in arrays
        while i < len(leftarr):

            dataset[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):

            dataset[k] = rightarr[j]
            j += 1
            k += 1


# test the merge sort with data
print("Initial items: ", items)
mergesort(items)
print("Ordered items: ", items)
