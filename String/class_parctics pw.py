
'''
a = "prashant"
b= "pankaj"
c = "dhakarey"

print(a)
print(b)
print(c)
d="prashant'dhakrey"
print(d)
print(a[0])   #index 0,1,2,3,....
print(a[1])    
print(a[3])
#print(a[8])
print(a[-1]) # negative index -1,-2,-3,....

for i in range(len(a)):
    print(i,a[i])

for i in range(len(a)):
    print(i-len(a),a[i-len(a)])
    
print(a[:])
print(a[:6])
print(a[2:])
print(a[1:5])
print(a[3:1])
print(a[3:3])
print(a[1:100])
print(a[4:1:-1])
print(a[-2:-5:-1])

m = "prashant dhakrey"
print(m[: :-1])
print(m)
print("prashant" in m)
print("sweety" in m)
print('p' in m)
print(len(m))
print(max(m))
#print(min(m))
#print(sum(m))



# pellondrom 
s= input("enter the  the string")
if s[::-1]==s:
     print("YES THIS PELONDROM")
else:
    print("NOT ")
 

s= "    prashant   "
print(len(s))
update = s.rstrip()
print(len(update))
update_1 = s.lstrip()
print(len(update_1))
update_2 = s.strip()
print(len(update_2))
'''

# split()
s = "prashant dhakrey is bad boy"
l = s.split()
print(l)
print(type(l))

