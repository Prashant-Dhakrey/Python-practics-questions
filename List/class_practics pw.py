'''

l =[]
print(type(l))

for i in range(1,6):
    l.append(i)
print(l)

r=eval(input("enter the list"))
print(r)


#n = input("enter the number")
s = input("enter the number by sperate space").split()
l=[]
for i in s:
    l.append(int(i))
print(l)

# when enter the number hen give a ist on number 

n = int(input("enter the number "))
l = []
for i in range(1,n+1):
    l.append(i)
print(l)


# enter the number by use in by one
n = int(input("enter the number"))
l = []
for i in range(n):
    r = int(input())
    l.append(i)
print(l)

'''
# 
l = []
for i in range(5):
    l.append(0)
print(l)   # ans is given zero list

# second method

l = [0 for i in range(5)]  # given a ans list zero like [0,0,0,0,0]
print(l)

#same work
l = [i for i in range(5)]  # then give a ans list like [0,1,2,3,4]
print(l)

# same
l = [2*i for i in range(5)] # then give a  ans list like [0,2,4,6,8]
print(l)

# same
l = [2*i-1 for i in range(5)] # then give a  ans list like [-1,1,3,5,7]
print(l)

# apeend method 

l = []
l.append(100)
print(l)   # output [100]

l.append(200)
print(l)     #output [100,200]

l.append("pankaj")
print(l)     #output [100,200,"pankaj"]

#   insert method

l.insert(0,"prashant")
print(l)      # ouput ["prashant",100,200,"pankaj"]

l.insert(2,999)
print(l)       #output ["prashant",100,999,200,"pankaj"]

l.insert(50,"dhakrey")
print(l)      # 50 index doesnot exit then insert last me add ho jayega 
              #output ["prashant",100,999,200,"pankaj","dhakarey"] 
              
# extend method 
a =[1,2,3]
b =[4,5,6]
a.extend(b)
print(a)
print(b)