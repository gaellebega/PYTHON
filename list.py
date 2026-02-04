list = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [10,11,12]
]
# this is slice method of start and end the start is the -3 and then stop to -1 but just because -1 
print(list[-3:-1])

# adding an element on the list
list[1][2]=70
print(list)
# example of the lists

list=["str",2,3.5,True,["a","b","c"]]
print(list)
print(list[0])
# this means access by starting from the start but then exclude 2
print(list[:2])
# this means go inside 4 then take the second items like on the index of 2
print(list[4][2])
# travelising lists 

# RANGE FUNCTION ON LIST
# range(2,4)
# del list will remove my variable
# del list
# we can also use in range 
# print(list(range(2,3)))
# when we want to see how much this element appears then we will use count
liste=[1,2,3,3,4]
print(liste.count(3))
# when we want to add the elemnts to the end of the list then we are going to use the extend method
list.extend(liste)
print(list)
# index will return the index which we found that number but when the number is repeated then it is gonna return our first index
print(liste.index(3))
# we have the insert which is used to add an element at the specific position
liste.insert(0,"hyy")
print(liste)
# to change the order with no returning of the new list we use the reverse
liste.reverse()
print(liste)
# to remove the last element we use the pop
liste.pop()
print(liste)
# remove at the specific postion
liste.pop(3)
print(liste)
# sorting element in any order
liste.sort()
print(liste)
# when we want to return in the descending order then we have to make this
liste.sort(reverse=True)
print(liste)
# remove is used when we want to remove element by specifying the value not the index
# here 1 will be removed
# also when the duplicates exists its  going to remmove all of them
liste.remove(1)
print(liste)