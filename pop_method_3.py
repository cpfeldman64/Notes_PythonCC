# Removing a list item using the POP() METHOD

bugs = []

bugs.append('grasshopper')
bugs.append('ladybug')
bugs.insert(1,'dragonfly')
bugs.append('stickbug')

print(bugs)

# POP() METHOD removes the last item in the list, but retains
# ability to work with that item post removal
# (item is not completely deleted as with DEL command)

popped_bug = bugs.pop()
print (f'\n{bugs}\n')

print(popped_bug)

#EX in string

print(f"\nThe last bug I saw was a {popped_bug.title()}!\n")

# Can use the POP() METHOD to remove an item from any list
# position if you provide its index in ()

#EX

first_bug = bugs.pop(0)
print(f"The first bug I saw was a {first_bug.title()}!\n")


# REMEMBER: everytime you use POP() you are removing the item
# from the list, as shown below
print(bugs)
print('\n\n\n')

# CHOOSING BETWEEN POP() AND DEL COMMAND
# Use DEL command when you want to get rid of an item and 
# not use it in any way. Use POP() METHOD when you want to use
# an item as you are removing it from the list.

# REMOVE COMMAND: REMOVE() used when you don't know the index position
# of the list element that you are removing
# EX

farm_animals = ['cows', 'pigs', 'sheep', 'geese']
print(farm_animals)

farm_animals.remove('sheep')
print(farm_animals)

too_mean = 'geese'
farm_animals.remove(too_mean)
print(farm_animals)
print(f"\n{too_mean.title()} are too mean to be my friends.\n")

# Geese variable has been removed from the list, but it 
# wasn't deleted entirely. 
# It can still be used through the variable 
# too_mean to show information.

# NOTE: the REMOVE() method removes only the first occurence
# of the specified value. If the value appears more than
# once in the list, you will have to use a loop to remove
# the other occurences.