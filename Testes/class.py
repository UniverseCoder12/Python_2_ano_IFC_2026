class tri:
    def __init__(self,b,a):
        pass
        self.base = b
        self.altura = a
#       self.area = (b*a)/2
    def area(self):
        return(self.base*self.altura)/2

t = tri(10,5)
t2 = tri(20,10)
print(f"Area do triangulo 1: {t.area()}")
print(f"Area do triangulo 2: {t2.area()}")