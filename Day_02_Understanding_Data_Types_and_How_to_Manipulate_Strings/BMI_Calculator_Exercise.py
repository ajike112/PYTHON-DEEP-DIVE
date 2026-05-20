
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# BMI is equal to the person's weight divided by the person's height squared.
# Convert this sentence into lines of code and calculate BMI.

# SOLUTION
height = 1.65
weight = 84
BMI = (weight / (height) ** 2)
BMI = (84 / (1.65) ** 2)
# Introducing round() function to round up possible floating data type number answer 
print(round(BMI))

# If you want to round to a desired floating number (decimal places)
print(round(BMI, 2)) # Where 2 is the number of decimal places in this case

