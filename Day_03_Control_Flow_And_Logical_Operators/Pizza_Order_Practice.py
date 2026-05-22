
## PIZZA ORDER PRACTICE
# Congratulations, you have got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill. Use the input () function to get a user's preferences and then add up the total for their order and tell how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2

## SOLUTION
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pay = 0

# to do: work out how much they need to pay based on their size choice
if size == "S":
   pay = 15
   print("Small pizza(S): $15")
elif size == "M":
   pay = 20
   print("Medium pizza(M): $20")
elif size == "L":
   pay = 25
   print("Large pizzza(L): $25")
add_pepperoni_for_small_pizza = input("Do you want to add pepperoni for small pizza? Y or N")
if add_pepperoni_for_small_pizza == "Y":
# Add $2 to the pay
  pay +=2
add_pepperoni_for_medium_or_large_pizza = input("Do you want to add pepperoni for medium or large pizza? Y or N")
if add_pepperoni_for_medium_or_large_pizza == "Y":
# Add $3 to the pay
  pay +=3
add_extra_cheese_for_any_size_pizza = input("Do you want to add extra cheese for any size pizza? Y or N")
if add_extra_cheese_for_any_size_pizza == "Y":
# Add $1 to the pay
  pay +=1
print(f"Your final pay is ${pay}")
