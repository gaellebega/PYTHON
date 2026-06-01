# the array is special variable that can hold more than one value
car1="volvo"
car2="volvodo"
car4="volvoz"

# cars=["bwm","colola"]
def makecount(cars):
  cars.append("Honda")
  cars.pop(1)
  # cars.remove("volvo")
  cars.count(cars)
  cars.index("Honda")

  return cars
print(makecount(["bwm","colola"]))