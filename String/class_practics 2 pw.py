# join method 

m = ['prashant','dhakarey','is','bad','boy']
r=' '.join(m)
print(r)

S = "pankaj sharma  sir "

for i in S.split():
    if len(i)%2==0:
        print(i)
        
        
# if we print p s sir 
l = S.split()
update = []
for word in  l[:len(l)-1]:
    update.append(word[0])
update.append(l[len(l)-1])
print(update)

print(' '.join(update))
    
    
# find methods 

s = "pankaj sir is pankaj sir "
print(s.find("pankaj"))
print(s.find("is"))
print(s.find("ankit"))
print(s.find("pankaj",6))

# index method 

print(s.rfind("pankaj"))
print(s.rfind("ankit"))

# count method 

print(s.count("pankaj"))
print(s.count("pankaj",1,len(s)))

# replace method 

s = "pankaj sir is a good faculty"
t = s.replace("pankaj","Baba")
print(t)
print(s)


n= "pankaj sir is a good faculty"
l = s.split()
print(l)
for i in l[::-1]:
    print(i,sep="")
    
# second method 
t = n.split()
x = ' '.join(t[::-1])
print(x)

t = input("ener the  string ").split()
x = ' '.join(t[::-1])
print(x)

# latter in revese order 
l = []
t = input("enter the string").split()
for i in t:
    l.append(i[::-1])
print(l)
x =' '.join(l)
print(x)
    
