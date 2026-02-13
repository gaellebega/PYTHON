empty_set=set()
print(empty_set)
empt_set={}
print(type(empt_set))
# this is invalid because it contains the list
# invalid_set={1,2,3,[4,5]}
# print(invalid_set)
# add the elements to the set
empty_set.add("hyy")
empty_set.add(True)
# empty_set.add(False)
empty_set.add(0)
# the more that we add the more that everything comes before the other which was there before
# remove is used to remove the given element 
# empty_set.remove("hyy")
print(empty_set)
empty_set.discard("hyy0")
# the difference between the discard and remove is that witht dicard when you try to remove the element which is not there it is not gonna print error but tyr to ignore that
# pop on set is used to remove the random element when it is used on the list 
# to append elements on the list we use the append  but on the set we use the add but it choose where it can go


setA={1,2,3}
setB={3,4,5,6}
# here we have used the union
result1=setA|setB
print(result1)
# here we have to return the intersection
print(setA&setB)
# here we have to return the difference
print(setA-setB)

# VALID OEPRATIONS
# symmetric_difference=setA^setB
symmetric_difference=setB^setA
symmetric_difference2=setA^setB
print(symmetric_difference)
print(symmetric_difference2)


# invalid operations on the sets
# concatination
# multiplication
# indexing and slice

# membership for 1 in or for 3 not

square_set={x**2 for x in range (10)}
print(square_set)
