from BD_core import *
#obj=DB()
objadmin=admin()

while 1:
    input_1 = int(input(
        "Enter the choice \n1.for add new user: \n2. for search the donor: \n3. for view all donors \n4. Update donor: \n5. Delete donor: \n\t Enter the choice:"))
    if input_1==1:

        objadmin.create()
    elif input_1==2:
        objadmin.search()
    elif input_1==3:
        objadmin.all_donor()
    elif input_1==4:
        objadmin.update()
    elif input_1==5:
        print("Enda ipadi delelte pandringaa pera pasangla thatha soldra kelulnga da")
        #objadmin.delete()
    else:
        print("Invalid selection")

