#Adding Whitespace to Strings with Tabs or Newlines
#Whitespace = any nonprinting characters (spaces, tabs, end-of-line symbols)
#Used to organize output to be easier to read

#\t flag will tab in once in the text

print("Python")
print("\tPython")

#\n flag will add a newline
print("Languages:\nPython\nC\nJavaScript")

#\t and \n combined
print("Launguages:\n\tPython\n\tC\n\tJavaScript")


#Stripping whitespace
#Python can look for whitepace on the left/right of a string
#Use the rstrip() METHOD or lstrip() METHOD or strip() METHOD


#this is an example of associating rstrip with a variable

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#Stripping is temporary, in order to make it permanenent,
#you have to associate the stripped value with a variable

