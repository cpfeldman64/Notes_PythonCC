# Simple Dictionaries
# Dictionaries are similar to lists. They allow you to connect pieces of info.
# They can store an *almost* limitless amount of info.

# Alien Dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
# You call for the key category(color) pertaining to a particular
# dictionrary (alien_0) and receive the value associated(green).

# Uses {} with key values inside. key-value pairs separated by a comma.
# Anything can by a key value and the amount you can have is unlimited!
# key-value pairs are just a set of values associated with each other. if you 
# give python a key, it will return with the value.
# dictionary = {key:value, key:value}

new_points = alien_0['points']
print(f'You just earned {new_points} points!')


# Adding New Key-Value Pairs
# Dictionaries are dynamic structures and can be added to at any time

alien_1 = {'color': 'yellow', 'points': 3}
print(alien_1)

alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

# Above adds these key values to the overall dictionary for alien_1
# Dictionaries retain the order that items are added/removed!
# This is important for looping!!

# Starting with an empty dictionary

dog_1 = {}

dog_1['breed'] = 'golden retriever'
dog_1['name'] = 'dillon'

print(dog_1)

# Modifying values in a Dictionary
dog_1 = {'breed': 'corgi', 'name': 'pumpkin'}
print(dog_1)
# You can modify the entire dictionary at once like this
# This way you can also change the order of the dictionary simultaneously

dog_1['breed'] = 'poodle'
dog_1['name'] = 'fletcher'
print(dog_1)
# Or modify individual values by calling and replacing them specifically
# This way will not change the order of the dictionary during modification

# Alien Speed Change Example

alien_2 = {'color': 'blue', 'points': 5}
print(alien_2)

alien_2['x_position'] = 0
alien_2['y_position'] = 25
alien_2['speed'] = 'medium'
print(alien_2)
print(f"Original position: {alien_2['x_position']}")

# Move alien to the right
# Determine how far to move alien based on current speed

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")
# NOTE all of the brackets that must be included for this print statement


# Removing Key-Value Pairs
# can use the del statement to completely remove a key-value pair
# del just needs the name of the dictionary and the key to be removed

alien_3 = {'color': 'orange', 'points': 4}
print(alien_3)

del alien_3['points']
print(alien_3)
# This will remove the key-value without changing the order of the dictionary

