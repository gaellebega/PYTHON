# DICTIONARIES 
car1={
  # key: value
  "name":"Rambo",
  "model":"Mushtang",
  "mil":20
  
}
# heterogenus examples
my_dist={
  "name":"uwimana",
  1:[10,20,30],
  "age":20,
  True:"Yes",
  3.14:{"pi":3.14}
}
print(my_dist)
# example of the enconding 
endc = {
  # mapping of the key to the values
  1:"a",
  2:"b",
  3:"c"
}
# similar to list to access the key  is done in 2 ways 
# print(endc.get(1)but this only get the element at the specific index but can not mody it
print(endc.get(2))
# by this you can change the values
endc[1]="A"
print(endc)

del endc[3]
print (endc)

# UNPACKING
# assigning the values witht the keys
value1,value2 = endc.values()
print(value1,value2)

# assigning valiables with the the values
value2,value2 = endc.values()
print(value1)

# assign the whole key-pairs variables we use .items()
a,*b=endc.items()
print(b)