# nums=list((1,2,3,4,5,6)) 
# print(type(nums))
# numberz=[10,11,12,13,14,15,16,17,18,19,10]
# # print(numbers[0:-1:2])
numbers= [1,2,3,4]
# numbers.insert(0,10)
# numbers.remove(0)
# on the pop remove the element based on the index but when none is specified then we are gonna remove the last one
# remove works witht the value and not retutning the removed value
# pop will return the removed value which means we can re use it pop have the return statement it will give the removed statement

print(numbers)

mylist=[1,2,3,4,5,6]
ispresent=2 in mylist
print(ispresent)


# SORTING
# inline cz it doesnt return the new array but it use what it already have
# inplace changing the position without creating the new list so we will not need the retun or the print and the function of sort inside
nums=[0,-1,2,-5]
nums.sort()
print(nums)
sorted_items=sorted(nums,reverse=True)
print(sorted_items)

# we can use the lamda 
grades=[[4,10],[2,9],[3,8]]
sorted_grade=sorted(grades,key=lambda i:i[-1],reverse=True)
print(sorted_grade)
sorted_grade=sorted(grades,key=lambda i:i[1])
print(sorted_grade)
# this will we the sorting of the id 
sorted_grade=sorted(grades,key=lambda i:i[0])
print(sorted_grade)

num1=[4,5,2,6,0]
num2=[5,6,0,8]
# append is gonna add on one element to the list but the list its gonna take all the list and make them one
print(num1+num2)
num1.extend(num2)
print(num1)

# insert take the index and the value

# traverising lists

