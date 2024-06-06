#random password generator

import string
import random

length= int(input("Enter length of password="))
a= string.ascii_letters+ string.digits +string.punctuation
res = random.choices(a,k=length)
password= ''.join(res)
print(password)
if password.istitle():
    print("your password is valid")
else:
    print("your password is not valid")
        
