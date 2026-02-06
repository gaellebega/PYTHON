# we use lambda when you need a small function for a short time like inside map, filter sorted() methods

nums=[1,2,3,4,5,6]
square=list(map(lambda x:x**2,nums))
print(square)

is_even=lambda x:x%2==0
print(is_even(4))
print(is_even(7))

make_double=lambda x:x*x
print(make_double(2))