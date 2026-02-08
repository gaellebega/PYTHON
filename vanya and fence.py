# the number and the height of people
n,hf=map(int,input().split())
# the height of the people
h=list(map(int,input().split()))
width=0
for person_height in h:
   if person_height>hf:
    width=width+2
   else:
    width=width+1
print(width)

