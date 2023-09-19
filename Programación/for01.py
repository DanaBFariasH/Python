listaBase= []
listaAltura= []
listaArea= []

print ("este programa calcula el area de redtangulos y los compara. ")

cantidad = int(input("cuantos rectangulos quiere comparar?"))

for i in range (cantidad):

    base = int(input(f"ingrese la base del rectangulo {i+1}:"))
    listaBase.append(base)

    altura = int(input(f"ingrese la altura del rectangulo {i+1}:"))
    listaAltura.append(altura)
    
    area = base * altura  
    listaArea.append(area)

print(listaArea)
print(listaAltura)
print(listaBase)

listaArea.sort()
print(listaArea)
    
    
    #print (f"el area del rectangulo {i+1} es {area}")