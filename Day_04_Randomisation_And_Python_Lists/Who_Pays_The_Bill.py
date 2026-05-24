## This exercise is to figure out how to pick a random name from the list of friends below to know who pays the bill from a restaurant outing.


import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"] 

# OPTION 1
print(random.choice(friends)) # Better choice, less code.

# OPTION 2
random_index = random.randint(0, 4)
print(friends[random_index])
