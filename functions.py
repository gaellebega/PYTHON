# to define a function we have to use keyword def
x=0
def function():
  # you will get an error because the variable and the values are inside the scope not outside
   x=20
   print(x)
   return x
x=function()
print(x)

def find(a,b):
   a=a+a
   b=b+7
   return a+b
print(find(10,90))

#