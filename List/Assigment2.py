
# Q1 write a pyhton  script to create a list of first N even natural number 
#sol.
# norma method 
n = int(input("enter the number "))
for i in range(1,n):
    l = print(2*i,end=',')

# 2nd method 
n = int(input("enter the number"))
l =list(range(2,2*n+1,2))
print(l)

 #    or sort 
l = list(range(2,2*int(input("enter the number"))+1,2))
print(l)

# Q 2 write a python  scrip to create a list of first N  of  fibbonaci  series
# sol: 0,1,1,3,5,8,13,21,34.... this is fibbonaci 

a = -1
b = 1
l = []
n = int(input("enter the number"))
for i in range(0,n):
        c = a+b
        l.append(c)
        a=b
        b=c
print(l,end='')
  

        
# Q 3 write a python script to create a list of first prime number 
# sol:
n = int(input("enter the number "))
for i in range(2,n):
    if i%i==0:
        print(i,end=',')   # this is not complete 
      
       
        
# Q 4 write a python script to add matrices 
# each of order 3*3 store  matrix element in a list of lists 
# sol.
print("enter the 9 element first matrix  [row wise]")
m1=[
    [int(e) for e in input().split(',')],
    [int(e) for e in input().split(',')],
    [int(e) for e in input().split(',')]
 ]
print("enter the 9 element second metarix [row wise]")
m2=[
    [int(e) for e in input().split(',')],
    [int(e) for e in input().split(',')],
    [int(e) for e in input().split(',')]
 ]
c =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        c[i][j]=m1[i][j]+m2[i][j]
        print(c[i][j],end =",")
    print()
print()




#Q5 write a python script to create two list from a given list of number in sach way 
# that the first list can have only positive number and 
# second list can have only non  positive number 


# when jab ham number de one by one then in output two list one positive & non positive
l1 = []
l2 = []
n = int(input("enter the number "))
for e in range(1,n):
    p = int(input())
    if p%2==0:
        l1.append(p)
        print(l1)
    else:
        l2.append(p)
        print(l2)
    print(l1,l2)
print(l1,l2)

        
# 2nd method => ek number or bha tak all number are give sep list postive & non postive
l = []
l1=[]
n =int(input("enter the number "))
for i in range(1,n):
    if i%2==0:
        l.append(i)
    else:
        l1.append(i)
print(l,l1)

    