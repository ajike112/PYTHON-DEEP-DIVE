
## The objective of this task is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How manny letters would you like in your password?\n"))
nr_symbols = int(input(f"How manny symbols would you like?\n"))
nr_numbers = int(input(f"How manny numbers would you like?\n"))

# Easy version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants 4 letters, 2 symbols, and 3 numbers.

password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)


# Hard version
# If your hacker knew that you always have two symbols at this position and 2 numbers at this position, then it is very easy to crack that password. To tackle that, we are going to write the code on how to get the password that hass all of the letters and numbers in a completely random order.
# How to tackle this is that, instead of adding the letters to a string "", they would be added to a list.

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

# How can we shuffle our list? how can we mess up the order of the items in our list?

random.shuffle(password_list)
print(password_list)

# How do we turn the password back to a string "" ?
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")