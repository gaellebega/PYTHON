def my_function():
  print("this is the python function")
my_function()  
my_function()
my_function()
my_function()
# info passed into the function are called the arguments
def nameslist(fname):
  print("my name is "+fname)
  # the real value of the variable is called the parameter
nameslist("Uwase Sangwa")  

# the arbitary arguments
# it is used when we dont know the number of the the argummets that we are going to use

def makesum_numbers (*numbers):
  return sum(numbers)
print(makesum_numbers(1,2,3))
print(makesum_numbers(1,2))