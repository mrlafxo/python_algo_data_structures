# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

print('\n', items, '\n')

htable = dict()

for item in items:
    htable[item] = 0

result = set(htable.keys())
print("Here's the list without the duplicate elements:")
print('\n', result, '\n')
