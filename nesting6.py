# Nesting
# Nesting is the action of storing multiple dictionaries in a list, or of 
# storing a list of items as a value in a dictionary
# Nest dict inside list, list inside dict, or dict inside dict

dog_1 = {'breed': 'doberman', 'name': 'jack'}
dog_2 = {'breed': 'golden retriever', 'name': 'dillon'}
dog_3 = {'breed': 'corgi', 'name': 'pumpkin'}

dogs = [dog_1, dog_2, dog_3]

for dog in dogs:
    print(dog)

# Dictionaries in Lists


# Empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# Make first three aliens turn yellow through game progression
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'


# Show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show all aliens created
print(f"Total number of aliens: {len(aliens)}")



# NOTE: If you are going to includes multiple dictionaries in a list, they
# need to all have the same exact structue (even if different info) in order
# to properly use loop functions

# Lists in Dictionaries

# Store pizza info

pizza = {
    'crusts': ['thick', 'thin'],
    'toppings': ['pepperoni', 'goat cheese', 'olives'],
}
# Be sure to put commas between dictionary items, even if the items are lists

# Summarize the order
for crust in pizza['crusts']:
    print(f"\nYou ordered a {crust}-crust pizza "
          "with the following toppings:")
    for topping in pizza['toppings']:
        print(f"\t{topping}")

# If you need to break up a long line in a print() call, choose an appropriate
# point to break the sentence and end that line with a " mark. Then, indent
# the next line, open with a new " and continue the string. Python will know
# to combine these strings into one.

# Looping through multiple values assigned to one key in a dictionary

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
# Note how the value languages in used in the second for loop after being
# created in the first.

# Also note the use of len(languages) to judge number of items in list.

# nice!

# DO NOT NEST LISTS AND DICTIONARIES TOO DEEPLY. The amount of nesting above
# is all that is really necessary. If too much nesting is occurring, there is
# probably actually a simpler way.

# Nesting Dictionaries in Dictionaries
# Be careful, because the code can quickly become complex

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# I like this one. It feels useable for a lot of applications.
# This works well because the value-dictionaries have identical structures. If 
# they did not, the for loops would likely be a lot more complex.


