"""list1=[999,3,99,9,9,9,839,000,2,2,33,39,99,89,434,0,2,5,3,2,7,]
set1=set(list1)
l=list(set1)
t=tuple(list1)
print(t)
list1.append(34)
print(list1)
list1.remove(99)
print(list1)
list1.reverse()
print(list1)
print(list1)
list1.insert(2,5566)
print(list1)
list1.clear()
print(list1)

list1.pop(8)
print(list1)
print(list1) """



class employee:
    x=34
    print(x)
    class data:
        def __init__(self,name,age, role):
            self.name=name
            self.age=age
            self.role=role
        def myfun(self):
         print("hell my name is"+ self.name)
    emp=data("lakki",23,"developer")

    emp.myfun()

    print(emp.name)
    print(emp.age)
    print(emp.role)
    print(x)
    class person:
        def __int__(self,ID,address,company):
            self.ID=ID
            self.address=address
            self.company=company

    class India():
        def capital(self):
            print("New Delhi is the capital of India.")

        def language(self):
            print("Hindi is the most widely spoken language of India.")

        def type(self):
            print("India is a developing country.")

    class USA():
        def capital(self):
            print("Washington, D.C. is the capital of USA.")

        def language(self):
            print("English is the primary language of USA.")

        def type(self):
            print("USA is a developed country.")

    def func(obj):
        obj.capital()
        obj.language()
        obj.type()

    obj_ind = India()
    obj_usa = USA()

    func(obj_ind)
    func(obj_usa)

    print("+++++++++++++++++++++++++==+======================================+++++++++++++++++++++++++++=")


from datetime import datetime


name=str(input("please enter your name "))
groceries=''' 
RICE              RS 3O/KG 
SUGAR             RS 40/KG
OIL               RS 89/KG
DAL               RS 90/KG
BOOST             RS 120/KG
COOLGATE          RS 100/KG
PANNER            RS  50/KG
              '''

items={"rice":30,"SUGAR":40,"OIL":89,"DAL":90,"BOOST":120,
       "COOLGATE":100,"PANNER":50}
options=int(input("for list of items press 1 exist for press 2:"))

if options==1:
    print(groceries)
    print("please carry on your shooping:")
for i in range(len(items)):
    inp=int(input("if you want to buy press 1 or 2 for exist from here: "))
    if inp==2:
        break
    if inp==1:
        item=input("Enter your items please  :")
        quantity=int(input("etner you quantiy:"))
        if item in items.keys():
         price=quantity*(items[item])
         print("total amount is " ,price)
         item= input("Enter your items here")











