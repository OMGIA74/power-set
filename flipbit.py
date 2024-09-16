def flip(n1,n2):
    flips = 0
    while n1>0 or n2>0:
        t1 = (n1&1)
        t2 = (n2&1)
        if not t1  == t2:
            flips+=1
        n1>>=1
        n2>>=1
    return flips
n1 = int(input("enter the n1: "))
n2 = int(input("enter the n2: "))
print(flip(n1,n2))