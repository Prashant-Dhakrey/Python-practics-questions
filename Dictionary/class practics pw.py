
'''

d ={}
print(type(d))
d ={1:"prashant",2:"vivek",3:"ajeet"}
print(d)


# when given a pair of value then create a dict
d =[(1,"prasahnt"),(2,"dhakrey"),(3,"ajeet"),(4,"dhakrey")] 
d =dict(d)
print(d)

#agr  hme ek dict banani hai but key hm provide karna  hai tab ham 
# .FROMKEYS  ka use karge

d = dict.fromkeys(["prashant",12,35.5])
print(d) 


# out put none ki hme koi particuler value deni hai tab

d = dict.fromkeys(["prashant",12,35.5],0)
print(d) 

# if  ham duplicate value ke pair de tof ast bala means update bala value ayega 
d = [(1,"ram"),(2,"syam"),(1,"seeta"),(1,4)]
d = dict(d)
print(d[2])

d = {1:"ram",2:"syam",3:"raavan",4:"seeta"}
for x in d:
    print(x)       # it returns are keys only
    print(d[x])    # it returns are only values
    print(x,d[x])  # it retuen are both key and values


# agr hame value update karna hai to 
d[1] ="krashna"
print(d)

# Q1 find the frequency(means how many time repaet every words) of every  words in this string
s = input("enter the string")
l=s.split()  # we convert in list
d ={}
for word in l:
    d[word] = d.get(word,0)+1
print(d)


# Q2 given string  print frequency for ecah charcter 
t = input("enter the string")
l=list(t)
#print(l)
s ={}
for i in l:
     s[i]=s.get(i,0)+1
print(s)  
'''
# whether find thet s2 is subset of s2
s1 = {1,2,3,4.5,6,8}
s2 = {2,4,5}
for i in s2:
    if i in s1:
        print("yes")
        break
    else:
        print("no")
        
        
    