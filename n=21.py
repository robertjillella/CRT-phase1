# l1=[1,2,3,"robert","banana","cherry"]
# l1.append ("kiwi")
# l1.insert(2,"dragon fruit")
# print (l1[-1:5])
# print (l1[::-1])
# l1[2]="jackfruit"
# print(l1)


# t1=("banana","cherry","apple","sai",1,2,3)
# print(t1)
# print(type(tuple))
# t1=t1+("hii,")
# print(t1)

# l1=[42,36,28,96,4,-1,1]
# min=999
# max=-999
# for i in range(0,len(l1)):
#     if l1[i]<min:
#         min=l1[i]
#     if l1[i]>max:
#         max=l1[i]
# print(min+max)

# d={1:"robert",
#    2:"21a31a04u5",
#    3:"ece",
#    4:"pragati engineering college",
#    }
# d[5]="training"
# d[4]="college"
# d.pop(5)
# for i in d:
#     print(i)
# for j in d.values():
#     print(j)
# for i,j in d.items():
#     print(i,j)
# print(d)

# l1=[[12,21,31],["hii","hello","heyy"],[3.2,3.6]]
# l2=l1[1][1]
# print(l2)
 
# s1={10,20,30,40,"hello","hii","hey"}
# s1.add(50)
# s1.update([70,80,60])
# s1.remove(20)
# s1.pop()
# print(s1)

# s1={10,20,30,40,"hello","hii","hey"}
# s2={50,60,70,80,"d","e","f"}
# s3=s1.union(s2)
# print(s3)
    

# s1={10,20,30,40,"hello","hii","hey"}
# s2={10,60,30,80,"d","e","f"}

# s3=s1.intersectioner(s2)
# print(s3)

     
# def prime():
#     n=int(input("enter the number"))
#     f=1
#     for i in range(2,n):
#         if n%i==0:
#             f=0
#             break
#     if f==1:
#         print ("prime")
#     else:
#         print ("not prime")
# prime()

# def sum(a,b,c):
#     print((a+b+c)/3)
# sum(10,20,30)

# def login():
#     n=1
#     while n!=0:
#         username=input("enter username:")
#         password=input("enter password:")
#         if username==password:
#             print("login successful")
#             break
#         else:
#             print("invalid enter again")
# login()
    
    
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# a=fact(6)
# print(a)

# def fab(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1 
#     return fab(n-1)+(n-2)
# a=fab(10)
# print(a)

# def power(n,m):
#     if m==0:
#         return 1
#     return n*power(n,m-1)
# a=power(2,4)
# print(a)

# def check(n):
#     if n%10==5:
#         return n**2
#     elif n%10==3:
#         return n**3
#     elif n%10==6:
#         return n-1
#     else:
#         return n/2
# # a=check(25)
# # print(a)


# class f15:
#     def light(self):
#         print("ok switching on the light")
#     def fan(self,speed):
#         print("fan is on and switch is",speed)
#         self.s=speed
#     def cpu(self):
#         print("powering on the cpu")
#         print(self.s)
# # robert=f15()
# # robert.light()
# # robert.fan(5)
# # robert.cpu()

# class shopping(f15):
#     def __init__(self,place):
#         print("welcome to shopping mall at",place)
#         self.place=place
#     def dresstype(self,type):
#         print("show me a shirt")
#         self.t= type
#     def price(self,price):
#         print("i want shirt less than 2000")
#         self.p=price
#     def size(self,size):
#         print("my shirt size is 42")
#         self.s=size
#     def display(self):
#         print(self.t,self.p,self.s,self.place)       
# # robert=shopping("judio")
# # robert.dresstype("pant")
# # robert.price(2000)
# # robert.size(36)
# # robert.display()

# class food(f15):
#     def foodtype(self):
#         print("i want biriyani")
#     def price(self,price):
#         print("the biriyani price is",price)
#         self.price=price
# robert=food("judio")
# robert.foodtype()
# robert.price(250)
# robert.dresstype("pant")
# robert.price(2000)
# robert.size("xl")
# robert.display()
# robert.light()
# robert.fan(5)
# robert.cpu()    

# class subjmarks:
#     math=int(input("ënter paper marks of math"))
#     DE=int(input("enter paper marks of design engineering"))
    
# class placements:
#     def info(self):
#         print("1062")
# class dept(placements):
#     def display(self):
#         print("all departments")
# class pragati(placements):
#     def welcome(self):
#         print("welcome")
# robert=placements()
# robert.info()
# robert.dept()
# robert.pragati()

# class arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# robert=arithmatic()
# robert.add(10)
# robert.add(20+10)
# robert.add(20+10+30)

# class carshowroom:
#     def company(self,mercedes,toyota,mahindra):
#         if company==mercedes:
#             print("welcome to mercedes")
#         elif company==toyota:
#             print("welcome to toyota")
#         elif company==mahindra:
#             print("welcome to toyota")
#         else:
#             print("company not selected")
#     def model()
# robert=carshowroom(mercedes)
# robert.carshowroom()   

# import csv
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# a.writerow(["studentid","rollno","name","mobileno"])
# studentid=int(input("enter studentid:"))
# rollno=int(input("enter your roll no:"))
# name=input("enter your name:")
# mobileno=int(input("enter your mobileno:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")

# class carshowroom:
#     def _init_(self):
#         cgst=2000
#         sgst=1000
#         insurence=45000
#         amount=cgst+sgst+insurence
#         self.amount=amount
#     def company(self,company_name):
#         company_name=input('enter the name')
#         print('wellcome to ',company_name,'family')
#         self.company_name=company_name
        
#     def model(self,model):
#         if self.company_name=='mahendra':
#             l1=['thar','xuv700']
#             print(l1)
#         elif self.company_name=='volkswagen':
#             l2=['virtus','taigun']
#             print(l2)
#         elif self.company_name=='toyota':
#             l3=['vellfire','fortuner']
#             print(l3)
#         else:
#             print('not found')
        

#         modelname=input('enter the model')
#         self.model=model
#         print(self.model)
#     def price(self):
#         if self.model=='thar':
#             exshowroom=1410000
#             print('x-showroom price:1410000')
#             print('onroad price:',exshowroom+self.amount)
#         elif self.model=='xuv700':
#             exshowroom=2699000
#             print('x-showroom price:2699000')
#             print('onroad price:',exshowroom+self.amount)
#         elif self.model=='virtus':
#             exshowroom=1941000
#             print('x-showroom price:1941000')
#             print('onroad price:',exshowroom+self.amount)
#         elif self.model=='taigun':
#             exshowroom=1170000
#             print('x-showroom price:1170000')
#             print('onroad price:',exshowroom+self.amount)
#         elif self.model=='vellfire':
#             exshowroom=13000000
#             print('x-showroom price:13000000')
#             print('onroad price:',exshowroom+self.amount)
#         elif self.model=='fortuner':
#             exshowroom=5144000
#             print('x-showroom price:5144000')
#             print('onroad price:',exshowroom+self.amount)
#         else:
#             print('not found')
# obj=carshowroom()
# obj.company('mahendra')
# obj.model('thar')
# obj.price()

class CarShowroom:
    def __init__(self):
        self.cgst = 2000
        self.sgst = 1000
        self.insurance = 45000
        self.amount = self.cgst + self.sgst + self.insurance

    def company(self, company_name):
        print('Welcome to', company_name, 'family')
        self.company_name = company_name

    def model(self, model_name):
        if self.company_name == 'mahendra':
            models = ['thar', 'xuv700']
        elif self.company_name == 'volkswagen':
            models = ['virtus', 'taigun']
        elif self.company_name == 'toyota':
            models = ['vellfire', 'fortuner']
        else:
            print('Company not found')
            return

        if model_name in models:
            self.model_name = model_name
            print('Selected model:', self.model_name)
        else:
            print('Model not found')

    def price(self):
        if hasattr(self, 'model_name'):
            ex_showroom_prices = {
                'thar': 1410000,
                'xuv700': 2699000,
                'virtus': 1941000,
                'taigun': 1170000,
                'vellfire': 13000000,
                'fortuner': 5144000
            }
            ex_showroom_price = ex_showroom_prices.get(self.model_name)
            if ex_showroom_price is not None:
                print('Ex-showroom price:', ex_showroom_price)
                print('On-road price:', ex_showroom_price + self.amount)
            else:
                print('Price not found for this model')
        else:
            print('Please select a model first')


obj = CarShowroom()
obj.company('toyota')
obj.model('fortuner')
obj.price()

# class car:
#     def __init__(self):
#         self.cgst=5555
#         self.sgst=5555
#         self.insurance=5555
#     def company(self):
#         while True:
#             print("toyota,mercedes")
#             self.n=input("enter the car company")
#             if self.n=="toyota":
#                 print("welcome to toyo")
#                 self.model()
#                 break
#             elif self.n=="mercedes":
#                 print("welcome to merc")
#                 self.model()
#                 break
#             else:
#                 print("enter valid company")
#     def model(self):
#         if self.n=="toyota":
#             while True:
#                 print("select the fortuner and LC")
#                 self.choice=input("enter the car model")
#                 if self.choice=="fortuner":
#                     self.price(self,choice)
#                     break
                
            
                