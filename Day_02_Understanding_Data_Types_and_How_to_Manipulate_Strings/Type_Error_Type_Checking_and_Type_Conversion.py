
# The length function len() is not compatible with integers e.g len(123456789) can't work.
len("Hello")

# To check different data types
print(type("Hello"))

print(type(123))

print(type(123.4))

print(type(True))

# What if we want to convert a piece of data into a different data type?
#Type conversion i.e type casting
# To turn a string into an integer
int("123")

# Addition sign inbetween string'ed number data does not add them up, it rather concatenates them
print("123" + "456")

## Only way to add string'ed numbers is to use the int("") function to convert them to integers.
print(int("123") + int("456"))
