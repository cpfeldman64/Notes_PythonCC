
#To remove a prefix ex: https://

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
print(simple_url)

#Remove Suffix
filename = "python_notes.txt"
print(f"{filename.removesuffix('.txt')}")

#or using a nested variable

simple_filename = filename.removesuffix('.txt')
print(simple_filename)