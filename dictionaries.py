# age=my_dictionary=["age"]
# age=my_dictionary.get("age",0)
# print(age)
dictionary_from_list=dict([("name","john"),("age",30),("city","newyork")])
my_new=dictionary_from_list.get("name")
print(my_new)

dictionary_from_list["country"]="Rwanda"
dictionary_from_list["age"]=20
dictionary_from_list["age"]+=30
dictionary_from_list["age"]=dictionary_from_list.get("age",0)+10
dictionary_from_list["location"]="CST"

country=dictionary_from_list.get("country","USA")
print(country)
print(dictionary_from_list)
value=dictionary_from_list.pop("age")
print(value)

print("age" in dictionary_from_list)


# pop removes the element with the specific element

for x in dictionary_from_list:
  print(x)
  # to get both the key and values
for ky,values in dictionary_from_list.items():
  print(ky,values)

for values in dictionary_from_list.values():
  print(values)

another_dictionary=dictionary_from_list
print(another_dictionary)

# to add new age to the dictionary
age=another_dictionary.get("age",30)
print(age)
another_dictionary["name"]="Daniel"
# dictionary copying how it works
print(another_dictionary)
print(dictionary_from_list)

# shallow copying
third_dictionary=dictionary_from_list.copy()
print(third_dictionary)
third_dictionary["city"]="Kigali"
print(dictionary_from_list)
print(another_dictionary)
print(third_dictionary)
dictionary_from_list["members"]=[1,2,3]
print(dictionary_from_list)
print(another_dictionary)
third_dictionary["members"]=[1,2,3]
third_dictionary["members"].append(4)
print(dictionary_from_list)
print(another_dictionary)
print(third_dictionary)