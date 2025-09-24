# API Flask para Gestión de Usuarios y Tareas

Este proyecto es una API simple construida con Flask y SQLite para gestionar el registro, inicio de sesión de usuarios y mostrar una página simple de bienvenida para la gestión de tareas

## Requisitos
**Tener Python 3**
**Flask:** Framework para el servidor web.
**Werkzeug:** Librería utilizada para el hasheo de contraseñas.
**SQLite:**

## Instalación
**Clona este repositorio:**
git clone https://github.com/loununez/Sistema-de-Gestion-de-Tareas-con-API-y-Base-de-Datos.git
cd Sistema-de-Gestion-de-Tareas-con-API-y-Base-de-Datos

**Instala las dependencias:**
pip install Flask Werkzeug

## Pruebas de la API
Puedes usar herramientas como **Postman** o **Thunder Client**

## 1. Registro de Usuario (`POST /registro`)

- **URL:** `http://127.0.0.1:5000/registro`
- **Método:** `POST`
- **Body (JSON):**

    {
     "usuario": "nombre",
     "contraseña": "1234"
    }

## 2. Inicio de Sesión (`POST /login`)
-   **URL:** `http://127.0.0.1:5000/login`
-   **Método:** `POST`
-   **Body (JSON):**
  
    {
     "usuario": "nombre",
     "contraseña": "1234"
    }
    

## 3. Acceso a Tareas (`GET /tareas`)
-   **URL:** `http://127.0.0.1:5000/tareas`
-   **Método:** `GET`
-   **Resultado:** Muestra una página HTML de bienvenida

## **Respuestas Conceptuales**
## 1. ¿Por qué hashear contraseñas?
Para que las contraseñas no se guarden tal cual en la base de datos. 
Si alguien entra sin permiso, no podrá verlas fácilmente, lo que ayuda a proteger a los usuarios.

#### 2. Ventajas de usar SQLite en este proyecto
Es fácil de usar, no necesita instalar un servidor aparte y guarda todo en un solo archivo. 
Además, funciona bien para proyectos chicos o medianos y hace que sea rápido empezar a desarrollar.
