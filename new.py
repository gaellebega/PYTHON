def find_palindrome(num):
  if str(num)==str(num)[::-1]:
     print(f"{num} is the palindrome")
  else:
     print(f"{num} is not palindrome")
  return num
print(find_palindrome(404))