# """

# def inputBook():
#   print("Enter BookId")
#   bookId = int(input())
#   print("Enter the Book Title:")
#   title = input("Enter the title name")
#   print("Enter the price ")
#   price=float(input())

#   mybook = (bookiId,title,price)

#   return mybook


# class Test:

#   # variables & functions
#   x1 = 5
#   x2 = 6
#   def f1():
#     print("Hello")

# t = Test
# print(type(t))
# t1 = Test()
# t2 = Test()
# t3 = Test()

# print(type(t1))
# print(type(t2))
# print(type(t3))

# print()

# class Test:
#   def __init__(self):
#     print("Hello")

# t= Test()
# t1 = Test()

# print()
# """


# Inheritance Concept


# class A:
#   def f1(self):
#     self.a = 5

# # obj1=A()
# # A.f1(obj1)
# # print(obj1.a)

# class B:

#   @staticmethod
#   def f1():
#     print("Hi Sweety")

#   @staticmethod
#   def f2(a,b):
#     print(a,b)

# # B.f1()
# # B.f2(5,7)

# obj2 = B()
# obj2.f1()
# obj2.f2(6,3)


# class C:
#   @classmethod
#   def f1(cls):
#     cls.x = 10
# obj1 = C()
# obj1.f1()

# print(obj1.x)
# print(C.__dict__)

# class D:
#   def __init__(self,a,b):
#     self.a = a
#     self.b =b
# obj1=D(3,4)
# print(obj1.a,obj1.b)


# inheritance
# class person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age = age

#   def showname(self):
#     print(self.name)
  
#   def showage(self):
#     print(self.age)

# p=person("Prashant",22)
# p.showname()
# p.showage()
# print()

# class student(person):
#   def setRollno(self,r):
#     self.rollno = r

#   def showRollno(self):
#     print(self.rollno)

# s1=student("rahul",23)
# s1.setRollno(25)

# s1.showname()
# s1.showage()
# s1.showRollno()

# class student(person):
#   def __init__(self,name,age,r):
#     person.__init__(self,name,age)
#     self.rollno = r


#   def showRollno(self):
#     print(self.rollno)

# s1 = student("Prashant",23,30)
# s1.showname()
# s1.showage()
# s1.showRollno()


# Name confict Concept 


# class A:
#   def __init__(self):
#     self.a=5

# class B(A):
#   def __init__(self):
#     super().__init__() # jese hi B class call ho gyi then a ki value 5 store hogi kyo ki phle super class ko call karega init method phir a ki value 4 store hogi

#     self.a=4

# obj1 = B() #__init__(obj1):

# print(obj1.a)

# # or 

# class A:
#   def __init__(self):
#     self.a=5

# class B(A):
#   def __init__(self):
#     self.a=4
#     super().__init__() # jese hi B class call ho gyi then a ki value 4 store ho jayegi after  super class ko call karega init method then a ki value 5 store hogi

# obj1 = B() #__init__(obj1):
# print(obj1.__dict__)
# print(obj1.a)

# class A:
#   x= 10
# class B(A):
#   x =20

# print(A.x)
# print(B.x)
# print()
# obj1 = B()
# print(obj1.x)




# class A:
#   def f1(self):
#     print("A")

# class B(A):
#   def f1(self):
#     print("b")

# obj1=B()
# obj1.f1()
# print()



# class A:

#   def __init__(self):
#     self.x = 20
#     x =10
# obj = A()
#print(obj.x)


# poly morphirsm

# class A:
#   def f1():
#     print("A")
  
# class B:
#   def f1():
#     print("B")

# obj1 = A()
# obj1.f1()

# class Animal:
#   def __init__(self,name):
#     self.name= name
#   def talk(self):
#     raise NotImplementedError("Eroor")

# obj = Animal("Vikas")
# obj.talk()
# print()

# class Animal:
#   def __init__(self,name):
#     self.name = name

#   def talk(self):
#     raise NotImplementedError("Error")
  
# class cat(Animal):
#     def talk(self):
#       return "meow"
  
# class Dog(Animal):
#     def talk(self):
#       return "Woof"
  
# animals = [

#   cat("Rekha"),
#   cat("soniya"),
#   Dog("Vikash"),
#   cat("Pooja"),
#   Dog("Sachin")
   
#   ]

# for animal in animals:
#   print(animal.name,"-",animal.talk())

#  Operator overloading

# class Line:
#   def __init__(self,L):
#     self.lenght = L

#   def show_lenght(self):
#     print("Lenght",self.lenght)

# l1=Line(10)
# l2 = Line(20)
# l3 = l1+l2
# l3.show_lenght()
# print()

# this type error is oprator overloding  that unsupported

# Now this operator id define in this class
# class Line:
#   def __init__(self,L):
#     self.lenght = L
#   def show_lenght(self):
#     print("Lenght",self.lenght)

#   def __add__(self,other):
#     Line=self.lenght+other.lenght


# l4 = Line(30)
# l5 = Line(40)
# l6 = l4+l5 #l4.__add__(l5) --> __add__(l4,l5)
# l6.show_lenght()
# print()

# Local And Global Varibales

x=30  # this is Global Varibale
def f1():
  x = 10  # this is Local varibale
  print(x)
f1()

def f2():
  y = 20
  print(y)

f2()
#x = 50
print(x)

z=40
def f3():
  global z
  # z =70 now this is global variable
  print(z)
f3()
print(z)

