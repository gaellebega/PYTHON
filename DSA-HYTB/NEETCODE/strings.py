# we need to slice inside our sting

s="iamastring"
print(s[0:2])
s+="def"
print(s)
# the strings are immutable to mean you can not modify them
# s[0]="I"
# print(s)

# when you want to add up the stings then you have to use the int
print(int("123")+int("345"))
# this because it is the texts
# by adding the stings to the string then there is no change except the space removal
# add integers together we get the integer as the result 
# adding the stings together we append the string to the other string
print(str("hy")+str("hello"))
print(str(123)+str(456))
print(int(13)+int(12))