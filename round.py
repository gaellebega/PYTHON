def longest_prefix(strs):
  prefix=strs[0]
  # while no word start with flower
  for word in strs:
    while not word.startswith(prefix):
       prefix=prefix[:-1]
       if prefix=="":
         return "" 
  return prefix
print(longest_prefix(["list","life","ling","line"]))

