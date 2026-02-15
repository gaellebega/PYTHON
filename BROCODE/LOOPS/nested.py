for x in range(5):
  for y in range (3):
    # formated strings
    print(f"({x},{y})")

    # strings are also iterable
    for x in [1,2,3,4]:
      print(x)