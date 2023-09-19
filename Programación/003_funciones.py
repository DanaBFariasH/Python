import math

print("Este programa calcula el area correspondiente de una figura geometrica")

menuInicio = '''
        
        ****************************
        *     1-Rectangulo         *
        *     2-Triangulo          *
        *     3-Circunferencia     *
        *     4- Salir             *
        ****************************
        '''

def Rectangulo():
    Altura = float( input("ingrese el valor de la altura del rectangulo:"))
    Base = float(input("ingrese el valor de la base del rectangulo:"))
    Area = Altura * Base / 2
    print("El area del Rectangulo es", Area) 

def Triangulo():
    Altura = float(input("ingrese el valor de la altura del Triangulo:"))
    Base = float(input("ingrese el valor de la base del Triangulo:"))
    Area = Altura * Base / 2
    print("El area del Triangulo es", Area) 

def Circunferencia():
    Altura = float(input("ingrese el valor del area de la Circunferencia:"))
    Base = float(input("ingrese el valor del radio de la Circunferencia:"))
    Area = math.pi*radio**2
    print("El area de la Circunferencian es", Area) 




def menu ():
    print(menuInicio)
    opción = int(input("Ingrese la opción deseada:"))
    if opción == 1:
        Rectangulo()
    elif opción == 2:
        Triangulo()
    elif opción == 3:
         Circunferencia()
    elif opción==4:
        return(opción)


    

while True:
    if menu() ==4:
        break
    menu()
    



    
