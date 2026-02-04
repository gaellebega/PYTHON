# BASICS ON PYTHON

x=5
print(x)

name="uwimana"
print (name)
# no matter the input that you are taking is gonna come as the string
# y=int(input("enter your number:"))
# print(type(y))

print("Hello Programmer this is your journey in python coding!")
# using the plus sign is an option
print("Helloo"+"world")
print('''hello
world
welcome here''')

# complex numbers they work with the

z = complex(3,5)
print(z.real)

b = complex(1,2)
print(b.imag)

# STRING METHODS

t="this is It"
m="GOODMORNING"
print(t.islower())
print(m.isupper())
print(t.upper())
print(t.replace("t","m"))
# the swap case is used to change like the smaller become th capital and the small become the big letters
print(t.swapcase())
# this will only capitalize the capital letter
print(m.capitalize())
# it is gonna return -1 when it is not there
print(m.find("k"))
# it will return the index of the first occurence word
print (m.find("O"))
# if you don't want the  only  first occurance you need the opposite you have to use this
print(m.rfind("D"))
# this is gonna tell you how many number of the word has repeated
print(m.count(m))

a=["apples","managos","bananas"]
# with the boolean data types you have to use the True and False also the small rule is the first letter must be capitalised and the rest not
# list must be ordered but not same as the set have all types of the data

k=input("Enter a String:")
# types of strings we have the even length and the other is the odd length the //means divide then return thr integer
mid=len(k)//2

# print(k[int(mid)]) but the below also the double slash is gonna be the same
print(k[mid])
# print(k[len(k)/2])

# TYPE CONVERSION IN PYTHON

# implicity type conversion the python changes the type for our selves to avoid the erros
x=2
y=4.4
# python automatically changes the x to the float so as to avoid the errors
z=x+y
print(type(z))
# explicity you yourslef you are only one who is gonna change the type of the variables
x="3"
y=int(x)
print(type(y))
z=int(z)
print(type(z))

# FORMATTED STRINGS IN PYTHON

p="john"
m=4
msg=p +" has "+  str(m) +" cars"
print(msg)
# you have to use f to print using what is in the curry braces
print(f'''John 
has {m} cars.''')

# ARITHEMATIC OPERATIONS IN PYTHON

# +,-,/,%,**,//
num1=4
num2=5
# exponential sign to mean power sign
print (num1*num2)

# Precedence Operators in python
# means if we got more than one operator then which one are we gonna perform first

print(2+2*9-1)
"""
P: Parentheses ()
B: Exponentiation **
U: Unary operators +x, -x, ~x
M: Multiplication, Division, Floor Division, Modulus *, /, //, %
A: Addition and Subtraction +, -
S: Bitwise Shifts <<, >>
B: Bitwise AND &
X: Bitwise XOR ^
O: Bitwise OR |
C: Comparisons ==, !=, <, <=, >, >=
N: Logical NOT not
A: Logical AND and
R: Logical OR or

"""
import math
x=30.4
print(round(x))

# absolute value used to return the positive number
x=-12.3
print(abs(x))
print(math.pi)
print(math.sqrt(12))
#goes up by rounding
print(math.ceil(55.5))
# goes down by rounding
print(math.floor(1.23))
print(math.factorial(6))
print(math.gcd(1,3))
print(math.sin(90))
print(math.cos(0))
print(math.e)
# tau means pi x pi like 2pi
print(math.tau)
# angle conversion
print(math.degrees(3.14))
# changing to radians from degrees
print(math.radians(180))
# CONDITIONAL STATEMENTS

# if statement
age = 3
if age > 90:
   print("you are so old")
elif age == 10:
   print ("you are some how young")
else:
   print("you are in the middle")
      
citizenship='Rwandan'   
# country=input("hey enter you orgin")   
if citizenship :
   print("You can vote")
else:
   print("go in diaspora")   

# Comparision operators
l=9
g=10
if l==2 and g==10:
  #  when the condition is true
   print("this is the big false") 
elif g != 1:
   print("yeah value of g is not equal to 10 ")

  #  LOOPS
for a in range(6,8):
     print(a)

nums=[1,2,3,4,5]
for i in nums:
   print(i)

v=5
while  v < 10:
   print("hi")
   v = v+1  

  #  the break when it is used then we have to  ignore everything that is below it

zepa=6
while zepa<4:
  for i in range(zepa):
     print(zepa)
  break
  zepa=zepa+1
print ("we are done")

for i in range (zepa):
  #  to mean skip when you reach here
  # also everyhting that is prited after will not be seen there
   if i==4:
      # when we have used something called pass it means when you reach to the situation matching with pass then act as nothing hapened like work normal
      continue 
   
   else:
      print(i)

n = int(input("Enter any number:"))
for k in range (n):
   for j in range (1,n-k + 1):
      # this is used when you want to end witht the space 
      print(j, end=' ')
   print() 

