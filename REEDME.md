### TP N° 9: Aplicación CRUD en Python con Base de Datos Remota

Alumno: Leandro Sebastian Rivas Romero  
Institución: IPET N° 247 - Ing. Carlos A. Cassaffousth  
Materia: Base de Datos  
Año: 2026  

// Descripción del Proyecto
Sistema de gestión para e-commerce desarrollado en Python que implementa operaciones CRUD (Crear, Leer, Actualizar y Eliminar) conectado de forma remota a una base de datos relacional MySQL alojada en la nube mediante **Clever Cloud**.

// Tecnologías y Herramientas
- **Lenguaje:** Python 3.13
- **Base de Datos:** MySQL (Clever Cloud)
- **Librerías utilizadas:** 
  - `mysql-connector-python` (Conexión y ejecución de consultas SQL)
  - `python-dotenv` (Gestión segura de credenciales y variables de entorno)

// Estructura del Repositorio
- `main.py`: Código fuente principal con la lógica de conexión y el menú interactivo del CRUD.
- `schema.sql`: Script SQL completo para la creación de la estructura de tablas, claves primarias, foráneas y restricciones.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.
- `.env.example`: Plantilla de referencia para las variables de entorno.
- `.gitignore`: Configuración para proteger archivos sensibles y excluir temporales.

// Instrucciones de Instalación y Ejecución

1. **Clonar o descargar** este repositorio en tu equipo.
2. **Instalar las dependencias** ejecutando en la terminal:
   ```bash
   pip install -r requirements.txt

   "fin"