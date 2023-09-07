# I feel like there is a better way to do this than by writing
# out the entire tuple when updating it's variable value. Can I copy
# a tuple as a list and use the list to update the tuple?

sodas = ('diet coke', 'coke zero', 'sprite zero', 'canada dry', 'fanta')
print('\n\nMy favorite sodas are:')
for soda in sodas:
    print(soda)

new_sodas = list(sodas)
new_sodas.append('root beer')

print('\n\nActually, my favorite sodas are:')
for soda in new_sodas:
    print(soda)

# Can turn a tuple into a list!

# Retains original tuple:
print(sodas)
# sodas.append('cake')
# still a tuple because this doesn't work!

# Also retains the second list made from first tuple
print(new_sodas)
new_sodas.append('pepsi')
print(new_sodas)

# Use the second list from the first tuple to create a second tuple and
# assign it to a new variable

new_sodas_tuple = tuple(new_sodas)

#new_sodas_tuple.append('mtn dew')
# now turned into a tuple because this doens't work!

print(f'\n{new_sodas_tuple}')
print(f'\n{new_sodas}')
print(f'\n{sodas}')

# The two tuples and the list all exist separately!