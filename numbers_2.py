#Integers
#You can add (+), subtract (-), multiply (*), or divide (/)
#Exponents use two ** 
#Python supports the standard order of operations

print(2 + 3)
print(2 - 3)
print(2 + 3 * 4)
print(2 + 3 / 4)
print(2 + 3 ** 4)

#Floats are numbers with decimal points
#Sometimes, in trying to very accurate python will calculate
#to a large number of decimal points. This is fine, and
#can be adjusted (see Part II projects).

print(0.2 + 0.1)

#Divison, even between two whole numbers, always provides a float
#Mixing integers and floats always provides a float as well
#Even if the output is a whole number!

#You can use underscores to make longer numbers more readable
#These will not affect the readout

universe_age = 14_000_000_000
print(universe_age)

#Multiple Assignment
#You can assign multiple numbers to variables at the same time

x, y, z = 0, 0, 0 


#Constants are variables whose value remain the same through 
#the life of a program
#Python programmers use all caps to show a variable is a constant

MAX_CONNECTIONS = 5000