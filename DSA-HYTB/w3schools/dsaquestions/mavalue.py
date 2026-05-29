def findmaxvalue(liste):
  if len(liste)==1:
    return liste[0]
  else:
    return max(liste)
print(findmaxvalue([1,2,5,6,7,3]))  

# using the recursion

def findmaxvalue2(liste2):
  if len(liste2)==1:
    return liste2[0]
  else:
    return max(liste2[0],findmaxvalue(liste2[1:]))
print(findmaxvalue2([80,20,18]))  