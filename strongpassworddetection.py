import re
passStrong=False
def passwordStrength():
    passwordText=input("enter the password")
    charregex=re.compile(r'\w{8,}')
    lowerregex=re.compile(r'[a-z]+')
    upperregex=re.compile(r'[A-Z]+')
    digitregex=re.compile(r'[0-9]+')
    if charregex.findall(passwordText)==[]:
        print("password must contain atleast 8 characters")
    elif lowerregex.findall(passwordText)==[]:
        print("password must contain atleast one lowercase letter")
    elif upperregex.findall(passwordText)==[]:
        print("password must contain atleast 1 uppercaase letter")
    elif digitregex.findall(passwordText)==[]:
        print("password must contain atleast 1 digit")
    else:
        print("your password is strong")
        global passStrong
        passStrong=True
        return
while not passStrong:
    passwordStrength()
