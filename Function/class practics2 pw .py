

#  WE CAN TAKE ANY AGRUMENT THEN WE USE *n(variable length) in FUNCTION
def f(*n):
    sum = 0
    for ele in n:
        sum = sum + ele
    print(sum)
f()
f(10)
f(10,20)
f(30,12.5)

#type 2
def f(*n):
    for i in n:
        print(i,end=" ")
f(10)
f(10,20,30,40)
f("prashant","dhakrey")

# GENRAL FORM

def f(*t):
    for i in t:
        print(i,end=" ")
f()



# lembda function use 
s = lambda x: x*x*x
print(s(3))

# agr ham function ka use kare
def f(a,b):
    return a*b
print(f(10,20))

# agr ham lembda ka use kare  

s = lambda a,b: a*b
print(s(10,20))

# lambda argument expresion 
t= lambda x,y: x if x<y else y
print(t(10,30))
print(t(40,30))

# use function type FILTER 

def f(x):
    if x%3==0:
        return True
    else:
        return False
t = list(filter(f,[10,20,30,40,50,63]))
print(t)

#  using with lambda function in filter 

t = list(filter(lambda x:x%3==0,[10,20,30,40,50,63]))
print(t)        # agr hame ek hi jgh use  karna  hai means ek hi  baar
                # use krna hai then we use  better lambda 
        
    
#  use function type 2 MAP

def f(x):
    return x*x*x
t = list(map(f,[1,2,3,4,5]))
print(t)       # isme jitne element diye utne hi output me milege with modification

#  using with lambda function in Map

t = list(map(lambda x:x*x*x,[1,2,3,4,5]))

# we have two given list then add with the help map function come output in list
a =[1,2,3,4,5]
b=[11,12,13,14,15]
t = list(map(lambda x,y: x+y,a,b))
print(t)

