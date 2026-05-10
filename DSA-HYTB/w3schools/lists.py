# to change the lsit intems
thislist=["apple","banana","orange"]
thislist[1:3]=["avaocado","toamato"]
print(thislist)

# we use the insert to insert an element at the specific index
# we use the append to append the element at the end of the list

# when you want to add the other liek the sets the dictionary on the list then youw ill gonna need ti use the extend method

newlist=["","","",""]
# if there is more than one element fromt he list then the the pop is used to remove from the specified index\
# remove will remove the first element
# to remove all the elements from the list we use clear

newliste=["uwimana","age","alice","burakari"]
# it removes the element by value
newliste.remove("uwimana")
# it removes the element by index
newliste.pop(2)
# when the pop is used without the psecific elemnt then we are going to get the removing of the last element
del newliste[1]
# when you want the existinf of the list but it being the empty then you are gonna need to use the clear method
newliste.clear()
print(newliste)

# to sort the list we can use .sort method
new=["uwimana","mukamana","angelique"]
new.sort()
print(new)