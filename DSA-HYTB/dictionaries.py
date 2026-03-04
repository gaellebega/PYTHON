capital={
  "name":"Rwanda",
  "location":"Africa",
  "citizens":"Rwandans"
}
# to be able to update the dictionary we use update or to change the existing key
capital.update({"location":"EastAfrica"})
# this will add a new key and value
capital.update({"millions":"7"})
print(capital)
# the location is gonna be changed to the east africa
# to remove the key we also use the key
capital.pop("name")
print(capital)
# the popitem will remve the last key and alaos the last value
capital.popitem()
print(capital)
# to clear the whole dictionary we may use
# capital.clear()
# print(capital)
 
keyz=capital.keys()
print(keyz)

valuez=capital.values()
print(valuez)

for key in capital.keys():
  print(key)
for value in capital.values():
  print(value)  
for key,val in capital.items():
  print(f"{key}:{val}")  