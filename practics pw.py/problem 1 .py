
#Q 1. find the peak element if return 1 then you ans is right and return 0 then wrong 
# sol>...

n=int(input("enter the number"))
l = []
def peakelement(self,list,n):
    if(n==1):          # spacial case mean only give one element the
     return 0                                 #find peak value of index  
    if(list[0]>=list[1]):   # give only first two elements then find peak element of index
        return 0
    if(list[n-1]>=list[n-2]):  # second last element  then find peak value 
        return n-1
    for i in range(1,n-1):
        if (list[i]>=list[i-1] and list[i]>=list[i+1]):
            d=l.append(i)
            print(d)
            return i
                           # this question is not complete some error 

            
# Q 2. you given a string you need to revese the string
# sol>... 
# 1st method 
s = input("enter the string ")
for i in s[::-1]:
    print(i ,end=" ")
print()


# 2nd method 
n =[1,8,7,4,3,2]
for i in range(0,n//2):
    temp = l[i]
    l[i]=l[n-j-1]
    l[n-j-1]=temp
print(l[i])

# Q 3 given a list then count number is repated
# sol 
l = [1,2,1,3,1,3,4,1,51,4]
l.cont()