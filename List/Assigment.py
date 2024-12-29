
# Q1 write a python script calculate sum of all element of a list
# sol:

# this method all over sam e programing

n = int(input("enter the number "))
l = []
sum = 0
for i in range(n):
    r = int(input())   # enter the number 
    l.append(r)
print(l)
for j in l:
    sum = sum +j
    print(sum,end=",")
print("total number sum is",sum) 


# this is second method python 
print("enter the number sep by coma")
l=[int(e) for e in input().split(',')]
sum = sum(l)
print(sum)

# Q 2 write a python script to calculate average of element of a list
# sol:
print("ener the number by sep coma")
l = [int(i) for i in input().split(',')]
s= sum(l)/len(l)
print(s)


# Q 3 write a python script to create a list of a squre of element of a given list 
# soll

print("enter the number sep by coma  ")
l =[int(e) for e in input().split(',')]
l2 = [e**2 for  e in l]
print(l2)


# Q 4 write a python script to sort list element in decreesing order 
# sol:
print("enter the number by sep coma ")
l =[int(e) for e in input().split(',')]
l.sort(reverse=True)
print(l)


# Q 5 write  a python script to create a list from a given list 
# by selecting only even place element 

# using slicing 1st method  this is print even places values

print("enter the number by sep coma ") 
l=[int(e) for e in input().split(',')] 
print(l)
for i in l[0::2]:
   l=[ print(i,end=',')]

#2nd method this is print even places index 

print("enter the number by sep coma ") 
l=[int(e) for e in input().split(',')] 
print(l)
i = 0
l1=[]
for e in l:
    if i%2==0:
        l1.append(e)
    i=i+1
print(l1)  
   
    