# Looping through an entire list
# FOR LOOP:
# Useful when you want to do the same action for every item in a list
# Prevents having to make individual commands for each list item,
# which might require code changes if items are added/removed later

dogs = ['golden retriever', 'corgi', 'doberman']

# You could read this as, for every dog in the dogs list, print their name
for dog in dogs:
    print(dog.title())
# Python repeats the entire loop once for each item in the list
# Then the program ends.

# Adding in a string
# Everything that is indented is part of the loop and will be executed
# once for each item in the list
for dog in dogs:
    print(f'\n{dog.title()}, you are the cutest!')
    print(f'{dog.title()}, do you know any tricks?')

# Doing something after a for loop
# So long as the next command is not indented, it will not be part
# of the loop and will only take place once.
print('\nDoggos! What are all of your names?')

