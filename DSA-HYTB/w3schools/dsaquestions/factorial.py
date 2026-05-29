def makefactorial(n):
  if n==1 or n==0:
    return 1
  else:
    return n*makefactorial(n-1)
print(makefactorial(5))  
    