from distutils.command.config import config
from flaskext.mysql import MySQL    
from flask import Flask, jsonify
from config import config
import pymysql

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST'] = "sql3.freemysqlhosting.net"
app.config['MYSQL_DATABASE_USER'] = "sql3473013"
app.config['MYSQL_DATABASE_PASSWORD'] = "zK2gbh194E"
app.config['MYSQL_DATABASE_DB'] = "sql3473013"

mysql.init_app(app)


# https://www.youtube.com/watch?v=D6LZnrDbQPM&t=1138s
@app.route('/users')
def listar_users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
   

#respuesta error 404

def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada...</h1>"
            


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()