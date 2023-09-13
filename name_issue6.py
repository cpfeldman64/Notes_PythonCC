favorite_foods = {
    'connor': 'pancakes',
     'hope': 'grapes', 
    'austin': 'jambalaya',
}

for name in favorite_foods:
    print(name.title())

friends = ['hope', 'austin',]
for name in friends:
    food = favorite_foods[name].title()
    print(f"\n{name.title()}, I see you love {food}!")

# same output if written as below, because keys are the default item for listing
# for name in favorite_food:
    #print(name.title())

#friends = ['austin', 'hope']

#if person in friends:
    #food = favorite_foods[person].title()
    #print(f"\n{person.title()}, I see you love {food}!")


# Fixed issue, be sure to use for loop to cycle through all of the 
# variables rather than if statement.