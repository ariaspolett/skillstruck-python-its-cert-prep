#importing random items in lists
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

#Looking for a specific letter in a list and only transferring the items within the 1st list into the empty list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

