#demonstrate hash tables usage in Python

items1 = dict({"key1":1, "key2":2, "key3":3, "key4":4})

print (items1)

#create a hash table progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 'three'
items2["key4"] = 4

print (items2)

#accessing a non-existing element
#print (items1["key6"])

#replace an element
items2["key1"] = 2
print (items2)

#iterate through the elements
for k,v in items1.items():
    print ("Key: ", k, " value ", v)
