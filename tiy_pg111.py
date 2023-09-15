# Try it yourself Page 111

# People
connor = {
    'first_name': 'connor',
    'last_name': 'feldman',
    'age': 23, 
    'city': 'lewisville',
}

hope = {
    'first_name': 'hope',
    'last_name': 'beohm',
    'age': 25,
    'city': 'arlington',
}

austin = {
    'first_name': 'austin',
    'last_name': 'adams',
    'age': 23,
    'city': 'arlington',
}

people = [connor, hope, austin]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\n{full_name.title()}")
    for key, value in person.items():
       print(f"\t{key}: {value}")

# whoo !

# Pets

dillon = {
    'name': 'dillon',
    'type': 'dog',
    'color': 'golden',
    'temperament': 'sweet', 
}

joe = {
    'name': 'joe',
    'type': 'cat',
    'color': 'white',
    'temperament': 'grumpy',
}

loki = {
    'name': 'loki',
    'type': 'cat',
    'color': 'black',
    'temperament': 'skittish',
}

pets = [dillon, joe, loki]

for pet in pets:
    pet_name = f"{pet['name']}"
    print(f"\n{pet_name.title()}")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

print('\n\n\n')


# Favorite Places

favorite_places = {
    'john': ['paris', 'berlin'],
    'jane': ['chicago', 'indianapolis'],
    'louis': ['new york', 'los angeles'],
    'connor': ['wherever'],
}

for person, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{person.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{person.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")

# code format stolen from nesting6. This works pretty well though.



