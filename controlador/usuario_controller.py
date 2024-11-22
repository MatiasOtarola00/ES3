import bcrypt
import mysql.connector
from modelo.bd import conectar

def crear_usuario(nombre, edad, email, passwd):
    """
    Crear un nuevo usuario con nombre, edad, email y contraseña.
    """

    salt = bcrypt.gensalt()
    passwd_hash = bcrypt.hashpw(passwd.encode('utf-8'), salt)

   
    conn = conectar()
    if conn is None:
        return "Error: No se pudo conectar a la base de datos"
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO usuarios (nombre, edad, email, passwd_hash) 
            VALUES (%s, %s, %s, %s)
        ''', (nombre, edad, email, passwd_hash))
        conn.commit()
        print("Usuario creado exitosamente.")
    except mysql.connector.Error as e:
        print(f"Error al crear usuario: {e}")
    finally:
        cursor.close()
        conn.close()


def autenticar_usuario(email, passwd):
    """
    Autenticar a un usuario con email y contraseña.
    """
    conn = conectar()
    if conn is None:
        return "Error: No se pudo conectar a la base de datos"
    
    try:
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT passwd_hash FROM usuarios WHERE email = %s
        ''', (email,))
        resultado = cursor.fetchone()
        if resultado is None:
            print("Usuario no encontrado.")
            return False

        # Verificar el hash de la contraseña
        passwd_hash = resultado[0]
        if bcrypt.checkpw(passwd.encode('utf-8'), passwd_hash.encode('utf-8')):
            print("Autenticación exitosa.")
            return True
        else:
            print("Contraseña incorrecta.")
            return False
    except mysql.connector.Error as e:
        print(f"Error al autenticar usuario: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

