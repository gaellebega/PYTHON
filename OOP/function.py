class Human_being:
  # method of the obj
  def __init__(self,property1,property2):
    self.property1=property1
    self.property2=property2
    
    # method of the obj
  def read(self):
    return f"all the properties are{self.property1 } and{ self.property2}"
newob=Human_being("Head","Chest")  
print(newob.read())

# constructor is the func when object created 