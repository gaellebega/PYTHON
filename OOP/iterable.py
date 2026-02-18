# iterable is the built-in method 
my_tuples=("apple","banana","cherry")
my_iter=iter(my_tuples)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))

# GENERATOR
# printed when the next is called
# help us to create a functin that is iteraable


# COOLECTIONS AND 
# with generator
def squares_num(nums):
   for i in nums:
      yield i*i

my_nums=squares_num([1,2,3])
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
