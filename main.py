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

if __name__ == "__main__":
    generar_historia()
