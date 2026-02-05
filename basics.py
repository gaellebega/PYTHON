def printName(name):
  return name
print(printName("Ishami Gaelle  Bega"))

def calculateInt(a,b):
  return a//b
print(calculateInt(7,3))

#BODMAS

Y=(2+3+2+3*6)
print(Y)

def solve_problem():
  array=[1,2,3,4,5]
  no=array
  no=40
  n=no
  if n in array:
    return True
  else:
    return False
print(solve_problem())


greetings="Hello, World"
print(greetings[2:5])
# decrement
print(greetings[5:2:-2])
print(greetings[3:2])

name="uwimana"
age=12
print(f"hello my name is {name} am {age} year old")

a=1
b="hello"
print(f"{b} {a+2}")

print("Hello" in "Hello World")


def make_palindrome(num):
 if str(num) == str(num)[::-1]:
   print("this is a palindrome")
 else:
     print("this is not a palindrome")
 return num
print(make_palindrome(101))

