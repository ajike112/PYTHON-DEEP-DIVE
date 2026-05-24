
import random
random_number_0_to_1 = random.random()
# random_number_0_to_1 = random.random() * 10 # by multiplying by 10, random numbers to be generated are now from 0 to 10.
print(random_number_0_to_1)

import random
random_Heads_or_Tails= random.randint(0, 1)
print(random_Heads_or_Tails)
print("Heads")
print("Tails")

import random
random_Heads_or_Tails = random.randint(0, 1)
if random_Heads_or_Tails == 0:
    print("Heads")
else:
    print("Tails")