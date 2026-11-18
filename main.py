import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

def leer_productos():
    conexion = conectar_bd()
    if not conexion:
        return
    
    cursor = conexion.cursor()
    cursor.execute("SELECT id_producto, nombre, precio, stock FROM productos")
    resultados = cursor.fetchall()
    
    print("\n--- LISTADO ---")
    for prod in resultados:
        print(f"ID: {prod[0]} | Nombre: {prod[1]} | Precio: ${prod[2]} | Stock: {prod[3]}")
    
    cursor.close()
    conexion.close()

def crear_producto():
    print("\n--- CREAR ---")
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    
    conexion = conectar_bd()
    if not conexion:
        return
    
    cursor = conexion.cursor()
    sql = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, descripcion, precio, stock))
    conexion.commit()
    print(f"¡Creado con éxito! ID: {cursor.lastrowid}")
    
    cursor.close()
    conexion.close()

def actualizar_producto():
    leer_productos()
    print("\n--- ACTUALIZAR ---")
    id_prod = input("ID a modificar: ")
    nuevo_precio = float(input("Nuevo precio: "))
    nuevo_stock = int(input("Nuevo stock: "))
    
    conexion = conectar_bd()
    if not conexion:
        return
    
    cursor = conexion.cursor()
    sql = "UPDATE productos SET precio = %s, stock = %s WHERE id_producto = %s"
    cursor.execute(sql, (nuevo_precio, nuevo_stock, id_prod))
    conexion.commit()
    
    if cursor.rowcount > 0:
        print("¡Actualizado correctamente!")
    else:
        print("No se encontró el ID.")
        
    cursor.close()
    conexion.close()

def eliminar_producto():
    leer_productos()
    print("\n--- ELIMINAR ---")
    id_prod = input("ID a eliminar: ")
    
    conexion = conectar_bd()
    if not conexion:
        return
    
    cursor = conexion.cursor()
    sql = "DELETE FROM productos WHERE id_producto = %s"
    cursor.execute(sql, (id_prod,))
    conexion.commit()
    
    if cursor.rowcount > 0:
        print("¡Eliminado correctamente!")
    else:
        print("No se encontró el ID.")
        
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("\n=== MENÚ CRUD ===")
        print("1. Leer")
        print("2. Crear")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            leer_productos()
        elif opcion == "2":
            crear_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()