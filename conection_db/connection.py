from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL()

mysql.init_app(app)



app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "laravel"