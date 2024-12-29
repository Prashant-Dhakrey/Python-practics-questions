
# Q 1 write a python  function to print first N odd natural number (TSRS)
# sol >....

def odd():
    n = int(input("enter the number"))
    for i in range(1,n+1):
        if i%2 != 0:
            print("number is odd",i)

odd()
print()

# Q 2 write a python function to print first N prime number (TSRS)
# sol..>

    
#panding both questions

def prime(n):
    n = int(input("enter the number "))
    for i in range(2,n):
        if n %i == 0:
          return False
    return True  
               

# Q 3 write a python fnction to print all prime number of beetwen two given number 
# sol...>
                     # first of all check number is prime or not 
def prime(n):
    for i in  range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input("enter the number"))
a = prime(n)
print(a)

def printisprime(a,b):
    x = a+1
    while x<b:
        if prime(x):
            print(x,end=" ")
        x = x+1  # increment  x
printisprime(10,20)



# Q 4 wite a pyhton function to print first N term of fibbonacci series (TSRS)
# sol...>

def fibbonaci():
    a =-1
    b = 1
    l = []
    n = int(input("enter the numbe"))
    for i in range(0,n+1):
        c = a+b
        l.append(c)
        a = b
        b = c
    return l
d = fibbonaci()
print(d)
         
# Q 5 write a python to function print all factore of given number (TSRS) 
# sol..>

def factore():
    l = []
    n = int(input("enter the number"))
    for i in range(1,n+1):
        if n % i==0:
            l.append(i)
    return l
a = factore()
print(a)

# Q 6. write a python to function to caculate LCM  of two number (TSRS)
# sol..>

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            break
    l+=1
    return l
print(lcm(4,6))


# Q 7. write a python  to function to count letter  in string 
# sol...>

def countletters():
    n = input("enter the string ")
    count = 0
    for i in n:
        if i != " ":
            count = count+1
    return count
a = countletters()
print(a)
  
# Q 8. write  a python to function to count word in string 
# sol.......>'

def countwords():

    count=0
    l = n.split()
    #for i in input().split(): or 
    for i in l :
        if i != 0:
            count= count+1
    return count

n = input("enter the string")
a = countwords(n)
print(a)

#   OR 
def countwords(s):
    return len(s.split(" "))
print("number of words",countwords(input()))

# Q 9. write a python to function to create a list of first prime number beetween 
# two given numbers(TSRS)
# sol....
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def primeList(a,b):
    for x in range(a+1,b):
        if prime(x):
            print(x,end=" ")
            
            # OR both are concept same 
            
        #return [int(x) for x in range(a+1,b) if prime(x)]
    
print(primeList(10,20)) 

#Q 10. write a python fuction to find all the commman factor of two given number
#return a tuple of such factors (TSRS)

def commanFactores(a,b):
    l = []
    f =a if  a<b else b
    while f >= 1 :
        if a%f == 0 and b%f==0:
            l.append(f)
        f -=1
    return tuple(l)
print(commanFactores(40,60))
print()
