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
# the update  can be used to add new item or change the exist values
thinewdict.update({"nameq":"sandrine"})
thinewdict.update({"name":2020})

print(thinewdict)

# we use the pop method when we want to remove the leemnt at the specific key name
thisdel={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdel.pop("model")
print(thisdel)

# the popitem is used to remove the last inserted item

thisdel.popitem()
print(thisdel)
# the del will be used to delete the complete dictionary
# also the clear is used to make the dictionary empty
# learning along the way

# loop through dictionary
# in py we have the nested dictionaries

my_fam={
  "myparents":{
"names":"uwimana",
"secondname":"marie"
  },
  "theirparents":{
"name":"john",
"location":"kigali"

  },
  "hisparents":{
"date":"12",
"district":"karongi"
  }
}
# to access the values of the nested dicitionary
print(my_fam["hisparents"]["date"])
print(my_fam)