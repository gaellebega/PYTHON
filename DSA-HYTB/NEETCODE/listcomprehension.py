nums=[1,5,7,3,4]
new=[]
for x in nums:
   new.append(x*x)
print(new)

squares=[x*x for x in nums] 
print(squares) 

arr=[i for i in range(5)]
print(arr)