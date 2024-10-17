#Math concepts used from the Python Math Library!!!

#Checkpoint -
import math
w = math.ceil(454.5)
print(w)
x = math.floor(434.2)
print(x)
y = math.sqrt(169)
print(y)
z = math.pow(2, 24)
print(z)

#Challenge - Biking Town
import math
num_ppl = int(input("How people live in this town?"))
num_bike = int(input("How many bikes in the town?"))
pplperbike = math.ceil(num_ppl/num_bike)
print("In this town, for every bike that exists there are " + str(pplperbike) + " people.")

#Challenge - Cube Volume
import math
lengofsidecube = int(input("enter the length of a side of the cube."))
volume = int(math.pow(lengofsidecube, 3))
print(volume)

#Challenge - Is it a Good Investment?
import math
value_of_stock_starting_x = int(input("Enter a value"))
value_of_stock_ending_y = int(input("Enter a value"))
div = value_of_stock_ending_y/value_of_stock_starting_x
square = math.sqrt(div)
sub = square - 1
total = round(sub, 2)
print(total)

#Challenge - Right Triangle