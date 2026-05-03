def check_temp(value):
  if (value>=50):
    return "No"
  elif 60>= value >=30:
    return "Warm"
  else:
    return "Cold"

cities={"Gasabo":32,"kicukiro":20,"nyamata":10}
# key:expression for (key,values) in iterables
cities={key:(val-32)*(5/9) for key,val in cities.items()}
print(cities)

desc_cities={key:check_temp(value) for key,value in  cities.items()}
print(desc_cities)