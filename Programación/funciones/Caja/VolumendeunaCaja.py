print("Este programa calcula el volumen maximo de una plancha de carton")

ancho = float(input("ingrese el ancho de la plancha de carton: "))
largo = float(input("ingrese el largo de la plancha de carton: "))
alto = 1 # modifica
volumen = (ancho - 2 * alto) * (largo - 2 * alto) * alto

while ancho - alto * 2 != 0 or largo - alto * 2 != 0:
    volumen = (ancho- 2*alto) * (largo- 2*alto) * alto
    alto = alto + 1
    volumenMaximo = (ancho - 2 * alto) * (largo - 2 * alto) * alto
    if volumen < volumenMaximo:

        print(f"el volumen de la caja es: {volumen}")
        break


#for alto in range 

