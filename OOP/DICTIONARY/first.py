#  my first dictionary
data={"name":"jane","age":20}
print(data)

# creating the dictionary
dictionary2=dict(a="my",b="name",c="is",d="uwimana")
print(dictionary2)

print(dictionary2["b"])
print(dictionary2["c"])

# ADDING AND UPDATING ITEMS

# adding new key value pair
dictionary2["e"]="home"

# updating an existing value
dictionary2["a"]="home is"
print(dictionary2)

del dictionary2["e"]
print(dictionary2)

new_remove=dictionary2.pop("a")
print(new_remove)

key,val=dictionary2.popitem()
print(f"key:{key},value:{val}")


