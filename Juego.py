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
  
