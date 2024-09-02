import socket
import os
import sys

def enviar_opcion_y_cantidad_caracteres(sock, opcion, cantidad_caracteres):
    sock.sendall(opcion.to_bytes(4, byteorder='little'))
    sock.sendall(cantidad_caracteres.to_bytes(4, byteorder='little'))

def main():
    # Inicializar el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 5000)
    sock.connect(server_address)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu\n 1)Generador de nombres de usuario:\n 2)Generador de contraseñas:\n 3)Salir\n")

        try:
            opcion_menu = int(input())
        except ValueError:
            print("Opción inválida. Inténtelo de nuevo.")
            os.system('pause' if os.name == 'nt' else 'read -p "Press Enter to continue..."')
            continue

        if opcion_menu in [1, 2]:
            try:
                cantidad_caracteres = int(input("Seleccione cantidad de caracteres\n"))
            except ValueError:
                print("Cantidad de caracteres inválida. Inténtelo de nuevo.")
                os.system('pause' if os.name == 'nt' else 'read -p "Press Enter to continue..."')
                continue

            enviar_opcion_y_cantidad_caracteres(sock, opcion_menu, cantidad_caracteres)

            respuesta = sock.recv(80).decode('utf-8')
            if opcion_menu == 1:
                print(f"Su usuario es: {respuesta}")
            elif opcion_menu == 2:
                print(f"Su contraseña es: {respuesta}")

            os.system('pause' if os.name == 'nt' else 'read -p "Press Enter to continue..."')

        elif opcion_menu == 3:
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opción incorrecta. Vuelva a elegir.")
            os.system('pause' if os.name == 'nt' else 'read -p "Press Enter to continue..."')

    sock.close()

if __name__ == "__main__":
    main()
