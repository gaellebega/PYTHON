
# to access 2 values at the same time we have to use
nums=[1,2,3,4,5,6,7]
for index in range(len(nums)):
  print(nums[index])

for num in nums:
    print(num)

# this will print the both values and the index
for i,num in enumerate(nums):
    print(i,num)


numbers=[1,2,3,4,5]
even_numbers=[]
for num in numbers:
   if num%2==0:
      even_numbers.append(num)
print(even_numbers)
numz=[1,2,3,4,5,6,7,8,9,0]
new_evens=[num for num in numz if num%2==0]
print(new_evens)

# LIST COMPREHESION
# my_list=[0] for_in range