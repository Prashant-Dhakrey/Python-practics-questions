
# Map() function
 
def squre(a):
    return a*a
x =  map(squre,[1,2,3,4,5,6])
print(x)
#l = list(x)   # ya hme list me de skte hai or phir for ke form me 
#print(l)

#      OR
for i in x:
    print(i,end=" ") 
print()

# Filter Function

def f(x):
    if x>=3:
        return x

# y = filter(f,(1,2,3,4,5))
# OR
t = (10,20,0,3,-2,-5,8,7,9)
y = filter(f,t)
l = list(y)
print(l)
print()

# Reduce() Function
from functools import reduce
def add(a,b):
    return a+b
l = [1,2,3,4,5,6,7]
x = reduce(add,l)
print("Sum is ",x)