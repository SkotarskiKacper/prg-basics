def Factorial(n):
    
    if n==0:
        return 1
    
    return Factorial(n-1)*n

Approximation=0
Iteratons=50

for i in range(Iteratons):
    Approximation+=1/Factorial(i)

print(f"e~{Approximation} for {Iteratons} iterations")