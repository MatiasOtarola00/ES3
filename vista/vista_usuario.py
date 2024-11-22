from controlador.usuario_controller import crear_usuario, autenticar_usuario


def mostrar_menu():
    """
    Mostrar el menú principal de la aplicación.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear Usuario")
        print("2. Autenticar Usuario")
        print("3. Actualizar Indicadores Económicos desde API")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            edad = input("Ingrese la edad del usuario: ")
            email = input("Ingrese el email del usuario: ")
            passwd = input("Ingrese la contraseña: ")
            try:
                edad = int(edad)
                crear_usuario(nombre, edad, email, passwd)
            except ValueError:
                print("Error: La edad debe ser un número entero.")

        elif opcion == "2":
            email = input("Ingrese el email del usuario: ")
            passwd = input("Ingrese la contraseña: ")
            autenticar_usuario(email, passwd)

        elif opcion == "3":
            actualizar_indicadores()

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
