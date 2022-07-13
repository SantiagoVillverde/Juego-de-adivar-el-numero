from random import *

aleatorio = randint(1, 100)
intentos = 0
decision = 0
nombre_jugador = input("Dime cual es tu nombre: ")

print(f"Bueno {nombre_jugador}, pense en un numero entre el 1 y el 100\nTienes 8 intentos para adivinarlo")
print("\n")


while intentos < 8:
    decision = int(input("Cual es el numero?: "))
    intentos += 1
    if decision not in range(1, 101):
        print("El numero elegido no esta dentro del rango del 1 al 100")
    elif decision < aleatorio:
        print("Mi numero es mayor")

    elif decision > aleatorio:
        print("Mi numero es menor")

    elif decision == aleatorio:
        print(f"Felicitaciones ´{nombre_jugador} ganaste!!!, te tomo {intentos} intentos")
        break

if decision != aleatorio:
    print(f"Te has quedado sin intentos, el numero secreto era {aleatorio}")
