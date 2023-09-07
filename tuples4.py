# Tuples
# Python refers to values that cannot change as immutable
# An immutable LIST is called a TUPLE
# Tuples use () rather than []
# You can take "slices" of tuples using each item's index, as with lists

# Dimensions of a rectangle that should remain one size
dimensions = (200,50)
# Can tell it is a tuple because of the ()
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250
# Will cause an error if you try to change, as above

# LOOPing through values of a TUPLE
# Can use FOR loops, as with lists

for dimension in dimensions:
    print(dimension)

# Writing over a tuple
# You can assign a new value to a variable that represents a tuple

print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Above is an example of re-associating an existing variable with new
# dimensions. This is the allowed method for changing a tuple


# Tuples are considered simple data structures. They should be used 
# when you want to store a set of values that should not be changed
# over the course of a program.


