from functools import wraps
from importlib.resources import Resource
from sqlite3 import connect
import pymysql
from distutils.command.config import config
from conection_db.connection import *  
from flask import Flask, jsonify, request, make_response
from config import config
from endpoints.endpoints_put import app

app = Flask(__name__)

'''rutas de actualizacion de datos endpoints put
'/message'
'/clientes_empresa'

'''


def messages_update(id):
    try:
        request_body = request.get_json()
        mensaje = request_body['mensaje']
        fecha = request_body['fecha']
        estado = request_body['estado']
        if request.method =='PUT':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("UPDATE messages SET mensaje =%s, fecha =%s, estado =%s WHERE id =%s",
            (mensaje, fecha, estado, id))
            cursor.connection.commit()
            return jsonify({'messages': 'messages updated successfully' +
                str(mensaje) + str(fecha) + str(estado)})
    except Exception as e:
            return jsonify({'messages': 'messages not updated', 'error': str(e)})


def clientes_empresa_update(id):
    try:
        request_body = request.get_json()
        nombre = request_body['nombre']
        apellidos = request_body['apellidos']
        numero_telefono = request_body['numero_telefono']
        pais = request_body['pais']
        ciudad = request_body['ciudad']
        direccion = request_body['dirreccion']
        if request.method =='PUT':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("UPDATE clientes_empresa SET nombre =%s, apellidos =%s, numero_telefono =%s, pais =%s, ciudad =%s, dirreccion =%s WHERE id =%s",
            (nombre, apellidos, numero_telefono, pais, ciudad, direccion, id))
            cursor.connection.commit()
            return jsonify({'clientes_empresa': 'clientes_empresa updated successfully' +
                str(nombre) + str(apellidos) + str(numero_telefono) + str(pais) +
                str(ciudad) + str(direccion)})
    except Exception as e:
            return jsonify({'clientes_empresa': 'clientes_empresa not updated', 'error': str(e)})