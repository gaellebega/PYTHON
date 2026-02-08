numbers=int(input())
current=0
max_capacity=0

for _ in range(numbers) :
 ex,et=map(int,input().split())
 diff=et-ex
 current+=diff
 if current>max_capacity:
    max_capacity=current
print(max_capacity)   
