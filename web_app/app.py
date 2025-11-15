import os
import mysql.connector
from flask import Flask
import time

app = Flask(__name__)

def get_db_connection():
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_pass = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')

    conn = None
    attempts = 0
    while attempts < 10:
        try:
            conn = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_pass,
                database=db_name
            )
            print("¡Conexión a la BD exitosa!")
            return conn
        except mysql.connector.Error as err:
            print(f"Error conectando a la BD: {err}")
            attempts += 1
            time.sleep(3)
    return None 

@app.route('/')
def hello():
    conn = get_db_connection()
    
    if not conn:
        return "<h1>Error: No se pudo conectar a la base de datos.</h1>", 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM nombres;")
        
        nombres_tuplas = cursor.fetchall()
        
        output = "<h1>Nombres en la Base de Datos:</h1>"
        output += "<ul>"
        for fila in nombres_tuplas:
            output += f"<li>{fila[0]}</li>"
            
        output += "</ul>"
        
        return output

    except Exception as e:
        return f"<h1>Error al consultar la base de datos:</h1><p>{e}</p>", 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)