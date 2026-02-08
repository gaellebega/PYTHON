# def make_multiples(num):
#   a=num[0]
#   new=[]
#   for n in num:
#     c=n*a+1
#     new.append(c)
#   return new
# print(make_multiples([1,2,3]))

def make_multiple(num,count=4):
  multiples=[]
  for i in range(1,count+1):
   multiples.append(num*i)
  # return multiples
  smallest_even=None
  for m in multiples:
    if m %2 == 0:
      smallest_even=m
      break
  return multiples,smallest_even
print(make_multiple(8))

