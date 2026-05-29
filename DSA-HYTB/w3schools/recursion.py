# the recursion meaans when the function is calling itself
def countdown(n):
  if n<=0:
    print("Done")
  else:
    # print(n)
    countdown(n-1)
    print(n)
countdown(4)
