def bmi(weight, height):
    #your code here
    bmi=weight/(height**2)
    if bmi <=18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
print(bmi(10,30))    
    