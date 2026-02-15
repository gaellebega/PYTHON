# we use the loop to create the repetition

# syntax
# wegot a builtin function called range()
# this will make the print of index
for i in range(3):
  print(i)
print()
# this will make print of the real nums
for number in range(1,4):
  print(number)
print()
  #we may also use the step
for n in range(1,10):
    s="*"*n
    print(s.ljust(n)) 
    print() 
success=False
for k in range(3):
   print("attempted")
   if success:
      print("you are in")  
      break
else:
     print("attempted 3 times")