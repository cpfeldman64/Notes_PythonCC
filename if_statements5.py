# IF tests
# An IF test can be used to let you handle some items in a list one way
# and other items another way.
# You can also use an IF test to determine if specific conditions are met
# and change the program response depending on those condiditons.

dogs = ['golden retriever', 'corgi', 'poodle', 'pitbull', 'doberman']

for dog in dogs:
    if dog == 'doberman':
        print(dog.upper())
    else:
        print(dog.title())


# Conditional Tests
# IF statements use expressions that can be evaluated as 
# TRUE or FALSE, these are called CONDITIONAL TESTS

# If a test evaluates as TRUE, python will execute the code following
# an IF statement.
# If a test evaluates as FALSE, python will ignore the code following
# an IF statement.

cat = 'tabby'
cat == 'tabby'

# == is an equality operator. If both side match, the evaluation shows
# true. If they do not match, it shows false.

# TESTING FOR EQUALITY IS CASE SENSITIVE
# car = 'Audi'
# car == 'audi'
# FALSE
# car.lower() == 'audi' will show true


# =! is and inequality operator. This can be used to determine whether
# two values are not equal

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


# Numerical Comparisons
age = 18
if age == 18:
    print(True)

answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

# You can also use > and < in your conditional checks

new_age = 20
age < 21
age <= 21
age > 21
age >= 21

# You can also use AND to check multiple conditions simultanesouly
age_0  = 22
age_1 = 18
(age_0 > 21) and (age_1 >= 21)
# Putting () around the inidividual tests is not required, but it can 
# enhance readability.

# You can use OR to check multiple conditions as well

