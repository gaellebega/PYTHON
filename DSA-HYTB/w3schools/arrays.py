# the array is special variable that can hold more than one value
car1="volvo"
car2="volvodo"
car4="volvoz"

# cars=["bwm","colola"]
def makecount(cars):
  cars.append("Honda")
  return cars
print(makecount(["bwm","colola"]))