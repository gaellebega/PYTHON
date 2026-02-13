import copy

dictionary1={"name":"John","age":30,"city":"NewYork"}
dictionary1["members"]=["1,2,3"]
# print(dictionary1)
dictionary2=dictionary1
dictionary3=dictionary1.copy()
dictionary2["age"]=50
print(dictionary1)
print(dictionary2)
print(dictionary3)

dictionary2["members"].append(4)

print(dictionary1)
print(dictionary2)
print(dictionary3)

dictionary4=copy.deepcopy(dictionary1)
print(dictionary4)

