# n=int(input())
# maximum=int()
# for i in range (n):
#   a,b,c=map(int,input().split())
#   row_max=max(a,b,c)
#   if row_max>maximum:
#     maximum=row_max
# print(maximum)    cha

n=int(input())
count=0
for i in range (n):
  a,b,c=map(int,input().split())
  if a%2==0:
    count=count+1
  if b%2==0:
    count=count+1
  if c%2==0:
    count=count+1    
print(count)
  
