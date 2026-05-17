thisisdict={
  "brand":"kia",
  "model":"mustang",
  "year":"1964"
}
print(thisisdict)
#the dupllicates are not allowed
# they are unordered
# the len function is also allowed to the dictionaries
# we are back
# after creating a dictionary varlue can not be changed
# 
# two keys can not have the same name
# to access the values we may use this
# get
x2=thisisdict["year"]
print(x2)
x=thisisdict.get("year")
print(x)
# to get the key elements
x3=thisisdict.keys()
x4=thisisdict.values()
x5=thisisdict.items()
print(x3)
print(x4)
print(x5)

# we use the update when we want to change botht he value and key
thinewdict={
  "name":"igb",
  "age":"nineeteen",
  "location":120
}
thinewdict.update({"name":2020})
print(thinewdict)