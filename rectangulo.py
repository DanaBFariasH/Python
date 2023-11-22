class Rectangulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def calcular_area(self):
        self.area = self.longitud * self.ancho
        return self.area
    def calcular_perimetro(self): 
        self.perimetro = self.longitud + self.ancho * 2
        return self.perimetro
        
Obj1 = Rectangulo (5,3)
print(Obj1.calcular_area())
print(Obj1.calcular_perimetro())