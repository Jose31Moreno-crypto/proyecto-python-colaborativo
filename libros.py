import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Biblioteca - Gestión de Libros"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Lista interna para almacenar los libros (cada libro será un diccionario)
    libros = []

    # Campos de entrada de texto para el formulario
    txt_titulo = ft.TextField(label="Título del libro", width=300)
    txt_autor = ft.TextField(label="Autor", width=300)
    txt_isbn = ft.TextField(label="ISBN (Identificador único)", width=300)

    # Contenedor donde se mostrará la lista de libros en pantalla
    lista_libros_view = ft.ListView(expand=1, spacing=10, padding=10, auto_scroll=True)

    def actualizar_lista():
        """Función para actualizar dinámicamente la vista de la lista de libros"""
        lista_libros_view.controls.clear()
        for libro in libros:
            lista_libros_view.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"📖 {libro['titulo']}", weight=ft.FontWeight.BOLD, size=16),
                            ft.Text(f"Autor: {libro['autor']}"),
                            ft.Text(f"ISBN: {libro['isbn']} | Estado: ", spans=[
                                ft.TextSpan(
                                    libro['estado'],
                                    style=ft.TextStyle(color=ft.colors.GREEN if libro['estado'] == "Disponible" else ft.colors.RED, weight=ft.FontWeight.BOLD)
                                )
                            ]),
                        ]),
                        padding=10
                    )
                )
            )
        page.update()

    def registrar_libro(e):
        """Función que se ejecuta al hacer clic en el botón Registrar"""
        titulo = txt_titulo.value.strip()
        autor = txt_autor.value.strip()
        isbn = txt_isbn.value.strip()

        # Validación básica de campos vacíos
        if not titulo or not autor or not isbn:
            page.snack_bar = ft.SnackBar(ft.Text("¡Error! Todos los campos son obligatorios."), bgcolor=ft.colors.RED_400)
            page.snack_bar.open = True
            page.update()
            return

        # Verificar si el ISBN ya existe (identificador único)
        for libro in libros:
            if libro['isbn'] == isbn:
                page.snack_bar = ft.SnackBar(ft.Text("¡Error! Ya existe un libro registrado con ese ISBN."), bgcolor=ft.colors.RED_400)
                page.snack_bar.open = True
                page.update()
                return

        # Agregar el nuevo libro con estado inicial "Disponible"
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn,
            "estado": "Disponible"
        }
        libros.append(nuevo_libro)

        # Limpiar los campos de texto después de registrar
        txt_titulo.value = ""
        txt_autor.value = ""
        txt_isbn.value = ""
        txt_titulo.focus()

        # Actualizar la interfaz visual
        actualizar_lista()

        # Mensaje de éxito
        page.snack_bar = ft.SnackBar(ft.Text("¡Libro registrado exitosamente!"), bgcolor=ft.colors.GREEN_400)
        page.snack_bar.open = True
        page.update()

    # Botón para registrar el libro
    btn_registrar = ft.ElevatedButton(
        text="Registrar Libro",
        icon=ft.icons.BOOK,
        on_click=registrar_libro,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE
    )

    # Estructura principal de la interfaz de esta sección
    page.add(
        ft.Text("📚 Gestión de Inventario de Libros", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Row([
            # Columna izquierda: Formulario de registro
            ft.Column([
                ft.Text("Registrar Nuevo Libro", size=18, weight=ft.FontWeight.W_500),
                txt_titulo,
                txt_autor,
                txt_isbn,
                btn_registrar
            ], alignment=ft.MainAxisAlignment.START, spacing=15),
            
            ft.VerticalDivider(width=20),

            # Columna derecha: Inventario visual dinámico
            ft.Column([
                ft.Text("Inventario de Libros", size=18, weight=ft.FontWeight.W_500),
                ft.Container(
                    content=lista_libros_view,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    border_radius=10,
                    padding=10,
                    width=400,
                    height=350
                )
            ], alignment=ft.MainAxisAlignment.START, spacing=15)
        ], alignment=ft.MainAxisAlignment.CENTER, expand=True)
    )

ft.app(target=main)
