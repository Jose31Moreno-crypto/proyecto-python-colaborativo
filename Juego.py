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

        opcion = input("Selecciona una opcion: ").strip()

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

        # 4. Pistas extra o comodines: se renuevan en cada partida
        comodines_maximos = 2
        comodines_usados = 0

        print("\nHe generado un numero entre 1 y", limite)
        print("Tienes 5 intentos para adivinarlo.")
        print("Tienes 2 comodines por partida; usarlos no gasta intentos.")
        print("Primer comodin: par o impar. Segundo comodin: rango mas pequeño.")
        print("Escribe 'pista' o 'comodin' cuando quieras pedir una pista extra.")

        while intentos < intentos_maximos:

            entrada = input(
                f"\nIntento {intentos + 1} de {intentos_maximos}. "
                "Ingresa tu numero o escribe 'pista': "
            ).strip().lower()

            # Revisar el comando antes de convertir la entrada a un numero
            if entrada in ["pista", "comodin", "comodín"]:
                if comodines_usados >= comodines_maximos:
                    print("Ya usaste tus 2 comodines en esta partida.")
                    continue

                if comodines_usados == 0:
                    if numero_secreto % 2 == 0:
                        print("Pista extra: el numero secreto es PAR.")
                    else:
                        print("Pista extra: el numero secreto es IMPAR.")
                else:
                    # Elegir un intervalo pequeño que contenga el numero secreto
                    tamano_rango = max(3, limite // 5)
                    inicio_minimo = max(1, numero_secreto - tamano_rango + 1)
                    inicio_maximo = min(numero_secreto, limite - tamano_rango + 1)
                    inicio_rango = random.randint(inicio_minimo, inicio_maximo)
                    fin_rango = inicio_rango + tamano_rango - 1
                    print(
                        f"Pista extra: el numero secreto esta entre {inicio_rango} "
                        f"y {fin_rango}, incluidos."
                    )

                comodines_usados += 1
                print("Comodines restantes:", comodines_maximos - comodines_usados)
                continue  # Pedir una pista no consume un intento

            try:
                numero = int(entrada)
            except ValueError:
                print("Error: ingresa un numero valido, 'pista' o 'comodin'.")
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
        ).strip()

    print("\n¡Gracias por jugar!")
    print("Total de partidas ganadas:", partidas_ganadas)
    print("Total de partidas perdidas:", partidas_perdidas)


if __name__ == "__main__":
    jugar_adivina_numero()


