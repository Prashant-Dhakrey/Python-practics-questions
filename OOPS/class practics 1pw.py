

class student:
    """this is student class"""
    """ student ki doc string ko kese print kare   'print(student_doc_)' """
print(student)

class teacher:
    "this is my class"
    def __init__(self):
        self.name = "pankaj"
        self.age = 41
        print("constructor excuted")
        
    def display(self):
        print("the name is ",self.name)
        print("the age is ",self.age)
t=teacher()   # create object then automatically call __init__() function 
t2 =teacher() # har objec ke liye ek baar construtor excute hota hai 
t.display()
t.display()
t.display()

class teacher:
    "this is my class"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("constructor excuted")
        
    def display(self):
        print("the name is ",self.name)
        print("the age is ",self.age)


# type of variable 
# static variabe
class teacher:
    institutes ='pw'
    def  __init__(self):
        self.name='pankaj'
        self.age=41
print(teacher.institutes)   # this is better classname _static_variable
t =teacher()
print(t.institutes)


# method  are 3 types
# 1. instance method ==> object se releted method instance method 
 
# 2. class method 
# ek oject any other oject par dependence na ho is called class object
class teacher:
    @classmethod
    def fun(cls):
        print(id(cls)) #class level ka object refrence
print(id(teacher))    #
teacher.fun()         #fun ==> class method 

class demo:
    def __init__(self):
        self.x=10
        self.y=90
d=demo()
print(d.x)
print(d.y)

print(d.__dict__)   # isase ek dict ban ke dict maintain ho jati 


class demo:
    def __init__(self):
        self.x=10
        self.y=90
    def fun(self):
        self.z=100
d1=demo()

d2=demo()
print(d.x)
print(d.y)
print(d1.fun())
print(d1.__dict__) 
