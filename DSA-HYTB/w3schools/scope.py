# the variable is only available from the region to which is created which is well know as the scope
# the nonlocal keyword can be used when we want to make the grobal variable become the local

def myfunc():
  x="Jane"
  def func2():
    nonlocal x
  func2()
  return x
print(myfunc())
  
def anotherfunc(x):

  global name
  name="mukesha"
  return x
print(anotherfunc("uwimana"))
print(name)


