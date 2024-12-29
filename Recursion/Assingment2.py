
# Q 1. write a recursive function to calculate sum of First N natural number 

def sum(n):
  if n==1 :
    return 1
  
  return n+sum(n-1)
print(sum (10)) 
print()

# Q 2. write a recursive function to calaculate sum of First N odd number 

def sum(n):
  if n==1:
    return 1
  return (2*n-1)+sum(n-1)

print(sum(10))
print()

# Q 3. write a recursive to calculate sum of first even natural number

def even(n):
  if n==1:
    return n
  return (2*n) + even(n-1)

print(even(10))
print()

# Q 4. write a recursive to calculate sum of sequre of Fist N natural number

def sequre(n):
  if n == 1:
    return 1
  return (n**2) + sequre(n-1)

print(sequre(10))
print()

# Q 5. write a recursive to calculate sum of cubes of First N natural number

def cubes(n):
  if n ==1 :
    return 1
  return (n**3) + cubes(n-1)

print(cubes(10))
print()

# Q 6. write a recursive function to calaculate sum of digit of a given number

def sum (n):
    if n == 1:
      return n 
    return n + sum(n-1)
n = int(input("Enter the Number"))
print(sum(n))

# Q 7. write a recursive function to calculate factorial of a given number 

def  fact(n):
  if n== 0 :
    return 0


# Q 10 . write a recursive function to calculate sum of first N Prime Number  


# Q 8. write a recursive fuction to print binary of a given decimal number 



# Q 9 .write a recursive function to print octal of a given decimal number 

