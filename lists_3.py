# A list is a collection of items in a specific order
# These items don't have to be related
# Ex the letters of the alphabet
# Usually named as a plural, Ex: letters
# [] are used to indicate a list, with individual elements
# separated by commas

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# This would print ['trek', 'cannondale', ... ] 
# which is not ideal

# Instead
# You can access any element of a list by telling Python
# the position, or INDEX, of the item desired
# To accesss an element of a list, write the name of the list
# Followed by the index of the item in []
# NOTE: INDEX positions start at 0, not 1 

print(bicycles[0])
# Will print trek

print(bicycles[0].title())

# You can print the last item in the list by calling -1
# This is helpful if you don't know the exact length of a list

print(bicycles[-1].title())

# If you call index -2 it will be the second item from the end
# -3 is third item from the end and so on

print(bicycles[-2].title())





# You can include an individual value from a list in a message

message = f"\nMy first bicycle was a {bicycles[0].title()}!\n"
print(message)



# Lists are usually dynamic, meaning that they change over 
# The course of a program

# MODIFYING ELEMENTS IN A LIST
# To change an element, use the name of the list followed by
# The index of the element you want to change and the new
# value you want that item to have

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ADDING ELEMENTS TO A LIST
# APPEND() can be used to add something to the END of the list
motorcycles.append('ducati')
print(motorcycles)

# Filling an empty list

bugs = []

bugs.append('grasshopper')
bugs.append('dragonfly')
bugs.append('stickbug')

print(bugs)

# INSERTING ELEMENTS INTO A LIST
# INSERT specifies an index position to add an element into

bugs.insert(0, 'ladybug')
print(f'\n{bugs}\n')

# REMOVING ELEMENTS FROM A LIST
# List elements can be removed according to their index position
# or their value

print(bugs)
bugs.remove('stickbug')
print(bugs)


# Can no longer access a value that was removed from list after
# DEL statement is used
del bugs[0]

print(f'\n{bugs}\n')

