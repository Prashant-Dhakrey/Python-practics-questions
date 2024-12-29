

#Q1. write a python script revser a words wise 
#sol>..
s = input("enter the string")
l = s.split()
print(l[::-1])

#Q2.whrite a python script to extract () numbers
# from a given text and store all the numbers in a list
# sol>....

l = []
s = int(input("enter tne number"))
l.append(s)
print(l,sep =",")


#Q3. write a python script to check palindrom or not 5q
#sol>...

s = input("enter the string" )
if s == s[::-1]:
    print("yes this is pellodrom")
else:
    print("not pellodrom")

#second method 




#Q4. write a python script to transeform a given string to uppercase
#so>...
 
s = input("enter the string ")
l = s.upper()
print(l)


#Q5.write a python script to find maximum lenth word in given text
#sol>...

s = input("enter the string")
i =0
index = 0
maxlenth = -1
for w in s.split(' '):
    if maxlenth<len(w):
        maxlenth = len(w)
        index=i
    i+=1
print("maxlenth word is ==",s.split(' ')[index])
print()
        
