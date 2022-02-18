from distutils.command.config import config
from flaskext.mysql import MySQL    
from flask import Flask, jsonify, request
from config import config
import pymysql

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "laravel"

mysql.init_app(app)
 


@app.route('/')
def index():
    return '<h1>Hola Mundo</h1>'

@app.route('/users/<int:id>', methods=['GET'])
def listar_users_get(id):
    try:
        if request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT name, email FROM users WHERE id = {0}" .format(id))
            rows = cursor.fetchall()
            respuesta = jsonify(rows)
            respuesta.status_code = 200
            return respuesta
        else:
            return '<h1>Metodo no soportado</h1>'
    except Exception as e:
        return jsonify ("Error en la coneccion de la base de datos",e)


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
    # finally:
    #     cursor.close()
    #     conn.close()
   

#respuesta error 404

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada...</h1>"
            


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()


