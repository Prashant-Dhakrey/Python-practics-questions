
# Q1 write a python scrip to remove all non int values from list
#sol>..

l =[20,20.5,"prashant",3+4j,10,30]
i=0
l1=[]
while(i<len(l)):
    if type(l[i])==int:
        l1.append(l[i])
    i=i-1
print(l1)
print()


# Q2 write a python script to print distinct element along with 
# thier frequencey (means kitni every element a rha hi) of occrence a the list
#sol>...

# 1st method when give random num then find a particular one element frequency
n = int(input("enter the number"))
l = []
for i in range(1,n+1):
    r = int(input())
    l.append(r)
print(l)
print(l.count(10)) 

# But 2nd we have a given list the in every num find frequency
l1 =[10,20,10,30,20,10,40,50,20,30]
i =0
for x in l1:
    if i==l1.index(x):
        print(x," ",l1.count(x))
    i=i+1

# Q3 write a python script to sort a list of string
#sol>..
l=["agra","mathura","aighar","hathrash"]
l.sort()
print(l)


# Q4 write a python script to find first repeated string in list of sring 
# sol>...



#Q5 write a python script to count string which ends at chapter's in a list of string 