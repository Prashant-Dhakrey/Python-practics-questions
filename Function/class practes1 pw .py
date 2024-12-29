
# print the given list of square of list 
def twice(l):
    for i in range(len(l)):
        l[i]=2*l[i]
l1 = [1,2,3,4,5]
twice(l1)
print(l1)


# LOCAL AND GLOBAL  ARUGUMENT CONCEPT

#1st type 

x = 10      #this is global varialbe
def f():
    a = 100  # thsi is local variable
    print(a)
    print(x)
f()
print(x)

# 2 type 

y = 10      #same this is global 
def f():
    b = 200  # this is local variable 
    print(b)
    print(y)
y = 150       # now y me aasing not 10  now assing value 150
f()
print(y)     #this y value are same then 150 both print bcz y assing 150

#3 type  

y = 10      #same this is global 
def f():
    b = 200  # this is local variable 
    print(b)
    print(y)
f()
y = 150     # now this is global variable   both variable are different 
print(y)             #  ek y me 10 assing  second y me 150 assing 


# 4 type 

y = 20
def f():
    c = 30 
    print(c)
    print(y)
#print(z)
f()
#z = 40  # agr function call karne ke baad koi dete hai  toh phir use ham 
         # function ki body me print  nhi kar skte hai error show variabke not define 
            
z = 40 
print(z)   # after function define values and print this value then this normal 
           # normal given return values
           
# 5 type 

x = 100 
def f():
    y = x+5
    print(y)
z = 300
print(z)
f()
print(x)


# AGRUMENT CONCEPT 
#  type 1

def f(a,b,c,d):
    print(a*b/c-d)
f(10,20,30,40)      # this is postional argument 
f(20,40,10,20)       #if postion change then ans  will be change

#type 2

def f(a,b,c,d):
    print(a*b/c-d)
f(b=20,a=10,d=40,c=30)   # this is keyword agrument  if we change postion
f(a=20,b=10,c=40,d=30)   #  then ans not change bcz define key values 