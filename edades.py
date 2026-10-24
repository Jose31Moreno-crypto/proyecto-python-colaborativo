def consultar_edad():
    # 1. Crear una lista con al menos 5 nombres de personas
    nombres = ["Ana", "Carlos", "María", "José", "Lucía"]
    
    # 2. Crear un diccionario donde las claves sean los nombres y los valores las edades
    edades = {
        "Ana": 30,
        "Carlos": 25,
        "María": 28,
        "José": 35,
        "Lucía": 22
    }
    
    print("=== SISTEMA DE CONSULTA DE EDADES ===")
    
    # 3. Solicitar al usuario que ingrese un nombre
    nombre_ingresado = input("Ingresa un nombre: ")
    
    # 4. Usar condicionales para verificar si el nombre está en el diccionario
    if nombre_ingresado in edades:
        print(f"{nombre_ingresado} tiene {edades[nombre_ingresado]} años.")
    else:
        print(f"La persona '{nombre_ingresado}' no fue encontrada.")

if __name__ == "__main__":
    consultar_edad()
