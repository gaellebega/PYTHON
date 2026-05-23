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

# without the *args
# this will work only for the 2 numbers but whenw e have the alot fo the
#  numbers thenw e need to make it like the above
def add(*values):
  return sum(values)
print(add(2,3))
print(add(9,2))


def myanotherfunc(*args):
  print("first argument",args[0])
  print("second argument",args[1])
myanotherfunc("Tobias","linus","emilc")  
  
def useargs(greeting,*names):
  # this will go will the number of the names which are 2 then index are 0,1
  for name in names:
    print(greeting,name)
useargs("Hello","Uwimana","Tobias")   
