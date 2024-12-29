
# Q 1 sequre partten
n = 5 
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()

# Q 2 Holoow sequre parrten 

size = int(input("enter the size"))
for i in  range(size):
    for j in range(size):
        if i ==0 or i==size-1 or j ==0 or j==size-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

# Q3  left tringle parrtern

n = int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

# Q 4 right tringle parrten 






# Q 5. Hellow tringle partten 







#Q6 left downword  tringle parrtten 
n = int(input("enter the number"))
for i in range(n+1,1,-1):
    for j in range(i+1,1,-1):
        print("*",end=" ")
    print()
print()

# Q 7. pyramid pratten 





