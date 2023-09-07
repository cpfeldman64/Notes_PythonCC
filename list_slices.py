# Working with Part of a List
# A specific group of items in a list is called a SLICE
# You can create a SLICE by specifying the index of the first and last 
# elements you want to work with
# As with RANGE, Python stops count one item before the second index
# specified. 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# If you omit the first index in a slice, Python will automatically
# use the first item from the list

cats = ['joe', 'roman', 'tobias', 'loki']
print(cats[:2])

# Similarly, if you do not provide a second index, Python will auto
# select the last item from the list

dogs = ['dillon', 'pumpkin', 'fletcher', 'finley']
print(dogs[2:])

# You can use this in conjunction with negative numbers to print
# only the last part of a list without knowing how long it is!

farm_animals = ['pigs', 'cows', 'chickens', 'geese']
print(farm_animals[-3:])

# This will continue to work even if the size of the list changes
farm_animals.append('crocodiles')
print(farm_animals[-3:])

# LOOPing through a SLICE
# You can use a slice in a FOR loop if want to loop through a subset
# of the elements in a list

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
# You can start with an existing list and make a new, separate list 
# from the first one.
# To copy, you can make a slice that includes the entire original list 
# by omitting both indexes ([:]).

my_foods = ['pancakes', 'chicken nuggets', 'peaches']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

friend_foods.append('lamb chops')
print("My friend's favorite foods are:")
print(friend_foods)

# Do NOT just make the lists equal to each other
# my_foods = friend_foods won't work because commands will point to 
# the exact same variable rather than two separate but identical lists







