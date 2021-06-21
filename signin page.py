print("WELCOME TO SIGNIN PAGE")


question=input("do you have an account(Y/N):")
if question=="y"or question=="Y"or question=="yes":
    my_file=open("new _login.txt","r+")
    f=my_file.read()
    name=input("enter the username:")
    lastname=input("enter the lastname:")
    password=input("enter the password")
    if name  in f and password in f:
        print("login successfully")
    else:
        print("Sorry invalid username and password")
    my_file.close()
if question=="n" or question=="N" or question=="no":
    
    num=input("DO YOU WANT TO SIGNUP NEW ACCOUNT(YES/NO)")
    if num=="yes"or num=="yes":
        file=open("new _login.txt","w")
        new_username=input("enter the new username:")
        file.write(new_username)

        lastname=input("enter the lastname:")
        file.write(lastname)

        password=input("enter the password:")
        file.write(password)
        print("YOUR NEW ACCOUNT IS CREATED SUCCESSFULY:")
    
