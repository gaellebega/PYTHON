n=int(input())
# ["uwimana", 20]

new_store=[]

# a,b=list(map(int,input().split()))
for _ in range(n):#n=2 1
  name=input()
  grades=float(input())
  new_store.append([name,grades])
print(new_store)
# for i in new_store:
#   print(i)
for i,j in enumerate(new_store):
  print(j[0])
  print(j[1])