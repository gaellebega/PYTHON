def makesum(numbers):
  # base case
  if len(numbers)==0:
    return 0
  else:
    # recursive call
    return numbers[0]+makesum(numbers[1:])
print(makesum([1,2,3,6,7,8,9]))  
  