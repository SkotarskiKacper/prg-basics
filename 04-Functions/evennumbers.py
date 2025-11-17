def SumOfEven(n):
    sum=0
    for i in range(0,n,1):
        if not i%2==1:
            sum+=i

    return sum

print(SumOfEven(11))