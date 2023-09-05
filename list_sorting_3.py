# Organizing Lists
# SORT() method allows you to sort a list, but will change the list
# order permanently.


# EX of sorting alphabetically
cats = [
    'calico', 'black', 'white', 'orange', 'tabby'
]

cats.sort()
print(cats)

# EX of sorting reverse-alphabetically

cats.sort(reverse=True)
print(cats)

# Sorting a list temporarily using sorted() function

bugs = [
    'stickbug', 'ladybug', 'beetle', 'grasshopper', 'dragonfly'
]

print("\nHere is the original list:")
print(bugs)

print("\nHere is the sorted list:")
print(sorted(bugs))

print("\nHere is the original list again:")
print(bugs)


# Printing a list in reverse order

trees = [
    'pine', 'oak', 'fir', 'maple'
]

print(f'\n{trees}')

trees.reverse()
print(f'\n{trees}')

# reverse() changes the order of the list permanently
# but you can revert it by commanding reverse() a second time

# Finding the length of a list using len()

cakes = [
    'chocolate', 'red velvet', 'vanilla', 'carrot'
]
cake_list_length = len(cakes)

print(f'\n{cake_list_length}')

print(len(cakes))

# Lists are calculated starting at 1, as normal

