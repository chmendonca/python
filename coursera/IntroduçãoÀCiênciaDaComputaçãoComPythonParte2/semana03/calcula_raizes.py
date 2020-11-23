import math

class Bhaskara:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(self.a,self.b,self.c)
    # def __init__(self):
    #     self.a = float(input("Digite o valor de a: "))
    #     self.b = float(input("Digite o valor de b: "))
    #     self.c = float(input("Digite o valor de c: "))  
        print(self.calcula_raizes())
        
    def delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def calcula_raizes(self):
        d = self.delta()
        if d == 0:
            raiz1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            print("Somente uma raíz: %s" %raiz1)
            return 1, raiz1
        else:
            if d < 0:
                print(" Esta equação não possui raízes reais")
                return 0
            else:
                raiz1 = (-self.b + math.sqrt(d)) / (2 * self.a)
                raiz2 = (-self.b - math.sqrt(d)) / (2 * self.a)
                print("A primeira raiz é: %s" %raiz1)
                print("A segunda raiz é: %s" %raiz2)
                return 2, raiz1, raiz2

