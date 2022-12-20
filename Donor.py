from BD_core import *
obj=DB()
obj=user()

#obj.login()
while 1:
    choice=int(input("\n\t Enter 1 For Login And Enter 2 For Signup"))
    if choice==1:
        obj.login()
    elif choice==2:
        obj.signup()
        obj.create()
    else:
        print("\n\t Invalid Sclction")

