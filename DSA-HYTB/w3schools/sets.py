# here we are learning the python sets
thisisset={"apple","banana","cherry"}
thisisset.update(["umuceri","ibijumba"])
print(thisisset)

# to add the element to the set we use the update method when they are more than one element otherwise we use the add
# to remove on the set we can use the reove or discard
# to remove the random on the set we use the pop()

# JOIN SETS
# join return the new set which have the combination of both sets
set1={"one","two","three",3}
set2={1,2,3}
combination=set1.union(set2)
# you can also combine the set with the TUPLES
# also you can write like this
# when we have used the union then the intersection is gonna be kept
combination=set1|set2
print(combination)

combination2=set1.intersection(set2)
combination=set1&set2
print(combination2)

# the frozen set is the version of the set which can be changed,

# the frozenset data type is the frozenset