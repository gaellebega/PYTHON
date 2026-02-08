n=int(input())
et,ex=list(map(int,input().split()))
current=0
update=0
for number in range(2,1001):
  if et>ex:
    diff=et-ex
    current+=diff
  else:
    current<et
    update=et+current
print(update)   
  

