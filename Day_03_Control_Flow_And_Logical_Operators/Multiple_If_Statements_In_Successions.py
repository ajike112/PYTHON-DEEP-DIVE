# You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:
# If/elif/else

#if <condition 1 is true>
#    <do A>
#elif <condition 2 is true>
#    <do B>
#else
#    <do C>

# Nested if statements
#if <condition 1 is true>
#    <do A>
#    if <condition 2 is true>
#        <do B>
#        if <condition 3 is true>
#            <do C>

# EXAMPLE
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


