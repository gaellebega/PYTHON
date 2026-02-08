# def find_palindrome(num):
#   if str(num)==str(num)[::-1]:
#      print(f"{num} is the palindrome")
#   else:
#      print(f"{num} is not palindrome")
#   return num
# find_palindrome(404)

# def new_function():
#    n=int(input())
#    new=[]
#    for n in range (0,n) :
#       new.append(n*n)
#    return new
# print(new_function())

# def new_func():
#    n=int(input())
#    new=[]
#    for i in range (0,n):
#         new.append(i*i)
#    return new
# for sq in new_func():
#       print(sq)
# print(new_func())      













def convert_tofrhein(celsius:float):
   #  farheinheight=(celisius*5/3)+32
   # kelvin=celsius+273.15
   kelvin=celsius+273.15
   fahrenheit=celsius * 1.80 + 32.00
   # kelvin=celsius+273.15
   return[kelvin,fahrenheit]
print(convert_tofrhein(12.5))    

