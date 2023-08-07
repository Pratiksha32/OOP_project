"""


an employee has age salary, id department an d email id. every

"""

class Emp:
    def __init__(self, nm, id ,sal,dept):
        self.name = nm
        self.EID = id
        self.salary =sal
        self.department = dept

    def getInfo(self):
        return self.name, self.EID, self.salary, self.department
    
    def __str__(self):
        return self.name

 
# from employee import *
# from employee import emp
from utility import *

db=[]  
class Test:
    def dashboard(self):
        print("""
              
            Welcome to the Employee Management Dashboard MENU
              
              1. Create a new Employee in DB
              2. Display the employee 
              3. Update the Employee
              4. Delete the Employee
              5. Search the Employee

            """)
    




    def createEmployee(self):
        uname = input("Enter Name of Employee : ")
        uid = eval(input("Enter id of Employee : "))   # not null unique : primary key
        usalary = eval(input("Enter salary of Employee : "))
        udept = input("Enter deptpart of Employee : ")

        e1 = Emp(nm = uname , id = uid, sal= usalary, dept= udept)
        db.append(e1)
        print(f"Employee {uname} added successfully in database....")
    

    def displayEmployee(self):
        print("-" *85)
        print("|{id:^20}|{n:^20}|{s:^20}|{d:^20}|".format(id = "E_ID", n = "Name", s ="Salary" , d="Department" ))
        print("-" *85)


        for i in range(len(db)):
            print("|{id:^20}|{n:^20}|{s:^20}|{d:^20}|".format(id = db[i].EID, n = db[i].name, s =db[i].salary , d=db[i].department ))
            print("-" *85)
    
    def searchEmployee(self):

        uid = eval(input("Enter Employee ID: "))

        for i in range(len(db)):
            if db[i].EID == uid:
                return i
        return -1





    def updateEmployee(self):
        i = self.searchEmployee()
        if i>=0:
            uname=input("Enter Updated Name of The Employee : ")
            usalary=eval(input("Enter The updated salary of the Employee : "))
            udept = input("Enter The Updated Employee Department : ")
            
            db[i].name=uname
            db[i].salary=usalary
            db[i].department=udept
            
            print(f"Employee {db[i].name} updated successfully in db...")


    def deleteEmployee(Self):
        i = obj.searchEmployee()
        # i = self.searchEmployee()

        if i>=0:
            del db[i]
            print("Employee deleted successfully from database....")
        else:
            print("invalid Employee ID!....please try again")    





dummy =Emp("jay",101, 25000, "IT")
db.append(dummy)

dummy =Emp("Viru",102, 35000, "HR")
db.append(dummy)

# print(db)   #[<__main__.Emp object at 0x0000026AB0AA5FD0>]
# print(db[0].name)
# print(db[0].EID)
# print(db[0].salary)

# print()
# print(db[1].name)
# print(db[1].EID)
# print(db[1].salary)


# for i in range(len(db)):
#     if db[i].name == "Viru":
#         print(db[i].name, "is at index", i)
       

obj= Test()

while True:
    obj.dashboard()

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        obj.createEmployee()


    elif choice == 2:
        if len(db)>0:
            obj.displayEmployee()
        else:
            print("DataBase is Empty")    


    elif choice == 3:
        var = validate_db(db)
        if var:
            obj.displayemployee()
        else:
            print("DataBase is Empty")    
        


    elif choice == 4:
        if len(db)>0:
            obj.deleteEmployee()
        else:
            print("DataBase is Empty")
        

    elif choice == 5:
        if len(db)>0:
            i = obj.searchEmployee()
            if i >= 0:
                print(f"Employee Found at index {i}")
            else:
                print("invalid Employee ID! ")
        else:
            print("DataBase is Empty")

    else:
        print("Invalid Choice.....Please choose correct Option")

    ch = input("Do you want to continue y/n? : ")
    if ch.lower() != 'y':
        # for i in range(len(db)):
        #     print(db[i])
        break






