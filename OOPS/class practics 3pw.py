

#  INHERITANCE

class parent:
    def __init__(self,x,y):
        self.x = x   # agr hme x private karna ho tab use x ki jgh __x 
        self.y = y
class child(parent):
    def __init__(self,x,y,a,b):
        # to initalized x,y ==> parent ka cunstructir chayiye
        super().__init__(x,y) # super hamne parent ke x or y k0 lene ke liye use kiya h
        self.a=a
        self.b=b
    def print(self):
        print("x == ",self.x)
        print("y == ",self.y)
        print("a == ",self.a)
        print("b == ",self.b)
c = child(1,2,3,4)
print(c.print())   

# agr hame private varibale acces kar skte hai some method se 

class parent:
    def __init__(self,x,y):
        self.__x = x   
        self.y = y
    def getx(self):
        return self.__x
    def setx(x):
        self.__x=x
    def print(self):
        print("x==",self.__x)
        print("y==",self.y)
class child(parent):
    def __init__(self,x,y,a,b):
        # to initalized x,y ==> parent ka cunstructir chayiye
        super().__init__(x,y) # super hamne parent ke x or y k0 lene ke liye use kiya h
        self.a=a
        self.b=b
    def print(self):
        super().print()
        print("a == ",self.a)
        print("b == ",self.b)
c = child(10,20,30,40)
print(c.print())  



class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,doosra):
        new_real = self.real+doosra.real
        new_imag =self.imag+doosra.imag
        c3 = Complex(new_real,new_imag)
        return c3
    def print(self):
        print(self.real,"+",self.imag,"i")
#    def __str__(self):
 #       return str(self.real)+"+"+ str(self.imag)+ "i"
            
# agr ham direct c ko print kare toh hm def str function ko use karke print karerge
              # toh bo printho jayega print fun ki jarurat nhi padegi
c1 =Complex(2,3)
print(c1.print())
c2 = Complex(4,5)
print(c2.print())
c=c1+c2
print(c.print())
print(c)  # when use str funcion then easly print(c) use 


# ABSTRACT CLASS AND ABSTRACT METHOD CONCEPT

from abc import ABC ,abstractmethod
class RBI:
    def __init__(self):
        print("RBI")
   # @abstractmethod
    def minibalence(self):
        pass 
   # @abstractmethod
    def f(self):
        pass
c=RBI()
print(c)

class ICICI(RBI):
    def __init__(self):
        print("ICICI")
    def minibalence(self):
        print("implemented icici rule")
    def g(self):
        print("Hello") # own methods
        
c=ICICI
print(c)



# EXAPECTION HALDLING  AND ERROR HANDING

a = 20
print(a)
a="xyz"
print(a==b) # then NAME ERROR

c=23/0
print(c)  # ZERO DIVISION ERROR

d="prashant"+4
print(d) # TYPE EROR  diffrent type 

s=int(input())
t=int(input())
print(s/t)      # input me abc dalege tohen give  VALUE Error



try:
    r=int(input())
    p=int(input())
    q=r/p
    print(q)
    #breakpoint
except ValueError:
    print("wrong values please enter the right value")
except ZeroDivisionError:
    print("please enter the non zero number")
except TypeError:
    print("ckeck the syntax")