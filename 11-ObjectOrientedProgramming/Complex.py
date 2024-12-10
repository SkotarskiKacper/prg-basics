class Complex:

    def __init__(self,Real,Complex):
        self.Real=Real
        self.Complex=Complex

    def Magnitude(self):
        import math
        return math.sqrt(self.Real^2+self.Complex^2)

    def Conjugate(self):
        return self.Complex*=-1

    def __str__(self):
        if self.Complex>=0:
            return f"{self.Real}+{self.Complex}i"
        else:
            return f"{self.Real}-{self.Complex}i"

C1=Complex(3,4)
print(C1.Magnitude())
print(C1)