import math

def Fact(n):
    if n==0:
        return 1
    else:
        return n*Fact(n-1)

def PiApprox(n):
    sum=0
    for i in range(n):
        sum+=1/(i+1)**2

    return math.sqrt((sum)*6)

def EApprox(n):
    sum=0
    for i in range(n):
        sum+=1/Fact(i)

    return sum

print("pi~~",PiApprox(100000))
print("e~~",EApprox(100))