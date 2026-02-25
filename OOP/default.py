from collections import defaultdictionary
d=defaultdictionary(int)
l=[1,2,3,42,4,1,2]
for i in l:
  # [1:1,2:1,3:1,4:1]
  d[i]+=1
print(d)  
