
#Using quotations in strings
print("This is a string")
print('This is also a string')
print("The language of 'Python' is named after Monty Python")


#title() is a METHOD, an action which python can perform on a piece of data
#METHODs are followed by () because they require specified data to work
#title() changes case to TITLECASE where each word is capitalized

name = "ada lovelace"
print(name.title())

#These METHODs change the printed info to upper/lowercase
print(name.lower())
print(name.upper())


#Using variables in strings / F STRINGS (Format Strings)
#Must use the "f" tag before inserting variables into a string 

first_name = ("ada")
last_name = ("lovelace")
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

#Assigning a string as a variable using "f"
#Stuff like this makes the print call simpler, which is ideal
message = f"Hello, {full_name.title()}!"
print(message)



