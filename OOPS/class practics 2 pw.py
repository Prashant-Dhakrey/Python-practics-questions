
class emp:
    def __init__(self):
        self.__name='pankaj' # under scrore lagane ke baad ye private variabe ho gya
                             #then ham ise class ke bahar acces nhi kar skte hai  
        self.age=42      # class ke bhar ham sirf public variable ko acces kar skte h
    def marrige(self):
        self.wife='sweety'
        
e=emp()
print(e.age)
#print(e.name)

# Q1  [complex number] work using oops

class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def print(self):
        print(self.real,"+",self.imag,"i")
    def add(self,doosra_compl):
        self.real=self.real+doosra_compl.real
        self.imag=self.imag+doosra_compl.imag
    
c=Complex(2,3)
c1=Complex(4,5)

print(c.real)
print(c.imag)
c.print()
c1.print()
print(c.add(c1))
print(c.print())



# agr hame koi bhi values na de then print 
# c.Complex() ==>0+0i
# c.Complex(2) ==>
#c.Complex(2,3) ==> 2+0i

class Complex:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
    def print(self):
        print(self.real,"+",self.imag,"i")
    def add(self,doosra_compl):
        self.real=self.real+doosra_compl.real
        self.imag=self.imag+doosra_compl.imag
    
c=Complex()
c1=Complex(2)
c2=Complex(2,3)
print(c.print())
print(c1.print())
print(c2.print())

# Q2 [fraction] work using oops

class fraction:
    def __init__(self,numerator,denorator):
        self.numerator = numerator
        self.denorator = denorator
    def print(self):
        print(self.numerator,"/",self.denorator)
f=fraction(4,3)
print(f.print())



# Agr hme fraction normalized karke print krana ho tab 

class fraction:
    def __init__(self,numerator,denorator):
        self.numerator=numerator
        self.denorator=denorator
    def print(self):
        print(self.numerator,"/",self.denorator)
    def normalize(self):
        min_value = min(self.numerator,self.denorator)
        while min_value>1:
            if self.numerator%min_value == 0 and self.denorator == 0:
                break
            min_value = min_value-1
        self.numerator = self.numerator//min_value
        self.denomerator = self.denorator//min_value
f=fraction(12,8)
print(f.print())
f.normalize()
print(f.print())



# subtract fraction 

class fraction:
    def __init__(self,numerator,denorator):
        self.numerator=numerator
        self.denorator=denorator
    def print(self):
        print(self.numerator,"/",self.denorator)
    def normalize(self):
        min_value = min(self.numerator,self.denorator)
        while min_value>1:
            if self.numerator%min_value == 0 and self.denorator == 0:
                break
            min_value = min_value-1
        self.numerator = self.numerator//min_value
        self.denomerator = self.denorator//min_value
    def subtract(self,doosra):
        update_numerator=self.numerator*doosra.denorator -self.denorator*doosra.numerator
        update_denorator = self.denorator*doosra.denorator
        self.numerator = update_numerator
        self.denorator = update_denorator
        self.normalize()
f=fraction(1,2)
f1=fraction(1,3)
f.subtract(f1)
print(f.print())
#print(f1.print())
        
        
