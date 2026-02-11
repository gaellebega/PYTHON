numbers=[1,2,3,4,6]
for index,num in enumerate(numbers):
  print(index,num)

  # list comprehensiion
  # this refers to creation of the new list basing on the existing list
even_numbers=[num for num in numbers if num%2==0]
print(even_numbers)

# here we created the new list basing on the exting list of the mixed up numbers then we are gona create the new list whic only have the evens
evens=[]
for num in numbers:
  if num%2==0:
    evens.append(num)
    print(evens) 

# WHY LIST COMPREHENSION
my_list=[[0]]*5
print(my_list)
# we are giving the commamnd the list to go to the list at 0 index then take an element at 0 index and cahnge it to 1
my_list[0][0]=1
print(my_list)

# why list comprehension
# to create 5 reference elements to the same inner list
# changing one inner list modifies all, as they dhare the same memeory location


numz=[1,2,3,4.5]
numz.copy()
print(numz.copy())
print(numz)