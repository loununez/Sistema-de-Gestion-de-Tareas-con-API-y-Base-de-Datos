import sqlite3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            usuario TEXT UNIQUE NOT NULL,
            contraseña_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Se llama al inicio para asegurar que la tabla existe
create_table()

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({"mensaje": "Faltan usuario o contraseña"}), 400

    contraseña_hash = generate_password_hash(contraseña)

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contraseña_hash) VALUES (?, ?)", (usuario, contraseña_hash))
        conn.commit()
        return jsonify({"mensaje": f"Usuario {usuario} registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"mensaje": "El usuario ya existe"}), 409
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({"mensaje": "Faltan usuario o contraseña"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT contraseña_hash FROM usuarios WHERE usuario = ?", (usuario,))
    usuario_db = cursor.fetchone()
    conn.close()

    if usuario_db and check_password_hash(usuario_db[0], contraseña):
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"mensaje": "Usuario o contraseña incorrectos"}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    return """
    <h1>Hola!</h1>
    <p>Bienvenido a PFO 2: Sistema de Gestión de Tareas con API y Base de Datos</p>
    """

if __name__ == '__main__':
    app.run(debug=True)