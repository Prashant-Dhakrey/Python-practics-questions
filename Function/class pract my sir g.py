def f1():
    a = int(input("enter the number"))
    b = a**2
    print("squre of ",a, " is =",b)

f1()

# agr hme ek function se dusare functon ki value use karni hai 
# then called take something fintion 

def f2(y): # Here y = x x ki value y me store ho gyi ab then print value y and y seq 
    #c = int(input("enter the number"))
    d=y**2
    print("sequre of",y,"is",d)
    
def start():
    x=5      # agr hme x=5 ka seq print krna hai then take agrument in f2 function  
    f2(x)
start() 

# Types of Function use    

#  Type 1
# Takes Nothing and Return Nothing

def add():
    print("enter the number ")
    a = int(input())
    b = int(input())
    c = a+b
    print("sum is ",c)
    
add()

# Type 2
# Takes Something and Return Nothing

def add(a,b): # a,b are formal arguments
    c = a+b
    print("sum is ",c)
add(10,20)  # 10,20 are actual arguments

# Type 3 
# Takes Nothing AND Return Something
def add():
    print("enter the number")
    a= int(input())
    b = int(input())
    c = a+b
    return c
add()

# Type 4 
# Takes Something And Return Something

def add(p,q):
    c = p+q
    return c
add(50,60)



    
    