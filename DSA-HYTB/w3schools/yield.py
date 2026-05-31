# you can use the yield in python instead of just using the normal return
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)
