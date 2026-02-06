def make_double(nums):
  doubles=[]
  for n in nums:
    doubles.append(n*n)
  return  doubles
print(make_double([1,2,3]))


def make_palindrome(word):
    if word == word[::-1]:
     print(f"{word}is a palindrome")
    else:
     print(f"{word} is not a palindrome")  
    return word
make_palindrome('MOM')

def separate_evens(nums):
  new_evens=[]
  for n in nums:
    if n%2 ==0:
      new_evens.append(n)
  return new_evens
print(separate_evens([1,2,4,5,8,9,0]))


def filter_nums(nums):
   brand=[]
   for n in nums:
     if n%2 == 0:
      brand.append(n)
   return brand
print(filter_nums([9,8,2]))


def ame_sum(nums):
  tot=0
  for n in nums:
    tot=tot+n
  return tot
print(ame_sum([1,2,3,4]))

def make_max(nums):
  big=nums[0]
  for n in nums:
    if n> big:
      big=n
      print(f"{big} is the largest")
  return big
print(make_max([8,10,4,5,60]))    

def find_biggest(numbers):
  return max(numbers)
numbers=[1,2,3,4,6,7]
print(find_biggest(numbers))

