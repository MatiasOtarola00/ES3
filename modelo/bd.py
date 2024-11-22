import mysql.connector
from mysql.connector import Error

def conectar():
    try: 
        conn = mysql.connector.connect(
            host='localhost',
            database='indicadores_economicos', 
            user='prueba',
            password='123456'  
        )
        return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is not None:
        try:
            cursor = conn.cursor()  
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    edad INT NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    passwd_hash VARCHAR(255) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS indicadores (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    valor DECIMAL(10, 2) NOT NULL,
                    fecha_actualizacion DATE NOT NULL
                )
            ''')
            conn.commit()
            print("Tablas creadas exitosamente.")
        except Error as e:
            print(f"Error al crear las tablas: {e}")
        finally:
            cursor.close()
            conn.close()