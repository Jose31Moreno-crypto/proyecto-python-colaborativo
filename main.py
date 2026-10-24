def generar_historia():
    print("=== REGISTRO DEL PROTAGONISTA ===")
    
    # Entradas del usuario
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    ciudad = input("Ingresa tu ciudad de residencia: ")
    
    # Mi aporte personal a la historia
    profesion = input("¿Cuál es tu profesión o pasatiempo favorito?: ")
    
    print("\n--- LA HISTORIA COMIENZA ---")
    # Salida personalizada
    print(f"¡Hola, {nombre}! Tienes {edad} años y vives en {ciudad}.")
    
    # Línea narrativa de mi aporte
    print(f"Los días en {ciudad} transcurren mientras te dedicas con entusiasmo a {profesion}.")

    # Aporte personal: experiencias y logros del protagonista
    objetivo = input("¿Qué objetivo quieres alcanzar este año?: ")
    obstaculo = input("¿Qué dificultad quieres superar?: ")
    logro = input("¿De qué logro te sientes orgulloso?: ")

    print("\n--- NUEVO CAPÍTULO DE MI HISTORIA ---")
    print(f"Este año, {nombre} quiere alcanzar el objetivo de {objetivo}.")
    print(f"Para lograrlo, deberá superar la dificultad de {obstaculo}.")
    print(f"Uno de sus logros más importantes es {logro}.")
    print("Cada experiencia le enseña algo nuevo y le ayuda a crecer como persona.")
    print("Su historia continúa con nuevos retos, aprendizajes y oportunidades.")

if __name__ == "__main__":
    generar_historia()
