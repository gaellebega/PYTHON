# EXCEPTION
try:
     def quot(a,b    ):
        return a//b
     

     x = int(input("Enter the first number:"))
     y = int(input("Enter the second number:"))

     print(quot(x,y))
     # anything without the exit code 0 means the program crashes
except  ValueError:
    print("inavlid Input")  
except ZeroDivisionError:
    print("Error:Can not not didvide by zero")
    # if you dont know the type of the error to face and you dont wanna the program to crash then this is all you can do

except :
    print("something went wrong:(")