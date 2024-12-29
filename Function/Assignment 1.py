

# Q 1 write a python to function to calcluate sum of two number(TSRS)
# sol...>
def sum(a,b):
    c = a+b
    #print("sum is ",c)
    return c 
x=sum(10,20)
print(x)

#Q 2 write a pyhotn to function to calculate area of a circle (TSRS)
# sol...>
def area(r):
    are = 3.14*r**2
    #print("Area is ",are)
    return are  
y =area(10)
print(y)

# Q 3 write a python  to function to calculate average of three Number (TSRS)
# sol...>
def avr(a,b,c):
   return (a+b+c)/3
a = (10,20,30)
print("Average is ",a) 

# Q 4 write a python to funcion to caculate compound interst (TSRS)
# sol...>
def compound_Intrest(p,r,t):
    Amount = p*(1+r/100)**t
    intrest = Amount - p
    return intrest
print(compound_Intrest(1000,2,3))

# Q 5 write a python to function to calculate volume of cubic
# sol...>
def vol(l,b,h):
    volume = l*b*h
    print("Voume is ",volume)
vol(10,20,30)

# Q 6 write a python to function to check if a number is even (TNRN)
# sol...>
def f1():
    x = int(input("enter the number "))
    if x%2==0:
        print("number is even ",x)
    else:
        print("number  is odd")    
f1()
       # if TSRS
         
def f2(x):
    if x%2==0:
        return True
    else: 
        return False
x = f2(10)
print(x)

# Q 7 write a pyhton to function to find amogest three number (TSRS)
# sol...>
def amg(a,b,c):
    if a>b:
        return a
        #print("greter number is ",a)
    elif b>c:
        return b
        #print("greter number is ",b)
    elif c>a:
        return c
        #print("greter number is ",c)
x = amg(10,20,30)
print("Greater number is ",x)

    
# Q 8 write a pythin to check wether number is prime is not prime 
# sol..>
def prime(n):
        for i in  range(2,n):
            if n%i == 0:
                return print("Number is not prime ")
        return print("Number is prime ")
n = int(input("enter the number"))
a = prime(n)
print(a)

# Q 9 write a python to check if an leap year (TSRS)
# sol...>

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year,"is a leap year")
        return True
    else:
        print(year,"is not leap year")
        return False
year = int(input("enter the year"))
leap_year(year)


# Q 10. write a python to caculate factorial of a number'
# sol ..>
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
n = int(input("enter the number "))
a = fact(n)
print(a)