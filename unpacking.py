# UNPACKING LIST
liste=["mangos","avocado","bananas","orange"]
# fr1=liste[0]
# fr2=liste[1]
# fr3=liste[2]
# fr4=liste[3]

# mangos,avocado,bananas,orange=liste
fst,*others=liste
print(fst)
print(others)

newList=["hey","hellow","guugu","gaga"]
hey,*remain,gaga=newList
print(remain)
print(hey)
print(gaga)
