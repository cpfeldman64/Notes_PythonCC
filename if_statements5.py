# If Statements

# Simple if statements
# if conditional_test:
#       do something!

age = 14
if age >= 15:
    print("You are old enough for a learner's permit!")
    print("Have you gone to driver's ed yet?")
else:
    print("Sorry, you can't drive yet.")
    print("You can go to driver's ed once you turn 15!")

# If the conditional test passes, the first test message prints
# If the conditional test fails, the second test message prints

# IF - ELIF - ELSE Chains\
# If-elif-else chains will pass through one test condition only.
# Not helpful for testing multiple conditions on one 
# single passthrough test.

# Once a variable passes one test, all other tests will be skipped!

age = 12
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $25.")
else:
    print("\nYour admission cost is $40.")

# NOTE that there is a colon after the else, just like the if and elif!
# If test checks one item, if that fails, elif test checks next item,
# if that also fails, it moves to else which is the catch-all for fails.


# There is a more efficient way!

new_age = 67
if new_age < 10:
    price = 0
elif new_age < 18:
    price = 25
elif new_age < 65:
    price = 40
else:
    price = 15
print(f"\nYour cost is ${price}")

# This method sets individual "price" variables inside of 
# the if statement. 

# Omitting the ELSE block
# The else block is not required, you can instead just use an additional
# elif block.

newest_age = 67
if newest_age < 10:
    price = 0
elif newest_age < 18:
    price = 25
elif newest_age < 65:
    price = 40
elif newest_age >= 65:
    price = 15
print(f"\nYour cost is ${price}")

# This is useful for if you need to extra specific about the categories

# NOTE: The else statement is a catchall. It maches any condition that
# wasn't previously matched by an if or elif statement, which could
# potentially include invalid/malicious data.

# TESTING MULTIPLE CONDITIONS WITH IF STATEMENTS

# Using a series of if statements rather than an if-elif-else chain
# can allow you to test a single variable against multiple tests without
# skipping any of them if the variable passes one!

pizza_toppings = ['mushrooms', 'pepperoni']

if 'mushrooms' in pizza_toppings:
    print("\nAdding mushrooms.")
if 'extra cheese' in pizza_toppings:
    print("\nAdding extra cheese.")
if 'pepperoni' in pizza_toppings:
    print("\nAdding pepperoni.")
print("\nFinished with your pizza!")

# subsequent if statement tests are run even if the preceding if statement
# test has been passed!





