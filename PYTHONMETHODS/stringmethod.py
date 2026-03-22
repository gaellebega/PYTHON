name=input()
phone_number="0-3-44"
result=len(name)
# first occurance of the character
result=name.find("O")
#find the last occurance the character
result=name.rfind("O")
# when the index is not find then we have to return -1
result=name.upper()
result=name.lower()
# to check if the number is digit
result=name.isdigit()
# if the name have the the numbers it will turn false
result=name.isalpha()
result=phone_number.count("-")
print(result)