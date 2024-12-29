
# Vriable length arguments ==> *n

# Ex-1

def f1(*n):     # *n means one many given arguments 
    sum =0
    for i in n:
        sum = sum + i
    return sum 

a=f1()
print(a)
b=f1(10)
print("sum is",b)
c=f1(10,20)
print("sum is ",c)
d=f1(10,20,30)
print("sum is ",d)
e=f1(10,20,30,40,50)
print("sum is ",e)
print()

# Ex-2
def f2(*n):
    for element in n:
        print(element,end=" ")
f2()
f2(1,2,"Prashant ","Sweety",21,20)

# Variable length kwargs argument 

# Ex-1

def f(**n):
    for k,v in n.items():
        print("key is ", k , "value is ",v)
f(a=21,b="prashant",c="sweety",d = 19.50)

# Ex-2
def f(**d):
    for k , v in d.items():
        print(k,"_",v)
f(a=1,b = 2,c =3,d =4)
         
         
def f(*t):
    print(t)
t = (10,20,30,40,50)
f(*t)    # ye same  value return kar dega (10,20,30,40,50) BUT
f(t)    # ye complete value ko tuple ke form dega ((10,20,30,40,50),) 
        # Because ye jo function me t hai [(def f(*t))] bo bhi ek tuple hi hai isliye
