# we use while loop to execute as long as the condition is true
i=6
while i<2:
  print(i)
  i+=1
  # when we want to end that condition which is true then we use the break statement

  m=3
  while m<9:
    print(i)
    if m==2:
      break
    i+=1
print("this is it")

# the continue statement
i=8
while  i<6:
  i+=1
  if i==2:
    continue
  print(i)

  # you can also use the while with the else

  a=1
  while a<3:
    print(a)
    a+=1
  else:
    print("a is no longer less than 6")