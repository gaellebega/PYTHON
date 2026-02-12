nums=(1,2,3,4,5)
num_1,num_2,*others=nums
print(num_1)
print(num_2)
print(*others)
num=(4,)
print(nums+num)
# can we delete the element on a tuple?
print()
# num=(4,) this is also the tiple bcz it is 
# we may need the tuples to use them as the keys
n=int(input())
arr=list(map(int,input.split()))
arr=list(set(arr))
arr.sort()
print(arr[-2])

n = int(input())
arr =map(int, input().split())
arr.sort()
if arr[-2]!=arr[-1]:
  print(arr[-2])
