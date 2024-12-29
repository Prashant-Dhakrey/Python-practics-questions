
"""
# Q 1. write a python function  to remove duplicate element from a given list(TSRS)
# SOL...

def f(l):
    s = set(l)
    print(l)
    return s
l = [int(i) for i in input("enter the numbers sep by comma").split(",")]
t = f(l)
print(t)
"""

# Q 2 write a python function to count frecuquecy of each element of the list and
# store list element in the dict object as key and element frequrcy as data value
# sol...>

def frequecyDict(mylist):
    d = {}
    i = 0
    while i<len(mylist):
        if mylist.index(mylist[i])==i:
            f = mylist.count(mylist[i])
            d[mylist[i]]=f
        i = i+1
    return d

print(frequecyDict([10,20,1,0,10,20,10,20,30,40,50,20 ]))                


# Q 3. write a python function to find number in a given  text 
# .store number in list and return list (TSRS) // Ans sum of 3 and 6 is 9 = [3,4,9]
# sol..>

def extractNumberFromText(text):
    num = []
    for word in text.split(' '):
        try:
            x = float(word)
            num.append(x)
        except:
            pass
    return num
print(extractNumberFromText("sum of 3 and 4 is 7"))

# Q 4. write a python to find largest sorted sub sequence in a givn list .
# return the largest sub sequence as a list (TSRS)
# sol.>. like [1,2,5,4,6,7,8,9,3,0] // sbse bda sub seq 6,7,8,9



# Q 5.write a python to check if two given list have same element in any order 
# or not True and  False 
# sol...>

def compare(l1,l2):
    if sorted(l1) == sorted(l2):
        return True
    else :
        return False

l1 = [2,6,3,8,1,4]
l2 = [1,2,3,7,6,5]
print(compare(l1,l2))

l1 = [1,3,5,2,4,6]
l2 = [3,4,2,1,6,5]
print(compare(l1,l2))

    


# Q 4. write a python a function to print fist N  term of fibbonaci series(TSRS)
# sol...>

def fib():
    n = int(input("enter the number "))
    a = -1
    b = 1
    for i in range(1,n+1):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
fib()
print()

# Q 5. write a python function to print all factore of given number (TSRS)
# sol....>
def f3():
    n = int(input("enter the number "))
    for i in range(1,n+1):
        if n%i==0:
            print("Factor is ",i,end=" ")
f3()


# Assignment 4 Q Questions

# Q 4. write a python function to filter out words from a text 
# starting from same alphabet and store them in a list . 
# Now create a dict with alphabets as key - value and list of words starting from 
# that alphabet as data values . Text as an argument and return dict object (TSRS)
# sol...>











# Q 5. write a python function to find all comman factors of two given number.
# return a tuple of such factore (TSRS)
# sol...>






