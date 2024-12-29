
# Q 1. write a recursion function to print N natural number 

def naturalNumbers(n):
  if n>0:
    naturalNumbers(n-1)
    print(n, end =" ") 
naturalNumbers(15)
print()

# Q 2. write a recursive function to print N natural number in revrse order

def nRevrse(n):
  if n>0:
    print(n,end=" ")
    nRevrse(n-1)

nRevrse(15)
print()

# Q 3. write a recursive function to print first N odd Natural number 

def OddNatural(n):
  if n>0:
    OddNatural(n-1)
    print(2*n-1,end=" ") # this given like 10 odd 
         #  or 
#     if n%2!=0: # this is given  10 tak ke odd number
#       print(n)

OddNatural(20)
print()

# Q 4. write a recursive func to print first N odd natural number in reverse order

def OddNumber(n):
  if n>0:
    print(2*n-1,end = " ")
    OddNumber(n-1)

OddNumber(10)
print()

# Q 5. write a recursiver function to print MysirG N times on the screen

def PrintMysirG(n):
  if n>0:
    print("MysirG")
    PrintMysirG(n-1)
PrintMysirG(5)

# Q 6. write a recusive function to print N even natural number

def even(n):
  if n>0:
    even(n-1)
    print(2*n,end=" ")
even(10)
print()

# Q 7. write a recursive function to print N Even Number in reverse order 

def evenReverse(n):
  if n>0:
    print(2*n,end=" ")
    evenReverse(n-1)

evenReverse(10)
print()

# Q 8. write a recursive function to print Sequre of First N natural number 

def sequre(n):
  if n>0:
    sequre(n-1)
    print(n**2,end =" ")

sequre(10)
print()

# 9. write a recursive function to print cubes of first N natural number

def cubes(n):
  if n>0:
    cubes(n-1)
    print(n**3,end = " ")
  
cubes(10)
print()

# Q 10 write a recursive function to print reverse of the given number

def reverse(n):
  if n>0:
    print(n,end =" ")
    reverse(n-1)

n = int(input("Enter the Number"))
reverse(n)
print()