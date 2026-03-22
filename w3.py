print("Hello",end="")
print("I will come on the same line")
# when we want to print to the same linw


print("I an only", 25," years old and i work in GOOGLE")

# unapck the list
fruits=["banana","cherry","apples","oranges"]
print(fruits[0])
print(fruits[1])
# error cz too many values to unpack
# y,z=fruits
# print(y)
# print(z)
x,y,z,w=fruits
print(x)
print(y)
print(z)

a=b=c="Hello world"
print(a)
print(b,end="")
print(c,end="")
# you can not add integer witht hte string it will throw an erro
# m=2
# n="hey"
# print(m+n)

# Global varibales
# these are the variables created out of the function

k="awesome"
def myfunc():
  print("Python is:"+k)
myfunc()  
# when you wanna make the local varibale become the gloabl varibale you have to use the grobal keyword


g=my_g
def myfunction():
  global g
  
