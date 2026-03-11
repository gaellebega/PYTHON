# the normal sort work from the ascending to the descending order
# when you want to change that you have to use .sort(reverse="true")
# witht he matrix python willl compare the first elements like at the index[0]
matrix=[["d","y","n"],
        ["c","x","o"],
        ["a","x","p"]]
matrix.sort()
print(matrix)
# when they start with the same items then pythin will check the next item 
# when you want to be specific you can write
matrix[1].sort()
print(matrix) 