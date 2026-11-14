import random

def jugar_adivina_numero():
    print("=== JUEGO: ADIVINA EL NÚMERO SECRETO ===")
    
    jugar_nuevamente = "sí"
    
    while jugar_nuevamente.lower() in ["sí", "si", "s"]:
        # 3. Niveles de dificultad
        print("\nSelecciona el nivel de dificultad:")
        print("1. Fácil (1 al 10)")
        print("2. Medio (1 al 20)")
        print("3. Difícil (1 al 50)")
        
        opcion = input("Elige una opción (1, 2 o 3): ")
        
        if opcion == "1":
            limite = 10
        elif opcion == "3":
            limite = 50
        else:
            limite = 20  # Por defecto medio
            
        # Generar número secreto
        numero_secreto = random.randint(1, limite)
        
        # 1. Límites de intentos (máximo 5)
        intentos_maximos = 5
        intentos_realizados = 0
        adivinado = False
        
        print(f"\n¡He pensado un número entre 1 y {limite}! Tienes {intentos_maximos} intentos para adivinarlo.")
        
        while intentos_realizados < intentos_maximos:
            try:
                intento = int(input(f"\nIntento {intentos_realizados + 1} de {intentos_maximos}. Ingresa tu número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue
                
            intentos_realizados += 1
            
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número secreto en {intentos_realizados} intentos.")
                adivinado = True
                break
            elif intento < numero_secreto:
                print("El número secreto es MAYOR.")
            else:
                print("El número secreto es MENOR.")
                
        if not adivinado:
            print(f"\n¡Se te acabaron los intentos! El número secreto era: {numero_secreto}.")
            
        # 2. Repetir juego
        jugar_nuevamente = input("\n¿Quieres jugar otra vez? (sí/no): ")

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    jugar_adivina_numero()
  

import random

def jugar_adivina_numero():
    partidas_ganadas = 0
    partidas_perdidas = 0

    print("======================================")
    print("       JUEGO ADIVINA EL NUMERO")
    print("======================================")

    jugar_nuevamente = "si"

    while jugar_nuevamente.lower() in ["si", "sí", "s"]:

        print("\nSelecciona el nivel de dificultad:")
        print("1. Facil (1 al 10)")
        print("2. Medio (1 al 20)")
        print("3. Dificil (1 al 50)")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            limite = 10
        elif opcion == "2":
            limite = 20
        elif opcion == "3":
            limite = 50
        else:
            print("Opcion no valida. Se seleccionara nivel medio.")
            limite = 20

        numero_secreto = random.randint(1, limite)

        intentos_maximos = 5
        intentos = 0
        numeros_usados = []
        adivinado = False

        print("\nHe generado un numero entre 1 y", limite)
        print("Tienes 5 intentos para adivinarlo.")

        while intentos < intentos_maximos:

            try:
                numero = int(input("\nIngresa tu numero: "))
            except ValueError:
                print("Error: debes ingresar un numero valido.")
                continue

            if numero < 1 or numero > limite:
                print("El numero esta fuera del rango permitido.")
                continue

            # Evitar numeros repetidos
            if numero in numeros_usados:
                print("Ya intentaste con ese numero. Prueba otro.")
                continue

            numeros_usados.append(numero)
            intentos += 1

            if numero == numero_secreto:
                print("\n¡FELICIDADES! Adivinaste el numero secreto.")
                print("Intentos utilizados:", intentos)

                partidas_ganadas += 1
                adivinado = True
                break

            elif numero < numero_secreto:
                print("El numero secreto es MAYOR.")

            else:
                print("El numero secreto es MENOR.")

            # Nueva pista de cercania
            diferencia = abs(numero_secreto - numero)

            if diferencia <= 3:
                print("Pista: ¡Estas muy cerca!")
            else:
                print("Pista: Estas lejos del numero secreto.")

            print("Intentos restantes:", intentos_maximos - intentos)

        if not adivinado:
            print("\nSe terminaron tus 5 oportunidades.")
            print("El numero secreto era:", numero_secreto)
            partidas_perdidas += 1

        # Mostrar estadisticas
        print("\n========== ESTADISTICAS ==========")
        print("Partidas ganadas:", partidas_ganadas)
        print("Partidas perdidas:", partidas_perdidas)
        print("==================================")

        jugar_nuevamente = input(
            "\n¿Deseas jugar nuevamente? (si/no): "
        )

    print("\n¡Gracias por jugar!")
    print("Total de partidas ganadas:", partidas_ganadas)
    print("Total de partidas perdidas:", partidas_perdidas)


if __name__ == "__main__":
    jugar_adivina_numero()
