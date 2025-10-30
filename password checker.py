#python password checker
password=input("Enter your Password:")
length=len(password)
if length >= 8:
    if not any(c.isupper() for c in password):
        print("Your password has no upper case.")
    
    if not any(c.islower() for c in password):
        print("your password has no lower case.")
    
    if not any(c.isnumeric() for c in password):
        print("your password has no numbers.")
        
    if not any(c.isspace() for c in password):
        print("your password has no space.It is recomended to have space.")
else:
    print("Your password is short.Make it atleast 8 Charecter long.")
