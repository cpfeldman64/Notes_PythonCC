
# Try it Yourself page 104
# Glossary 2

python_glossary = {
    'for loop': 'Used to loop through lists',
    'pop method': 'Used to remove last item in a list without deleting it',
    'print function': 'Used to print text strings',
    'if statement': 'Used to make conditional value checks',
    'titlecase': 'First letter of every word in a string is capitalized',
}

for function, definition in python_glossary.items():
    print(f"\n{function.title()}: {definition}")


# Original individual print statement version, per page 99 tiy
# print(f"\nFor Loop:\n{python_glossary['for loop']}")
# print(f"\nPop Method:\n{python_glossary['pop method']}")
# print(f"\nPrint Function:\n{python_glossary['print function']}")
# print(f"\nIf Statement:\n{python_glossary['if statement']}")
# print(f"\nTitlecase:\n{python_glossary['titlecase']}")

# whoo!

print(f"\n\n")

# Rivers

rivers = {
    'Nile': 'Egypyt',
    'Yangtze': 'China',
    'Trinity': 'Texas',
    'Mississippi': 'Mississippi',
}

for river in rivers:
    if river == 'Nile':
        print(f'\nThe {river} is in Egypt.')
    elif river == 'Yangtze':
        print(f'\nThe {river} is in China.')
    elif river == 'Trinity':
        print(f'\nThe {river} is in Texas.')
    elif river == 'Mississippi':
        print(f"\nThe {river} is in Mississippi.")

print('\n\n')


# OR

for river, location in rivers.items():
    print(f'\nThe {river.title()} river is in {location.title()}.')
          
          
print('\n\n')

for river in rivers:
    print(f'\n{river}')

for location in rivers.values():
    print(f'\n{location}')

print('\n\n\n\n\n')

# Polling

favorite_languages = {
    'connor': 'python',
    'austin': 'javascript',
    'hope': 'c#',
    'josh': 'c++',
    'andy': 'php',
}

people_to_poll = ['connor', 'ty', 'root', 'josh', 'jared']

for people in people_to_poll:
    if people in favorite_languages.keys():
        print(f'\n{people.title()}, thanks for polling!')
    else:
        print(f'\n{people.title()}, come take the poll!') 

# whoo !

