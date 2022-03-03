from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)
mysql = MySQL()

mysql.init_app(app)



app.config['MYSQL_DATABASE_HOST'] = "localhost"
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ""
app.config['MYSQL_DATABASE_DB'] = "laravel2"


# app.config.setdefault("MYSQL_UNIX_SOCKET", None)
# app.config.setdefault("MYSQL_CONNECT_TIMEOUT", 10)
# app.config.setdefault("MYSQL_READ_DEFAULT_FILE", None)
# app.config.setdefault("MYSQL_USE_UNICODE", True)
# app.config.setdefault("MYSQL_CHARSET", "utf8")
# app.config.setdefault("MYSQL_SQL_MODE", None)
# app.config.setdefault("MYSQL_CURSORCLASS", None)
# app.config.setdefault("MYSQL_AUTOCOMMIT", False)
# app.config.setdefault("MYSQL_CUSTOM_OPTIONS", None)

