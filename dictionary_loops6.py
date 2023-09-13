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

print(favorite_foods)


for person in favorite_foods.keys():
    print(f"\nHi {person.title()}!")



# same output if written as below, because keys are the default item for listing
# for name in favorite_food:
    #print(name.title())

friends = ['austin', 'hope']

for person in friends:
    food = favorite_foods[person].title()
    print(f"\n{person.title()}, I see you love {food}!")

if 'ty' not in favorite_foods.keys():
    print("\nTy is not my friend!")


print("\n\n\n")

# Looping through keys in particular order
# You can sort through keys as they are returned in a for loop using 
# the sorted function

favorite_dogs = {
    'austin': 'german shepherd',
    'hope': 'pitbull',
    'connor': 'doberman',
    'ty': 'pitbull',
    'root': 'corgi',
}

for name in sorted(favorite_dogs.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.\n")



# Looping through all VALUES in a dictionary
# Can use the VALUES() METHOD to return sequence of values

print("The following dog breeds have been mentioned:")
for dog in sorted(favorite_dogs.values()):
    print(dog.title())
# NOTE that looping through the values requires the .values() method,
# unlike looping through keys, where that can be omitted.



# Looping through Dictionary VALUES WITHOUT REPETITION using a SET
# A SET is a collection in which item must be unique.

print("\nThe following dog poll results were:")
for dog in set(favorite_dogs.values()):
    print(dog.title())

# You can also directly build a set by using braces and separating
# the elements with commas:

cats = {'maine coon', 'persian blue', 'tabby', 'ginger'}
print(cats)

# SETS look similar to DICTIONARIES because they are both wrapped in
# braces. 
# If you see braces but no key-value pairs, it is a set
# Sets do not retain items in a specific order!

