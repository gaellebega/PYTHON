# the recursion means when the function is calling itself
def countdown(n):
  # BASE CASE: CONDITION that sops the function
  if n<=0:
    print("Done")
  else:
    # print(n)
    # RECURSIVE CASE: EVERY UTPUT AFTER THE RECURSION like the output after function called itself with a changed value
    countdown(n-1)
    print(n)
countdown(4)
