import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.get_all_perfiles200_response_inner import GetAllPerfiles200ResponseInner  # noqa: E501
from openapi_server.models.usuario import Usuario# noqa: E501
from openapi_server import util
from sqlalchemy.exc import IntegrityError


from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, render_template, make_response

db = SQLAlchemy()

def import_db_controller(database):
    global db

def post_iniciar_sesion():
    """Iniciar sesión de usuario en la aplicación

    Verifica las credenciales de un usuario y, si son válidas, inicia sesión.

    :rtype: Union[Dict[str, str], Tuple[Dict[str, str], int]]
    """
    if not request.is_json:
        return jsonify({"error": "La solicitud debe estar en formato JSON"}), 400
    
    data = request.get_json()
    
    # Extraer y validar campos obligatorios
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # Intentar buscar el usuario en la base de datos
    usuario = Usuario.query.filter_by(email=email).first()
    
    # Verificar si el usuario existe y la contraseña es correcta
    if usuario and usuario.verificar_contraseña(password):  #'verificar_contraseña' es un método en Usuario
        # Generar token o mensaje de éxito
        return jsonify({"mensaje": "Inicio de sesión exitoso", "id_usuario": usuario.id_usuario}), 200
    
    
    # Credenciales incorrectas
    return jsonify({"error": "Credenciales incorrectas"}), 401

def add_favorito(id_usuario, nombre_perfil, body):  # noqa: E501
    """Añadir un nuevo contenido al listado de favoritos de un perfil específico de un usuario por su ID

    Añade un nuevo contenido al conjunto de contenidos multimedia favoritos de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario al que se le añadirá un contenido a la lista de favoritos de uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil al que se le añadirá un contenido a su lista de favoritos
    :type nombre_perfil: str
    :param body: 
    :type body: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def add_perfil(id_usuario, get_all_perfiles200_response_inner):  # noqa: E501
    """Añadir un nuevo perfil a un usuario por su ID

    Añade un nuevo perfil a un usuario en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario al que se le añadirá un nuevo perfil
    :type id_usuario: int
    :param get_all_perfiles200_response_inner: 
    :type get_all_perfiles200_response_inner: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_all_perfiles200_response_inner = GetAllPerfiles200ResponseInner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_usuario():  # noqa: E501
    """Añadir un nuevo usuario a la aplicación

    Crea una nueva cuenta en la aplicación que estará asociada a un nuevo usuario # noqa: E501

    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    if request.is_json:
        data = request.get_json()

        # Extraer y validar el objeto 'usuario'
        usuario_data = data.get("usuario")
        if not usuario_data:
            return jsonify({"error": "No ay objeto."}), 400
        
        # Extraer y validar campos obligatorios del usuario
        email = usuario_data.get("email")
        password = usuario_data.get("password")
        metodo_pago = usuario_data.get("metodo_pago")  # Opcional
        status = usuario_data.get("status", True)      # Activo por defecto
        perfiles = usuario_data.get("perfiles")        # Opcional, formato JSON
        if not email or not password:
            return jsonify({"error": "Faltan campos obligatorios"}), 400
        
        try:
        # Crear el nuevo usuario utilizando la función create
            nuevo_usuario = Usuario.create(
                email=email,
                password=password,
                metodo_pago=metodo_pago,
                status=status,
                perfiles=perfiles
              )
            return jsonify({"Usuario Creado"}), 201  # Retorna el nuevo usuario creado

        except IntegrityError:    
            
            return jsonify({"error": "El usuario con ese email ya existe"}), 409  
            
    return jsonify({"error": "La solicitud debe estar en formato JSON"}), 400

     



def delete_perfil(id_usuario, nombre_perfil):  # noqa: E501
    """Eliminar un perfil específico de un usuario por su ID

    Elimina un perfil específico de un usuario registrado en el sistema en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se borrará el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se borrará
    :type nombre_perfil: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_usuario(id_usuario):  # noqa: E501
    """Eliminar un usuario específico por su ID

    Elimina un contenido multimedia específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a borrar
    :type id_usuario: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_perfiles(id_usuario):  # noqa: E501
    """Obtener una lista de los perfiles asociados a un usuario

    Retorna el conjunto de perfiles asociados a un usuario específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrán sus perfiles
    :type id_usuario: int

    :rtype: Union[List[GetAllPerfiles200ResponseInner], Tuple[List[GetAllPerfiles200ResponseInner], int], Tuple[List[GetAllPerfiles200ResponseInner], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_usuarios():  # noqa: E501
    """Obtener la lista de usuarios registrados en la aplicación

    Retorna el conjunto de usuarios registrados en la aplicación # noqa: E501


    :rtype: Union[List[Usuario], Tuple[List[Usuario], int], Tuple[List[Usuario], int, Dict[str, str]]
    """
    
    try:
        # Obtiene todos los registros de usuarios en la base de datos, ordenados por 'status' (activos primero)
        usuarios = Usuario.query.order_by(Usuario.status.desc()).all()  # Ordena por 'status' (True primero, luego False)

        # Convierte cada usuario en un diccionario usando `to_dict`
        usuarios_dict = [usuario.to_dict() for usuario in usuarios]

        return usuarios_dict, 200  # Devuelve la lista de usuarios y el código HTTP 200 (OK)

    except Exception as e:
      # Manejo de errores en caso de fallo en la base de datos u otro problema
        error_msg = {"error": f"Error al obtener usuarios: {str(e)}"}
        return [], 500, error_msg  # Devuelve lista vacía, código 500 y mensaje de error

    
    
    
    return 'do some magic!'


def get_favoritos(id_usuario, nombre_perfil):  # noqa: E501
    """Obtener el listado de contenidos multimedia favoritos de un perfil específico de un usuario por su ID

    Retorna el conjunto de contenidos multimedia favoritos de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá la lista de favoritos de uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil del que se obtendrá su lista de favoritos
    :type nombre_perfil: str

    :rtype: Union[List[int], Tuple[List[int], int], Tuple[List[int], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_perfil(id_usuario, nombre_perfil):  # noqa: E501
    """Obtener un perfil específico por su ID

    Retorna los datos de un perfil específico en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se obtendrá el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se obtendrá
    :type nombre_perfil: str

    :rtype: Union[GetAllPerfiles200ResponseInner, Tuple[GetAllPerfiles200ResponseInner, int], Tuple[GetAllPerfiles200ResponseInner, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_usuario_by_id(id_usuario):  # noqa: E501
    """Obtener un usuario específico por su ID

    Retorna la información de un usuario en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a devolver
    :type id_usuario: int

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_perfil(id_usuario, nombre_perfil, get_all_perfiles200_response_inner):  # noqa: E501
    """Actualizar un perfil específico por su ID

    Actualiza un perfil específico de un usuario registrado en el sistema en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario del que se actualizará el perfil
    :type id_usuario: int
    :param nombre_perfil: Nombre del perfil que se actualizará
    :type nombre_perfil: str
    :param get_all_perfiles200_response_inner: 
    :type get_all_perfiles200_response_inner: dict | bytes

    :rtype: Union[GetAllPerfiles200ResponseInner, Tuple[GetAllPerfiles200ResponseInner, int], Tuple[GetAllPerfiles200ResponseInner, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_all_perfiles200_response_inner = GetAllPerfiles200ResponseInner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_usuario(id_usuario, usuario):  # noqa: E501
    """Actualizar un usuario específico por su ID

    Actualiza la información de un usuario registrado en función del identificador proporcionado # noqa: E501

    :param id_usuario: ID del usuario a actualizar
    :type id_usuario: int
    :param usuario: 
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upload_imagen(id_usuario, nombre_perfil, request_body):  # noqa: E501
    """Actualizar la imagen de un perfil específico de un usuario por su ID

    Actualizar la imagen de un perfil específico perteneciente a un usuario en función de su identificador # noqa: E501

    :param id_usuario: ID del usuario al que se le actualizará la imagen a uno de sus perfiles
    :type id_usuario: int
    :param nombre_perfil: nombre del perfil al que se le actualizará su imagen
    :type nombre_perfil: str
    :param request_body: 
    :type request_body: List[str]

    :rtype: Union[List[str], Tuple[List[str], int], Tuple[List[str], int, Dict[str, str]]
    """
    return 'do some magic!'
