from utils.dbConnection import get_connection


# Función para leer todos los libros de la base de datos
def ReadBooks():
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return []  # Si no hay conexión, retornar una lista vacía

    try:
        # Crear un cursor que retorna los resultados como diccionarios
        cursor = connection.cursor(dictionary=True)
        # Ejecutar la consulta para seleccionar todos los libros
        cursor.execute("SELECT * FROM libros")
        rows = cursor.fetchall()  # Obtener todos los registros
        return rows  # Retornar los libros
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar una lista vacía
        print(f"Error al obtener datos: {e}")
        return []
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

# Función para crear un nuevo libro en la base de datos
def CreateBook(titulo, autor, categoria, disponible):
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return False  # Si no hay conexión, retornar False

    try:
        cursor = connection.cursor()  # Crear un cursor
        # Definir la consulta para insertar un nuevo libro
        query = "INSERT INTO libros (titulo, autor, categoria, disponible) VALUES (%s, %s, %s, %s)"
        # Ejecutar la consulta con los datos proporcionados
        cursor.execute(query, (titulo, autor, categoria, disponible))
        connection.commit()  # Confirmar la transacción
        return True  # Retornar True si la inserción fue exitosa
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar False
        print(f"Error al insertar datos: {e}")
        return False
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

# Función para leer todos los usuarios de la base de datos
def ReadUser():
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return []  # Si no hay conexión, retornar una lista vacía

    try:
        # Crear un cursor que retorna los resultados como diccionarios
        cursor = connection.cursor(dictionary=True)
        # Ejecutar la consulta para seleccionar todos los usuarios
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()  # Obtener todos los registros
        return rows  # Retornar los usuarios
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar una lista vacía
        print(f"Error al obtener datos: {e}")
        return []
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

# Función para crear un nuevo usuario en la base de datos
def CreateUser(nombre, correo):
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return False  # Si no hay conexión, retornar False

    try:
        cursor = connection.cursor()  # Crear un cursor
        # Definir la consulta para insertar un nuevo usuario
        query = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)"
        # Ejecutar la consulta con los datos proporcionados
        cursor.execute(query, (nombre, correo))
        connection.commit()  # Confirmar la transacción
        return True  # Retornar True si la inserción fue exitosa
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar False
        print(f"Error al insertar usuario: {e}")
        return False
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()

# Función para registrar un préstamo en la base de datos
def CreatePrestamo(id_usuario, id_libro, fecha_prestamo, fecha_devolucion):
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return False  # Si no hay conexión, retornar False

    try:
        cursor = connection.cursor(dictionary=True)  # Crear un cursor que retorna diccionarios

        # Verificar si el libro está disponible
        cursor.execute("SELECT disponible FROM libros WHERE id_libro = %s", (id_libro,))
        libro = cursor.fetchone()  # Obtener el libro

        if libro is None:
            print("Error: El libro no existe.")
            return False  # Si el libro no existe, retornar False

        if libro['disponible'] == 0:
            print("Error: El libro no está disponible.")
            return False  # Si el libro no está disponible, retornar False

        # Registrar el préstamo
        query = """
        INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (id_usuario, id_libro, fecha_prestamo, fecha_devolucion))

        # Actualizar la disponibilidad del libro a "No disponible" (0)
        cursor.execute("UPDATE libros SET disponible = 0 WHERE id_libro = %s", (id_libro,))

        connection.commit()  # Confirmar la transacción
        return True  # Retornar True si el préstamo fue registrado exitosamente
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar False
        print(f"Error al registrar el préstamo: {e}")
        return False
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()
            


# Función para leer todos los prestamos de la base de datos
def ReadPrestamos():
    connection = get_connection()  # Obtener la conexión a la base de datos
    if connection is None:
        return []  # Si no hay conexión, retornar una lista vacía

    try:
        # Crear un cursor que retorna los resultados como diccionarios
        cursor = connection.cursor(dictionary=True)
        # Ejecutar la consulta para seleccionar todos los prestamos
        cursor.execute("SELECT * FROM prestamos")
        rows = cursor.fetchall()  # Obtener todos los registros
        return rows  # Retornar los prestamos
    except Exception as e:
        # Si hay un error, imprimir el mensaje y retornar una lista vacía
        print(f"Error al obtener datos: {e}")
        return []
    finally:
        # Cerrar la conexión si está abierta
        if connection:
            connection.close()