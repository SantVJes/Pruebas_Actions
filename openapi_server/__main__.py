#!/usr/bin/env python3
import connexion
from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from openapi_server.controllers.usuario_controller import import_db_controller

def main():
    # Inicializa una instancia de la aplicación Connexion, especificando el directorio donde está el archivo OpenAPI.
    app = connexion.App(__name__, specification_dir='./openapi/')
    
    # Configura el codificador JSON personalizado para manejar la serialización de objetos.
    app.app.json_encoder = encoder.JSONEncoder
    
    # Agrega la especificación de la API desde el archivo `openapi.yaml`, con el título y soporte de parámetros en estilo Python.
    app.add_api(
        'openapi.yaml',
        arguments={'title': 'Microservicio de Usuarios de una aplicación de tipo Netflix'},
        pythonic_params=True
    )

    # Configura la URL de la base de datos PostgreSQL para SQLAlchemy y desactiva el seguimiento de modificaciones para mejorar el rendimiento.
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5433/Usuarios'
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la instancia de SQLAlchemy, vinculándola a la aplicación Connexion.
    db = SQLAlchemy(app.app)

    # Importa y registra los controladores necesarios para la base de datos.
    import_db_controller(db)
    
    # Importa el modelo de la base de datos, asegurando que las tablas y las estructuras estén definidas.
   

    # Ejecuta la aplicación en el puerto especificado (8080).
    app.run(port=8080)

# Punto de entrada principal de la aplicación.
if __name__ == '__main__':
    main()
