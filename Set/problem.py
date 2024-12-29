
# Q 1.write a python script to print all distinct element of a list . use set

# l = [int(e) for e in input("Enter the number sep by comma").split(",")]
# for i in set(l):
#   print(i,end=" ")

# Q2. create two sets from a given set of number to seprate even  and odd numbers
# l = set()
# l1 = set()
# s = [ int(e) for e in input("Enter the Numbers sep by comma").split(",")]
# for i in s:
#   if i%2==0:
#     l.add(i)
#   else:
#     l1.add(i)
# print( "Even Number set ",l,end=" ")
# print( "Odd Number set ",l1,end=" ")

# Q3. Given a set of five players write a python script to form all possible pair
#  of player that selecting  two player at a time 
i = 0
s = {"Rohit","Virat","Surya","MS Dhoni","Yassavi"}
for p1 in s:
  i+=1
  for p2 in list(s)[i::]:
    print(p1,p2)
