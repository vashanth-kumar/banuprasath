import pandas as pd
import csv
class DB:
    global m,indx
    m = []
    #m=[]
    def create(self):
        global name, bg, location, no, k, m
        k = int(input("Enter the no of donor's need to be added:"))

        for i in range(k):
            a = []
            name = input("Enter your name:")
            bg = input("enter the blood group:")
            location = input("enter the location: ")
            no = int(input("Enter the Ph.no:"))

            a.append(name)
            a.append(bg)
            a.append(location)
            a.append(no)
            print("Recorded updated succesfully")
            m.append(a)
            with open("new_file.csv", "a+") as my_csv:
                csvWriter = csv.writer(my_csv, delimiter=',')
                csvWriter.writerows(m)
            print("====================================================")

    #def create(self,name,bg,location,no):
    def update(self):
        ch = int(input("Enter the choice \n 1. For change name \n2. for change blood group \n3. for change location \n4. change no \nEnter your choice:"))

        if ch == 1:
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))
            old = input("Enter the old name:")

            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1
                    print(indx)


            new = input("Enter the new name:")
            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'Name'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "Name"] = new
            log.to_csv("new_file.csv", index=False)

        if ch == 2:
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))
            old = input("Enter the old name:")

            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1

            new = input("Enter the new  blood group:")
            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'blood_grp'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "blood_grp"] = new
            log.to_csv("new_file.csv", index=False)
            print("=====Details Updated=====")

        if ch == 3:
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))
            old = input("Enter the old name:")

            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1


            new = input("Enter the new location:")
            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'location'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "location"] = new
            log.to_csv("new_file.csv", index=False)


        if ch==4:
            file = open('new_file.csv', mode='r')
            lst = list(csv.reader(file))
            old = input("Enter the old name:")

            for i in lst:
                if i[0] == old:

                    indx = lst.index(i) - 1


            new = input("Enter the new no:")
            df = pd.read_csv("new_file.csv")
            df.loc[indx, 'no'] = new
            df.to_csv("new_file.csv", index=False)
            log = pd.read_csv("new_file.csv")
            log.loc[indx, "no"] = new
            log.to_csv("new_file.csv", index=False)
            print("=====Details Updated=====")


        else:
            print("Invalid selection")



    def search(self):
        #print(m)

        blood_type = input("Enter the blood group:")
        loc=input("Enter the location:")
        file = open('new_file.csv', mode='r')
        csfile = csv.reader(file)
        a = []
        for i in csfile:
            # print(m[i][1])
            if blood_type == i[1] and loc==i[2]:
                a.append(i)
        file.close()
        print(a,end=" ")
        print("====================================================")



    def all_donor(self):

        print("======Total Donar======")
        # blood_type = input("Enter the blood group:")
        file = open('new_file.csv', mode='r')
        csfile = csv.reader(file)
        for i in csfile:
            print(i,end="\n ")

        print("====================================================")



    def delete(self):
        no = input("\nEnter the name:")

        file = open('new_file.csv', mode='r')
        csfile = csv.reader(file)
        a = []
        for i in csfile:
            # print(m[i][1])
            if no == i[1]:
                a.append(i)
                del i
        file.close()

        print(a)
        print("====================================================")
        #
        # for i in range(len(m)):
        #
        #     if m[i][0] == name:
        #         del m[i]
        #         for i in m:
        #             print(i, end=" \n")

        return("delete Operation")



class user(DB):

    def login(self):
        global name, password
        name=str(input("    \n\tEnter the Username :"))
        password=input("\n\tEnter the password :")
        print("\n\tLogined")
    def signup(self):
        name1 = str(input("    \n\tEnter the Username :"))
        password1 = input("\n\tEnter the password :")
        if name1==name or password1  == password:
            print("\n\t signin succesfully")


    def log_out(self):
        return("Log Out")
    def user_details(self):
        return('succesfully submitted')

class admin(DB):
    def send(self):
        return "Alert sended"
   
    def request(self):
        return("request sended")
    def bd_view(self):
        #IT WILL SEARCH FOR THE DONOR
        obj_DB.search()
        obj_DB.create()
        obj_DB.update()
        obj_DB.delete()
        #login and logout
        obj_DB.login()
        obj_DB.log_out()

        return("bd values")

obj_DB=admin()