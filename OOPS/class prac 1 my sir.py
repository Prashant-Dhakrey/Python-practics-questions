"""
class Test:
    def __init__(self):
        print("Hello")
        
t1 = Test()
t2 = Test()
t3 = Test()

print()

# Intatnce method 

class A:
    def f1(self):
        self.a = 6
obj = A()
A.f1(obj)
print(obj.a)
print()


# Static method 
class A:
    @staticmethod
    def f1():
        print("hello")
        
    @staticmethod
    def f2(a,b):
        print(a,b)
        
obj1 = A()
obj1.f1()
obj1.f2(3,4)
print()

# Class Object 

class A:
    @classmethod
    def f1(cls):
        cls.a = 10
A.f1()
obj = A()
obj.f1()
print(obj.__dict__)  # ye dikhayega ki Instance object me kon sa variable hai   
  
print(A.__dict__)   # ye dikhayega  ki ye class object me variable  hai ki nhi 
print()  


# TYPES OF VARIABLE 

x = 5  # gobal variable 
def f2():
    x = 10    # local variable 
class A:
    y = 10  # class oject variable
    def __init__(self):
        self.n= 5  # instance object variable 
        
        
# Way to create a Instance object variable 

class A:
    def __init__(self,a,b):
        self.a = a  
        self.b = b
    def f1(self):
        self.c = 10
         
obj = A(4,5)   # __init__(obj,4,5) method is called
obj.f1()
print(obj.a,obj.b,obj.c)
obj.d = 30
print(obj.a, obj.b, obj.c, obj.d)

# Way to create a Class object variabe

class B:
    x = 4
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def f1(self):
        self.c = 10
        
    @classmethod
    def f2(cls):
        cls.x2 = 12
        
obj = B(7,9)
obj.f1()
obj.f2()  # mean f(B)
B.f2()   # same mean f(B)
print(obj.a,obj.b,obj.c)
print(obj.__dict__)  # object me kitne variable hai  ye ham dekh skte hai

B.x3 = 25
#print(B.__dict__)  # class me kitne varible hai ye dekh skte hai 

for k,v in B.__dict__.items():
    print(k,v)
    print()
    
"""
    
# Inheritance  Concept 

class Person :
    def __init__(self,n,a):
        self.name = n
        self.age = a 
        
    def showName(self):
        print(self.name)
        
    
    def showAge(self): 
        print(self.age)
        
class Student(Person):
    def __init__(self,r,n,a):
        Person.__init__(self,n,a)  #Person class jo ki parent class hai uske  
          # __init__ function ko call karega tab usame Rahul or 20 dono pass ho jayega 
                                       
        self.rollno = r   # use __init__method () 
    
    #def setRollno(self,r):  
        #self.rollno = r  Ab is function koi jarurat nhi hai 
    
    def showRollno(self):
        print(self.rollno)
        
#p = Person("Prashant ",21)
#p.showName()
#p.showAge()

#s1 = Student("Rahul",20)
s1 = Student(1)
#s1.setRollno(1)
s1.showRollno()
s1.showName()
s1.showAge()


print()