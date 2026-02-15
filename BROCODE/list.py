# ordered and changable duplicates are okay

fruits=["apple","orange","banana","coconut"]
# when you want to step but also including the first elemnt at the index 0 you wany need to use the
print(fruits[::2])
print("apple" in fruits)
fruits.reverse()
print(fruits)
fruits.remove("apple")
fruits.insert(0,"pinapple")
# sort can be used on the list only but sorted can be used on tuples,dictionaries and string and sets
fruits.sort()
fruits.clear()
print(fruits.index("coconut"))
# dupliactes on the sets are okay
print(fruits.count("banana"))