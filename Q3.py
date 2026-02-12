C_Username="samatha"
C_Password="sam@123"
C_Status=True
Username=input("enter the username:")
password=input("enter the password:")
if Username==C_Username and Password==C_Password:
    if C_Status:
        print("Login sucessful")
    else:
        print("your account is disabled")
else:
    print("wrong credentails ")