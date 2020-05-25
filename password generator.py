import random
import string
a=string.ascii_letters
c=string.punctuation
d=string.digits
days=int(input("enter the number of days that you want to access this password"))
no_of_letters=int(input("enter the number of letters to have in yoyur password"))
no_of_digits=int(input("enter the number of digits to have in your password"))
#length of the password should be atleast 6
password=""
passwordlength=int(input("enter password length that u want"))
print("hey user, your password should have atleast one upperletter,lower letter,digit and a character. So give the no of inputs accordingly. so that we will generate a password according to that")
if no_of_letters+no_of_digits<passwordlength and no_of_letters>=2:
    for l in range(no_of_letters):
        s=random.choice(a)
        if s.islower():
            if any(s):
                password=password+s
            else:
                password+=s.upper()
        else:
            if any(s):
                password+=s
            else:
                password+=s.lower()
    for j in range(no_of_digits):
        password=password+random.choice(d)
    while len(password)<passwordlength:
        password=password+random.choice(c)
    print("hey user, your password"+" "+password+" "+"is valid upto"+" "+str(days)+"days")
else:
    print("invalid input")
