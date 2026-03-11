def easy_solution(arr1,arr2):
  
  # O(nlogn)
  # O(m+n) when one m is the size of one array and the other is the size of the other array
  unique=sorted(set(arr1+arr2))
  return unique
print(easy_solution([1,2,3,1],[3,2,7,9]))