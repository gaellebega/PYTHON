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
empty_set.add(False)
empty_set.add(0)
# the more that we add the more that everything comes before the other which was there before
# remove is used to remove the given element 
empty_set.remove("hyy")
print(empty_set)
