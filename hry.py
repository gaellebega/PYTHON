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
# types of strings we have the even length and the other is the odd length
mid=len(k)//2

# print(k[int(mid)]) but the below also the double slash is gonna be the same
print(k[mid])
# print(k[len(k)/2])

# TYPE CONVERSION
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

# FORMATTED STRINGS

p="john"
m=4
msg=p +" has "+  str(m) +" cars"
print(msg)
# keepgoing girl