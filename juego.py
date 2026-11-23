opcion = input("""
Pac-Man UIDE
Elija una opción 
1. Un Jugador | 2. Multijugador | 3. Salir
""").strip()
while opcion != "3":
    if opcion == "1" or opcion == "2":
        print("Se programará en la fase 4")
    else:
        print("Opción Inválida")
    if opcion == "3":
        break
    opcion = input("""
Pac-Man UIDE
Elija una opción 
1. Un Jugador | 2. Multijugador | 3. Salir
""")
print("Hasta pronto")
