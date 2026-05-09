thislist=["apple","banana","cherry"]
for x in thislist:
  print(x)


  #you can also use the range and also the len when you want the range of the values in the list
  # when you want the indexes of the given elements then you are gonna need to use the range and the len together

  for i in range(len(thislist)):
    print(i) 


    #if youw ant to get the valuess of those youa re gonna make something like this
  for i in range(len(thislist)):
    # this will print the values at those indexes
    print(thislist[i]) 
# list comprehension in use
  [print(thislist[x]) for x in range(len(thislist))]  