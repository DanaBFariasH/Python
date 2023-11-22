import random 

print("En este juego es vas a tener que adivinar el número que yo elija.")

númeroComputadora = random.randint(1,10)

listaNúmeros = []
while True:
    númeroAdiv = int(input("Ingrese el número que pienses que es:"))
    listaNúmeros.append(númeroAdiv)
    
    if númeroComputadora > númeroAdiv:
        print("Muy bajo, intenta con uno mas alto")
        
    elif númeroComputadora < númeroAdiv:
        print("Muy alto, intenta con uno mas bajo")
        
    elif númeroComputadora == númeroAdiv:
        print("Felicitaciones, Ganaste el juego!!!")
        print(listaNúmeros)
        break
    
print("Fin del Juego")
