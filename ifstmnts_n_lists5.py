# If Statement and Lists
# You can look for special values in a list that need to be treated
# differently from others by the program. You can also manage
# changing conditions (example availability of a menu).

# Can also start proving that code will work in as expected in 
# all situations!

pizza_toppings = ['mushrooms', 'pepperoni', 'pineapple']

for pizza_topping in pizza_toppings:
    if pizza_topping == 'pepperoni':
        print("Sorry, we are out of pepperoni right now.")
    else:
        print(f'Adding {pizza_topping}.')
print("Finished making your pizza!")

# Checking that a list is not empty

farm_animals = []

if farm_animals:
    for farm_animal in farm_animals:
        print(f"\nWow, a {farm_animal}!")
    print("\nSo many animals!")
else:
    print("\nWhere are all the animals?")

# Using Multiple Lists

requested_animals = ['zebra', 'kangaroo', 'giraffe', 'polar bear', 'penguin']
unavailable_animals = ['polar bear', 'penguin']

for unavailable_animal in unavailable_animals:
    if unavailable_animal in requested_animals:
        print(f"\nSorry, it's too hot out for those animals!")
    else:
        print(f"Right this way to their enclosure!")
print("\nAnymore animals you'd like to see?")
# This is sort of a weird double-negative example
# It might have been easier to use "not in" in order to show this one.
# It's a bit confusing, but it still works.

available_tshirts = ['hanes', 'fruit of the loom', 'gap', 'old navy']
requested_tshirts = ['gap', 'hollister', 'old navy']

for requested_tshirt in requested_tshirts:
    if requested_tshirt in available_tshirts:
        print(f'Sure, we have {requested_tshirt} in stock.')
    else:
        print(f"Sorry we don't have {requested_tshirt} in stock.")
print("Any other tshirts you'd like to look at?")
# This example more closely mirrors the one in the book

