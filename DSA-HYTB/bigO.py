# Big O notation is used to measure how running time or space requirements for your program grow as the size of input size grows
# as the size grows the time also grows
# size(arr)=>100 time=>0.22ms
# size(arr)=>1000 time=>2.44ms


# squared numbers
def square_numbers(numbers):
  doubles=[]
  for n in numbers:
    doubles.append(n*n)
  return doubles
print(square_numbers([1,2,3]))
  

def even_numbers(nums):
  new_evens=[]
  for n in nums:
     if n % 2 == 0 :
       new_evens.append(n)
  return new_evens
print(even_numbers([1,2,3,4,5,6,7]))




def return_sum(numb):
  total=0
  for n in numb:
    total=total+n
  return total
print(return_sum([1,2,3]))


# def find_large(numz):
#   big,*others=numz
#   for big in numz:
#     if big > numz[others]:
#   return big
# print(find_large([1,9,0,4,3,3]))

def find_large(numbers):
  big=numbers[0]
  for n in numbers:
    if n> big:
      big=n
  return big
print(find_large([90,100,5,3,1,4]))


def odd_appearence(numz):
  c=0
  for n in numz:
    if(n%2!=0):
      c+=1
  return c
print(odd_appearence([1,2,3,413,16,17,9,0]))


# make sort in the descending order
def reverse_list(nums):
  nums.sort(reverse="true")
  return nums
print(reverse_list([1,2,12,5,0,3]))

# make revrsign a reverse
def reverse_list(nums):
  nums.reverse()
  return nums
print(reverse_list([9,0.2,5,6]))

# slice to reverse
def make_reverse(nums):
  new=nums[::-1]
  return new
print(make_reverse([3,5,6,7,88]))
   
def find_totals(numbers):
  tot=0
  for n in numbers:
    tot+=n
  return tot
print(find_totals([10,2,3,5,9]))


def greater_n(liste,num):
  result=[]
  for n in liste:
      if n>num:
       result.append(n)
  return result
print(greater_n([1,2,3,9,8],num=1))

# find duplicate

def find_duplicate(nums):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if(nums[i] == nums[j]):
       return nums[i]
      
print(find_duplicate([1,2,3,4,6,6,7,0]))
     
#  find the duplicate when they are more than one element

def find_all_duplicate(nums):
  seen=set()
  duplicates=set()
  for n in nums:
    if n in seen:
      duplicates.add(n)
    else:
      seen.add(n)
      # convert set to list
  return list(duplicates)
print(find_all_duplicate([1,2,2,4,5,6,7,7,8]))
