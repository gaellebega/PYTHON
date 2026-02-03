# how do we write sets in python

set1={1,2,3,4,5}
set2={3,4,5,6,7,8,9,10}
# print(set1[0])  # this will give error because sets are unordered collections and do not support indexing
# when we add like that 7 then it is going to be on the last index
set1.add(9)
# in sets you can not add already the existing element so there is no error to occur or something but nothing changes
set1.add(2)
set1.add(7)
print(set1)
set1.clear()
print(set1)
# 2.4.26
set1.update([3, 4, 7])
print(set1)
set1.remove(4)
print(set1)
# by doing the update using the other set that is to mean like take the set 2 then add some elements of it and then add them to the set1
set1.update(set2)
print(set1)

# TUPLES
tpl=1,2,3,4,5
print(tpl)