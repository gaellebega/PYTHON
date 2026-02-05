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