a = int(input("ingrese el primer numero:"))
b = int(input("ingrese el segundo numero:"))

def menu():
    opcion = int(input("ingrese 1 para sumar y 2 para restar:"))
    if opcion == 1:
        suma()
        print(suma())
    elif opcion == 2:
        resta()
        print(resta())

def suma():
    return (a+b)

def resta():
    return (a-b)

menu()

        