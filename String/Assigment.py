
# Q 1.write a python to check if a given string has only alphabates in it
#sol>>...

s = input("enter the string")
for i in s:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        pass
    else:
        print("not all alphabets")
        break
else:
    print("string conatin ony alphabets")     
        
#Second Methods 



 
# Q2. write a python script to check 
# if a given character is present in a given string or not

s =input("enter the string")
r = input("ente the chachter ")
if r in s:
    print(r,"this is present in string")
else:
      print(r,"this is not present in string")
    
  
# Q3.write a python script to count vowels in stringprashant

s = input("enter the string")
r = "aeiouAEIOU"
count = 0
for i in s:
    if i in r:
        print(i)
        count = count+1 
print("vowels are in string",count) 



#Q4. write a python script to count words in a given string
#sol>...

s = input("enter the string")
# s.strip()      # we are not use in strip then working 
l = s.split(' ')
print(l)
i =0
count =0
while i<len(l):
    if l[i]!='':
        count+=1
    i+=1
print("total word in string",count)
 
#for loop not workin int iterables
s = input("enter the string")
# s.strip()      # we are not use in strip then working 
l = s.split(' ')
print(l)
#i =0
count =0
for i in len(l):
    if l[i]!='':
        count+=1
    i+=1
print("total word in string",count)      



#Q5. write a python script reverse of string 
#sol>...

s = input("enter the string ")
print(s[::-1])   # latters ka reverse 
l=s.split()
print(l[::-1])   # words ka reverse then use split then  print