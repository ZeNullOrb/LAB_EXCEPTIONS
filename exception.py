def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
    

try:
   additoin(10, 20)
except NameError:
    print("the name of the variable is wrong")
else:
    print("the operation is successful")