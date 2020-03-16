# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1

    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:

        midPoint = (lowerIdx + upperIdx) // 2

        if itemlist[midPoint] == item:
            return midPoint

        if item > itemlist[midPoint]:
            lowerIdx = midPoint + 1

        elif item < itemlist[midPoint]:
            upperIdx = midPoint - 1

    # if indexes have crossed, the value do not exist in the list
    if lowerIdx > upperIdx:
        return None


print(binarysearch(20, items))
print(binarysearch(53, items))
print(binarysearch(2500, items))
