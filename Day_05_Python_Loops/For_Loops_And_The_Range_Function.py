
## The combination of the range () function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

## Range function with For Loop

for number in range(1, 11, 3):
    print(number)


##  GAUSS CHALLENGE
# Work out the total of the numbers between 1 and 100, inclusisve of both 1 and 100.

total = 0
for number in range(1, 101):
    total += number # This adds every number in this range to the total starting from 0
print(total)