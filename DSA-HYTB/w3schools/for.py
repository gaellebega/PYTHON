mystring="banana"
for x in mystring:
  print(x)

  # the iterator usage
mytuple=("apple","banana","cherry")
  # for myiter in mytuple print myiter
myiter=iter(mytuple)
# we use the next keyword to dispaly the value of the iterables
# the more we use next the more we display item one by one
print(next(myiter))