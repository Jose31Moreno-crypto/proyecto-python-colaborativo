# Importar el módulo operaciones creado por el equipo
import operaciones

def calculadora():
    print("=== CALCULADORA BÁSICA DEL EQUIPO ===")

    try:
        # Solicitar al usuario dos números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return

    # Solicitar la operación que desea realizar
    print("\nSelecciona la operación:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    opcion = input("Ingresa el número de la operación (1/2/3/4) o el símbolo: ")

    # Utilizar las funciones del módulo operaciones.py (nota que usa 'suma', 'resta', 'multiplicacion', 'division')
    if opcion == "1" or opcion == "+":
        resultado = operaciones.suma(num1, num2)
        print(f"\nEl resultado de la suma es: {resultado}")

    elif opcion == "2" or opcion == "-":
        resultado = operaciones.resta(num1, num2)
        print(f"\nEl resultado de la resta es: {resultado}")

    elif opcion == "3" or opcion == "*":
        resultado = operaciones.multiplicacion(num1, num2)
        print(f"\nEl resultado de la multiplicación es: {resultado}")

    elif opcion == "4" or opcion == "/":
        resultado = operaciones.division(num1, num2)
        print(f"\nEl resultado de la división es: {resultado}")

    else:
        print("\nOperación no válida.")

if __name__ == "__main__":
    calculadora()
    
