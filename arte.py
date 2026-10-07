def imprimir_arte(caracter="*"):
    """Imprime un árbol usando caracteres en la consola."""
    print(f"--- ARTE EN PYTHON (usando '{caracter}') ---")
    print(f"        {caracter}")
    print(f"       {caracter * 3}")
    print(f"      {caracter * 5}")
    print(f"     {caracter * 7}")
    print(f"    {caracter * 9}")
    print(f"   {caracter * 11}")
    print("       |||")
    print("       |||")
    print("   ___________")

if __name__ == "__main__":
    print("MÓDULO DE ARTE ACTIVADO")
    # El usuario ahora puede elegir el carácter
    eleccion = input("Ingresa un carácter para dibujar el árbol (o presiona Enter para usar *): ")
    if eleccion == "":
        imprimir_arte()
    else:
        imprimir_arte(eleccion)
