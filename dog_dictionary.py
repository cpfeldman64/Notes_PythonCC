# Practice

dog_1 = {
    'breed': 'golden retriever',
    'name': 'dillon',
}

dog_2 = {
    'breed': 'corgi',
    'name': 'pumpkin',
}

dog_3 = {
    'breed': 'poodle',
    'name': 'fletcher',
}

for breed, name in dog_1.items():
    print(f"\n{breed.title()}: {name.title()}")

for breed, name in dog_2.items():
    print(f"\n{breed.title()}: {name.title()}")

for breed, name in dog_3.items():
    print(f"\n{breed.title()}: {name.title()}")

# It feels like there is potentially a way to loop this entire for loop inside
# of another for loop potentially. I want to write one statement instead of 
# copying it and having three separate statements.