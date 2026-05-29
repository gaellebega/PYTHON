def makefibonacci(n):
# to get evry number you have to take the 2 numbers before it
# the first will be (n-1)and the other will be (n-2)
# the base case
  if n<=1:
    return n
  else:
    # recursive call
    return makefibonacci(n-1)+makefibonacci(n-2)
print(makefibonacci(10))
