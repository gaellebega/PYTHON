def make_split_join(word):
   sentence=word.split(" ")
   new="-".join(sentence)
   return new
print(make_split_join("his name is Gasana"))