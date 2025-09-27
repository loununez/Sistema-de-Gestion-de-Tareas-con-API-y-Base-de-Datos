import requests
import json

BASE_URL = "http://127.0.0.1:5000"


# Registrar al usuario en el sistema
def registrar_usuario():
    print("Registro de Usuario")
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    payload = {'usuario': usuario, 'contraseña': contraseña}
    try:
        response = requests.post(f"{BASE_URL}/registro", json=payload)
        print(response.json().get('mensaje'))
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar al servidor :(")

# Permitir al usuario iniciar sesión
def iniciar_sesion():
    print("Inicio de Sesión")
    usuario = input("Ingresa tu nombre de usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    payload = {'usuario': usuario, 'contraseña': contraseña}
    try:
        response = requests.post(f"{BASE_URL}/login", json=payload)
        print(response.json().get('mensaje'))
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar al servidor :(")

# Acceder a la página de tareas
def ver_tareas():
    print("Acceso a Tareas")
    try:
        response = requests.get(f"{BASE_URL}/tareas")
        # El contenido es HTML, así que lo imprimimos directamente
        print(response.text)
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar al servidor :(")

# Menú principal
def menu():
    while True:
        print("Menú Principal")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Ver Tareas")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            ver_tareas()
        elif opcion == '4':
            print("Saliendo")
            break
        else:
            print("Opción no válida, intenta de nuevo :(")

if __name__ == '__main__':
    menu()