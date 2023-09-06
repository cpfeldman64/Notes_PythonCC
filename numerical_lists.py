# Making Numerical Lists
# RANGE() FUNCTION will generate a series of numbers
# You can use it in conjunction with a for loop
# EX

for value in range(1, 5):
    print(value)

# Python will start the count at the first value you provide and
# end the count at the second value you provide
# So to print 1 through 6, you would want to ask for (1,7)

# Can also use range() on only one argument and it will start the
# sequence of numbers from 0
# EX
for value in (range(6)):
    print(value)

# Using range() with list function

numbers = list(range(1, 6))
print(f'\n{numbers}')

# If you pass a third argument to range(), Python uses that value as
# step size when generating numbers
# To list even numbers from 1 - 10:
even_numbers = list(range(2, 11, 2))
# This function has the value start at 2, then add 2 to that value
# repeatedly until it reaches or passes the end value, 11.
# result is [2, 4, 6, 8, 10]

# To print the first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(f'\n{squares}')

# more concisely:

# squares = []
# for value in range(1,11):
#   squares.append(value**2)
# print(squares)


# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f'\n{min(digits)}')
print(f'\n{max(digits)}')
print(f'\n{sum(digits)}')

# List Comprehensions
# Allows you to generate a more complex list in just one line of code
# Combines a for loop and the creation of elements into one line and
# automatically appends each element.

also_squares = [value**2 for value in range(1,11)]
print(f'\n{also_squares}')

# Note the lack of a colon!










































































