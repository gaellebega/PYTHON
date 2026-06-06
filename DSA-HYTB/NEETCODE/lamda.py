# when we want to make the normal sort

nums=[90,23,45]
nums.sort(key=lambda x:x)
print(nums)


# to sort by the second element
# this is going to compare the all second elements
students=[("Uwimana",10),("Mukamana",90),("Solange",70),("kamanzi",2)]
students.sort(key=lambda n:n[0])
print(students)

# to sort by the size from small to the greatest
size=["alice","aline","gahongayire"]
size.sort(key=lambda x:len(x))
print(size)


liste=[("first",20),("second",30),("third",40)]
liste.sort(key=lambda x:x[0])
print(liste)