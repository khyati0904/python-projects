#random password generator

import string
import random

length= int(input("Enter length of password="))   #it will take input from user
a= string.ascii_letters+ string.digits +string.punctuation  #allows user to generate password with letters, digits, special characters
res = random.choices(a,k=length)
password= ''.join(res)
print(password)
if password.istitle():
    print("your password is valid")
else:
    print("your password is not valid")
        
