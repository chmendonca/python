class Triangulo:
    def __init__(self,l1,l2,l3):
        self.a = l1
        self.b = l2
        self.c = l3
    
    def perimetro(self):
        perimetro = int(self.a + self.b + self.c)
        return perimetro

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isósceles'
