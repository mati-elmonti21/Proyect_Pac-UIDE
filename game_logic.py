posX1 = 1
posY1 = 3

while True:
    direccion1 = (input("Leer Direccion1 (ARRIBA, ABAJO, IZQUIERDA o DERECHA), escriba ESC para salir: ").upper().strip())

    if (direccion1 == "ARRIBA" or direccion1 == "ABAJO" or direccion1 == "IZQUIERDA" or direccion1 == "DERECHA"):
        nuevaX = posX1
        nuevaY = posY1
        if direccion1 == "ARRIBA":
            nuevaY = posY1 - 1
        elif direccion1 == "ABAJO":
            nuevaY = posY1 + 1
        elif direccion1 == "IZQUIERDA":
            nuevaX = posX1 - 1
        elif direccion1 == "DERECHA":
            nuevaX = posX1 + 1

        if nuevaX <= 0 or nuevaX >= 18 or nuevaY <= 0 or nuevaY >= 16:
            print("Jugada inválida por las reglas: hay una pared.")
        else:
            posX1 = nuevaX
            posY1 = nuevaY
    elif direccion1 == "ESC":
        print("Saliendo...")
        break
    else:
        print("Jugada inválida por formato.")


print("Posición final jugador 1:", posX1, posY1)

print("Continuando con el jugador 2")

posX2 = 17
posY2 = 13

while True:
    direccion2 = (input("Leer Direccion2 (ARRIBA, ABAJO, IZQUIERDA o DERECHA), escriba ESC para salir: ").upper().strip())

    if (direccion2 == "ARRIBA" or direccion2 == "ABAJO" or direccion2 == "IZQUIERDA" or direccion2 == "DERECHA"):
        nuevaX = posX2
        nuevaY = posY2
        if direccion2 == "ARRIBA":
            nuevaY = posY2 - 1
        elif direccion2 == "ABAJO":
            nuevaY = posY2 + 1
        elif direccion2 == "IZQUIERDA":
            nuevaX = posX2 - 1
        elif direccion2 == "DERECHA":
            nuevaX = posX2 + 1

        if nuevaX <= 0 or nuevaX >= 18 or nuevaY <= 0 or nuevaY >= 16:
            print("Jugada inválida por las reglas: hay una pared.")
        else:
            posX2 = nuevaX
            posY2 = nuevaY
    elif direccion2 == "ESC":
        print("Saliendo...")
        break
    else:
        print("Jugada inválida por formato.")


print("Posición final jugador 2:", posX2, posY2)

puntosj1 = input("Puntos Jugador 1: ").strip()
puntosj2 = input("Puntos Jugador 2: ").strip()

if int(puntosj1.isdigit()) and int(puntosj2.isdigit()):
    j1 = int(puntosj1)
    j2 = int(puntosj2)
    if j1 > j2:
        print("El jugador 1 ha ganado")
    elif j1 < j2:
        print("El jugador 2 ha ganado")
    elif j1 == j2:
        print("Empate")
    else:
        ("Cantidad de puntos inválida")
else:
    print("Cantidad de puntos inválida")
