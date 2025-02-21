import random
import string
print("Welcome to random password generator")
def passwordgenerator():
   
    length=int(input("enter length of password"))
    lowerdata=string.ascii_lowercase
    upperdata=string.ascii_uppercase
    digitdata=string.digits
    symbolsdata=string.punctuation
    combine=lowerdata+upperdata+digitdata+symbolsdata
    x=random.sample(combine,length)
    password="".join(x)
    print(password)

    passwordgenerator()
passwordgenerator()    