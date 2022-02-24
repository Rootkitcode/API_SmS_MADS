# import jwt
# import datetime

from functools import wraps
from pickle import GET
from sqlite3 import connect
import pymysql
from distutils.command.config import config
from conection_db.connection import *    
from flask import Flask, jsonify, request, make_response
from config import config



'''rutas get clients, user_plans, sms send, paises, admin, user contrl'''
app = Flask(__name__)




@app.route('/')
def home():
    return "<h1>Bienvenido a la API de la aplicacion de SMS</h1>"
      

#endpoint para obtener datos de los usuarios clientes de SMS MADS

@app.route('/users_data/<int:id>', methods=['GET'])
def listar_users_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, name, email, mobile, username, image, country, city, post_code, address FROM users_data WHERE id = '{0}'" .format(id))
            rows = cursor.fetchone()
            if rows != None:
                respuesta = jsonify(rows)
                respuesta.status_code = 200
                return jsonify('ok 200', rows)
            else:
                return jsonify ('<h1>No hay datos en la db</h1>')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#Endpoin que permite obtener los mensajes sms enviados a los usuarios finales
@app.route('/message/<int:id>', methods=['GET'])
def message_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, mensaje, fecha, estado FROM messages WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id') 
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


# endpoint que permite consultar el cliente final que recibe los sms
@app.route('/clientes_empresa/<int:id>', methods=['GET'])
def clientes_empresa_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, nombre, apellidos, numero_telefono, pais, ciudad, direccion FROM clientes_empresa WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id') 
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#Endpoint que me permite obtener las pruebas de envio de sms
@app.route('/prueba_sms/<int:documento>', methods=['GET'])
def prueba_sms_get(documento):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT documento, nombre, telefono, ciudad FROM prueba_sms WHERE documento = '{0}'".format(documento))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el documento') 
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#Endpoint que me permite obtener informacion de las transacciones
@app.route('/transactions/<int:id>', methods=['GET'])
def transactions_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, to_add, to_bal, from_add, from_bal, amount, type, trx FROM transections WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#endpoint para obtener el token de la empresa
@app.route('/token_api/<int:id>', methods=['GET'])
def token(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, token FROM token_api WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el token id')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)



#endpoint para obtener los tikets de soporte
@app.route('/support_tickets/<int:id>', methods=['GET'])
def support_tickets_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, user_id, subject, status FROM support_tickets WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del support')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)




#endpoint para obtener los tikets de soporte
@app.route('/support_messages/<int:id>', methods=['GET'])
def support_messages_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, support_ticket_id, type, message FROM support_messages WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del support')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)

#endpoint que permite obtener los logs de los sms
@app.route('/sms_logs/<int:id>', methods=['GET'])
def sms_logs_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, user_id, number, status FROM sms_logs WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del sms')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#endpoint para obtener empresas registras
@app.route('/registro_clientes_planes/<int:id>', methods=['GET'])
def registro_clientes_planes_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, email, nombre_empresa, nit_empresa, ciudad, telefono, representante, planes_sms, sms_1_alerta, sms_2_alerta FROM registro_clientes_planes WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del registro')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


#endpoint para obtener el receptor de los sms
@app.route('/receptor_sms/<int:documento>', methods=['GET'])
def receptor_sms_delete(documento):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT documento, nombre, telefono, ciudad FROM receptor_sms WHERE documento = '{0}'".format(documento))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del registro')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)


@app.route('/numeros_telefonos/<int:id>', methods=['GET'])
def numeros_telefono_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT id, fecha, telefonos FROM numeros_telefonos WHERE id = '{0}'".format(id))
            row = cursor.fetchone()
            if row != None:
                respuesta = jsonify(row)
                respuesta.status_code = 200
                return jsonify ('ok coneccion exitosa', row)
            else:
                return jsonify ('No se encontro el id del numero')
    except Exception as e:
                return jsonify ("Error en la coneccion de la base de datos",e)



def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada...</h1>"
            


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
    