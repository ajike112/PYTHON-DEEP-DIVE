

## When you combine two different conditions using AND operator, they both hae to be True for both A and B for the entire line of code to be True.
# If A is True and B is False, then it is False
## If A is False and B is True, then it is False
## If A is True and B is True, then it is True

## Or operator is used if I only need one of the conditions to be True.
# if C or D were True, then it is True
# if both C, D were True, then it is True
# It is only when both C, D are False that both statements are False.

## The "NOT" operator basically reverses a condition.
# If a condition becomes False, then it becomes True.
# If a condition becomes True, then it becomes False.


# EXAMPLE 1
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55: # same as elif 45 <= age <= 55
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
       #Add $3 to thier bill
       bill = bill + 3 # this is the same as bill +=3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


# EXAMPLE 2
a = 5
b = 7
 
if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")