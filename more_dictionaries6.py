# Dictionaries Continued
# Dictionaries of Similar Objects

favorite_languages = {
    'connor': 'python',
    'hope': 'rust',
    'austin': 'c',
    'josh': 'python', 
}
# It is good practice to leave a comma at the end of the last value in case
# you add another value to the dictionary in the near future

language = favorite_languages['connor'].title()
print(f"Connor's favorite language is {language}.")
# Assigning a fresh variable to the dictionary key-value to be called
# simplifies the print call considerably.

# Using GET() METHOD to Access Values

pizza_1 = {'crust': 'thin', 'topping': 'sausage',}
print(pizza_1['topping'])

second_topping = pizza_1.get('topping_2', 'Just one topping.')
print(second_topping)

# Will print topping_2 value if it is added to the dictionary and called, or 
# will print requested message if has not been added to the dictionary and
# is called.

