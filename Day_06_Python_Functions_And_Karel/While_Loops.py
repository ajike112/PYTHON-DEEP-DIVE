## While loop is a loop that continues going if a particular condition is true, but the loops stops when that condition is no longer true.
## If your While loop continues going and the condition keeps being true, then it becomes INFINITE LOOP.
# while something_is_true:
     # Do this
     # Then do this

# EXAMPLE 1
i = 0
while i < 10:
    print(i)
    i += 1

# EXAMPLE 2
i = 0
while ((i < 10) == True):
    print(i)
    i = i + 1

# EXAMPLE 3 (Iterating backward)

i = 100
while ((i >=0) == True):
    print(i)
    i = i - 1

# EXAMPE 4
x = 2 
while(x < 100000):
    print(x)
    x = x**2
## Example of Infinite Loop

#  while 5 > 3:
    # Do this
    # Then do this
    # Then do this 
    # In this case, 5 is greater than 3, and this function is going to keep executing. Hence, this is infinite loop.