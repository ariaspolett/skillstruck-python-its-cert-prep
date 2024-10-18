#Checkpoint - 
name = "Ari"
dogs = 54
location = "Columbia"
print("My name is " + name + " and I have " + str(dogs) + " dogs and live in " + location)
print("My name is",name,"and I have",dogs,"dogs and live in", location)
print(f"My name is {name} and I have {dogs} dogs and live in {location}")

#Challenge - Market List
item1 = "bananas"
item2 = "tomatos"
item3 = "kiwis"
item4 = "onions"
item5 = "apples"
number1 = 16
number2 = 8
number3 = 10
number4 = 6
number5 = 12
print(f"I have bought {number1} {item1}, {number2} {item2}, {number3} {item3}, {number4} {item4}, and {number5} {item5} at the store.")

#Challenge - Sports Scores
soccer = 4
volleyball = 23
basketball = 78
baseball = 24
football = 46
print(soccer, volleyball, basketball, baseball, football)

#Challenge - Favorite Method
method = input("Which method of concatenation is your favorite? + or f or ,?")
if method == "+":
    print("I prefer the " + method + " method")
elif method == "f":
    print(f"I prefer the {method} method")
elif method == "comma" or ",":
    print("I prefer the", method, "method")
else:
    print("this is not a valid method")