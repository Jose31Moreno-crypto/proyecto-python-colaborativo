def generar_historia():
    print("=== REGISTRO DEL PROTAGONISTA ===")
    
    # Entradas del usuario
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    ciudad = input("Ingresa tu ciudad de residencia: ")
    
    print("\n--- LA HISTORIA COMIENZA ---")
    # Salida personalizada
    print(f"¡Hola, {nombre}! Tienes {edad} años y vives en {ciudad}.")

if __name__ == "__main__":
    generar_historia()
