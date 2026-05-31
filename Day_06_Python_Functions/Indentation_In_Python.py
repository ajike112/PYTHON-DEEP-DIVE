
## Sample Indentation illustration below:

def my_function():
     print("Hello")
     print("World")
my_function()
# Lines 5 and 6 are dependent on line 4 because they are indented under line 4. Therefore both lines 5 and 6 statement will execute their prints under line 4 

# However if:
def my_function():
     print("Hello")
print("World")
my_function()
# Only line 12 is indented under line 11. Line 13 is not indented under line 11. Therefore, only line 12 will executte its print under line 11. Line 13 will not print or trigger under the function.