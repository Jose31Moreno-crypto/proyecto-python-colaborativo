# proyecto-python-colaborativo
Proyecto de práctica en el que trabajamos en equipo usando Python y GitHub. Incluye tres módulos con funcionalidades diferentes: operaciones matemáticas, impresión de un cuento y arte en la consola.

## Descripción de los módulos

| Archivo | Funcionalidad |
| --- | --- |
| `matematicas.py` | Contiene las funciones `sumar`, `restar`, `multiplicar` y `dividir`. Si se intenta dividir entre cero, devuelve un mensaje explicativo. |
| `cuento.py` | Imprime el cuento «El viaje del código», una historia sobre el trabajo en equipo entre desarrolladores. |
| `arte.py` | Imprime un árbol en la consola utilizando caracteres. |

## Requisitos

- Tener Python 3 instalado.
- Los módulos utilizan funciones de Python y no requieren instalar paquetes adicionales.

## Instrucciones de uso

1. En la página del repositorio, selecciona **Code > Download ZIP** para descargar el proyecto.
2. Descomprime el archivo.
3. Abre una terminal en la carpeta que contiene los archivos `.py`.
4. Ejecuta los siguientes ejemplos.

Si en tu equipo el comando para Python 3 es `python3`, úsalo en lugar de `python`.

### Operaciones matemáticas

Las funciones de este módulo se utilizan importando `matematicas`. Puedes probar cada operación con estos comandos:

```bash
python -c "import matematicas; print(matematicas.sumar(10, 5))"
python -c "import matematicas; print(matematicas.restar(10, 5))"
python -c "import matematicas; print(matematicas.multiplicar(10, 5))"
python -c "import matematicas; print(matematicas.dividir(10, 5))"
```

Los resultados de estos ejemplos son `15`, `5`, `50` y `2.0`, respectivamente.

### Impresión del cuento

```bash
python cuento.py
```

Este comando muestra el título y el texto del cuento en la consola.

### Arte en la consola

```bash
python arte.py
```

Este comando muestra el título del módulo y el dibujo de un árbol.
