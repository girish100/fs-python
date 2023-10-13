# to print multiple employee records with creating only one object
import pandas as pd
class details():
    def __init__(self) -> None: #constructor
        self.id = []
        self.name  = []
        self.sal = []
        self.desig = []
        self.dob = []
        self.comp = []
        self.c_name = []
        self.c_id = []
        self.c_dob = []
        self.pname = []
        self.pid = []
        self.price = []
        self.p_comp = []
    def e_data_add(self,n): #instance method
            for i in range(n):
                print(f"{i+1}.Employee ")
                id = input("Id: ")
                name = input("Name: ")
                dob = input("Date of Birth: ")
                comp = input("Company: ")
                desig = input("Designation: ")
                sal = input("Salary: ")
                print()
                self.id.append('-'if id == '' else id)
                self.name.append('-'if name == '' else name)
                self.dob.append('-'if dob == '' else dob)
                self.desig.append('-'if desig == '' else desig)
                self.sal.append('-'if sal == '' else sal)
                self.comp.append('-'if comp == '' else comp)
    def c_p_data(self,n,type1): #instance method
        if type1 == 'cust':
            for i in range(n):
                print(f"{i+1}.Customer ")
                c_name = input("Customer Name: ")
                c_id = input("Customer Id: ")
                c_dob = input("Customer Date of Birth: ")
                print()
                self.c_id.append('-'if c_id == '' else c_id)
                self.c_name.append('-'if c_name == '' else c_name)
                self.c_dob.append('-'if c_dob == '' else c_dob)
        elif type1 =='pro':
            for i in range(n):
                print(f"{i+1}.Product ")
                pname = input("Product Name: ")
                pid = input("Product Id: ")
                price = input("Price: ")
                p_comp = input("Product company: ")
                print()
                self.pid.append('-'if pid == '' else pid)
                self.pname.append('-'if pname == '' else pname)
                self.price.append('-' if price=='' else price)
                self.p_comp.append('-' if p_comp == '' else p_comp)
    def d_print(self,n,type1): #instance method
        if type1 == 'emp':
            print("=====Employee Details=====")
            for i in range(n):
                print("{}. Company:{}".format(i+1,self.comp[i]))
                print("Id: {}\nName: {}\nDOB: {}".format(self.id[i],self.name[i],self.dob[i]))
                print("Designation: {}\nSalary:{}\n".format(self.desig[i],self.sal[i]))
        elif type1 == 'cust':
            print("=====Customer Details=====")
            for i in range(n):
                print(f'{i+1}. Customer name: {self.c_name[i]} \nId: {self.c_id[i]}\n DOB: {self.c_dob[i]}/n')
        elif type1 == 'pro':
            print("=====Product Details=====")
            for i in range(n):
                print(f'{i+1}. Company: {self.p_comp[i]}\nProduct name: {self.pname[i]} \nId: {self.pid[i]}\n Price: {self.price[i]}\n ')
    def d_pandas(self,n,type1):
        if type1 == 'emp':
            print("=====Employee Details======")
            self.emp_pd = pd.DataFrame(columns=['ID','Employee Name','DOB','Company','Designation','Salary'])
            for i in range(n):  
                self.emp_pd.loc[i]=[self.id[i],self.name[i],self.dob[i],self.comp[i],self.desig[i],self.sal[i]]
            print(self.emp_pd)
        elif type1 == 'cust':
            print("=====Customer Details=====")
            self.cust_pd = pd.DataFrame(columns=['Customer Id','Customer Name','DOB'])
            for i in range(n):  
                self.cust_pd.loc[i]=[self.c_id[i],self.c_name[i],self.c_dob[i]]
            print(self.cust_pd)
        elif type1 == 'pro':
            print("=====Product Details=====")
            self.pro_pd = pd.DataFrame(columns=['Company','Product ID','Product Name','Price'])
            for i in range(n):  
                    self.pro_pd.loc[i]=[self.p_comp[i],self.pid[i],self.pname[i],self.price[i]]
            print(self.pro_pd)
#Main execution
t1 = details() #object creation
e = False
c = False
p = False
while True:
    type1 = int(input('''\nEnter the choice for entering
1 for Employee Details
2 for Customer Details
3 for Product Details
4 for printing all the entered data
5 for exit
number: '''))
    print()
    if type1 == 1 or type1 == 2 or type1 == 3:
        q = int(input("Enter number of records you want to input: "))
    if type1 == 1:
        t1.e_data_add(q)
        t1.d_print(q,'emp')
        e = True
    elif type1 == 2:
        t1.c_p_data(q,'cust')
        t1.d_print(q,'cust')
        c = True
    elif type1 == 3:
        t1.c_p_data(q,'pro')
        t1.d_print(q,'pro')
        p = True
    elif type1 == 4:
        if e == True or c == True or p == True:
            choice = input("Use pandas: y/n  : ").lower()
            if choice == 'y' or choice == 'yes' and e == True :
                t1.d_pandas(q,'emp')
            if choice == 'y' or choice == 'yes' and c == True :
                t1.d_pandas(q,'cust')
            if choice == 'y' or choice == 'yes' and p == True :
                t1.d_pandas(q,'pro')
            else:
                if e == True :
                    t1.d_print(q,'emp')
                if c == True:
                    t1.d_print(q,'cust')
                if p == True:
                    t1.d_print(q,'pro')
        else:
            print("No Data record found")
    elif type1 == 5 :
        break
    else:
        print("Invalid Input")
        break
