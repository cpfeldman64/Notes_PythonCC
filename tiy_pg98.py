# Try it yourself page 98

# Person

connor = {
    'first_name': 'connor',
    'last_name': 'feldman',
    'age': 23, 
    'city': 'arlington',
}

print(connor['first_name'])
print(connor['last_name'])
print(connor['age'])
print(connor['city'])

# There is definitely a better way to print all values at once.
# printing this:
# for item in connor:
#   print(item)
# will print out the keys but not the values. 

# Favorite Numbers

favorite_numbers ={
    'connor': '64',
    'austin': '59',
    'mom': '13',
}

print(f"Connor: {favorite_numbers['connor']}")
print(f"Austin: {favorite_numbers['austin']}")
print(f"Mom: {favorite_numbers['mom']}")


# Glossary

python_glossary = {
    'for loop': 'Used to loop through lists',
    'pop method': 'Used to remove last item in a list without deleting it',
    'print function': 'Used to print text strings',
    'if statement': 'Used to make conditional value checks',
    'titlecase': 'First letter of every word in a string is capitalized',
}

print(f"\nFor Loop:\n{python_glossary['for loop']}")
print(f"\nPop Method:\n{python_glossary['pop method']}")
print(f"\nPrint Function:\n{python_glossary['print function']}")
print(f"\nIf Statement:\n{python_glossary['if statement']}")
print(f"\nTitlecase:\n{python_glossary['titlecase']}")










