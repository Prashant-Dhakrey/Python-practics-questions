
def f1(n):
    if n ==1:
        return 1
    s = n + f1(n-1)
    return s
r = f1(3)
print(r)


def f2(n):
    if n ==1:
        return 1
    s = n*f2(n-1)
    return s
n = int(input("enter the number"))
r = f2(n)
print(r)

#  sum of n number ka program hi 
# sol...>

def f3(n):
    if n==1:
        return 1
    return n+f3(n-1)
n = int(input("enter the number"))
a = f3(n)
print(a)