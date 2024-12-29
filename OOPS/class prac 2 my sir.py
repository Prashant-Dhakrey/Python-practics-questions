
"""
# Name Conflict - Issue
# 1. Instance object variable name conficlt

class A:
    def __init__(self):
        self.a = 5
        
class B(A):
    def __init__(self):
        #super().__init__()     # output me a = 4 print 
        self.a = 4
        #super().__init__()      # output me a = 5 print hoga kyo ki parent class ka 
                             # bad me chalega phir a print hoga jo ki a = 5 pass hoga
q = B()   # B class ka init method call hua hai 
print(q.__dict__)     

# 2. class object variable name confilct 

class A :
    x = 10
    
class B(A):
    x = 30
    
print(A.x,B.x)
print()

#  Ex-

class A:
    def f1(self):
        print("A")

class B(A):        
    def f1(self):
        print("B")
        
obj = B()
obj.f1()
print()

# Ex -

class A:
    def f1(self,a):
        print("A")
        
class B(A):
    def f1(self):
        print("B")
        
obj = B()
obj.f1(5) # type Error ayega bcz class B me ek bhi argument nhi  but call me 1 arg hai
print()


# 3. tpye 
# static method name confilct 

class A:
    @staticmethod
    def f1(a,b):
        print("A")
    
class B(A):
    @staticmethod
    def f1(a,b):
        print("B")
        
B.f1(3,4)
obj = B()
obj.f1(3,4)

"""

# 4. tpye
# class method name  conficlt


class A:
    @classmethod
    def f1(cls,a):
        print("A")
        
class B(A):
    @classmethod
    def f1(cls,b,c):
        print("B")
        
B.f1(3,4) 

# I O and C O Variable name confict in single class

class A:
    x = 10
    def __init__(self):
        self.x = 15
obj = A()
print(obj.x) 
print(A.x)


# Poymorphism

# Ex- 
class Animal:
    def __init__(self,name):
        self.name = name
        
    def talk(self):
        return NotImplementedError ("Error")
    
class cat(Animal):
    def talk(self):
        return "meo"
    
class Dog(Animal):
    def talk(self):
        return "woof"
    
Animals = [
    
cat("Rekha"),
cat("Soniya"),
Dog("Moti"),
cat("Rupa"),
Dog("Gabber")
]

for Animal in Animals:
    print(Animal.name,"-",Animal.talk())
    
print()
