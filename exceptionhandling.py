# EXCEPTION
try:
     def quot(a,b):
        return a/b
     

     x = int(input("Enter the first number:"))
     y = int(input("Enter the second number:"))

     print(quot(x,y))
    # anything without the exit code 0 means the program crashes
except  ValueError:
    print("inavlid Input")  