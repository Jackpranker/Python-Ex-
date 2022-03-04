print("Welcome to Pranker Password generator for all formats ")
import random
import string
characters='abcdefghijklmnopqrstuvwxyz1234567890'
password= "".join(random.choice(characters) for i in range(7))
print('Your Password is: ',password)

letters=string.ascii_letters
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for both upper & lower',code)

letters=string.ascii_uppercase
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for upper case',code)

letters=string.ascii_lowercase
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for lower case',code)

letters=string.digits
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for digits',code)

letters=string.punctuation
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for string',code)

letters=string.whitespace
code= "".join(random.choice(letters) for i in range(10))
print('Code generate',code)

letters=string.printable
code= "".join(random.choice(letters) for i in range(10))
print('Code generate for printable',code)





