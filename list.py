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
del list
print(list(range(2,3)))

