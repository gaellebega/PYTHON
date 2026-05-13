# the tuples are ordered it means that items have a defined order and tat order will not change
# allow duplicates
# unchangeable
# the order dont have to change
# the tuple can be any data type
# you can use the tuple() to make the tuple
thistuple=tuple(("apple","banana","cherry"))
print(thistuple)
# to access the tuples
print(thistuple[1])

# you can add a tuple to another tuple
y=("orange","avocado")
# to make it not look like the string then you have,
x=("smoothies",)
y+=x
print(y)
newthistuple=("apple","banana","orange","amapera")
(a,b,c,d)=newthistuple
print(a)
print(b)
print(c)
print(d)

