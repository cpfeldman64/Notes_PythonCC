# Looping through a Dictionary
# You can loop through all of a dictionary's key-value pairs, keys, or values.

user_0 = {
    'username': 'cfeldman',
    'first': 'connor',
    'last': 'feldman',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# could also write as 
    # for k, v in user_0.items():
    #   print(f"\nKey: {k}")
    #   print(f"\nValue: {v}")

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.\n")


# Looping through ALL KEYS in a dictionary
# Can use the KEYS() to loop through just the keys

favorite_foods = {
    'connor': 'pancakes',
    'austin': 'jambalaya',
    'hope': 'grapes',
}

for name in favorite_foods.keys():
    print(name.title())

# same output if written as below, because keys are the default item for listing
# for name in favorite_food:
    #print(name.title())


