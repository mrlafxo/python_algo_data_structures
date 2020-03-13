#create a queue and try out the Python queue functions

#object optimized for adding and removing elements from both ends of the collection
from collections import deque

queue = deque()

#append some elements to queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print (queue)

#remove an element from the front of the list
x = queue.popleft()

print (x)
print (queue)
