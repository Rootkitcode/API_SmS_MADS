from functools import wraps
from sqlite3 import connect
import pymysql
from distutils.command.config import config
from conection_db.connection import *    
from flask import Flask, jsonify, render_template, request
from config import config
from endpoints.endpoints_delete import app

'''endpoints delete
'/delete/admin/<int:id>'
'/delete/clientes_empresa/<int:id>'
'/delete/numeros_telefono/<inte:id>'
'/delete/users_data/<int:id>'

'''




def delete_users_data(id):
    try:
        if request.method =='DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM users_data WHERE id =%s", (id))
            cursor.connection.commit()
            return jsonify({'users_data': 'users_data deleted successfully'})
    except Exception as e:
        return jsonify({'users_data': 'users_data not deleted', 'error': str(e)})


def delete_admin(id):
    try:
        if request.method == 'DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM admins WHERE id =%s", (id))
            cursor.connection.commit()
            return jsonify({'admin': 'admin deleted successfully'})
    except Exception as e:
            return jsonify({'admin': 'admin not deleted', 'error': str(e)})


def delete_clientes(id):
    try:
        if request.method == 'DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM clientes_empresa WHERE id =%s", (id))
            cursor.connection.commit()
            return jsonify({'clientes': 'clientes deleted successfully'})
    except Exception as e:
            return jsonify({'clientes': 'clientes not deleted', 'error': str(e)})


def delete_numeros_telefono(id):
    try:
        if request.method == 'DELETE':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("DELETE FROM numeros_telefonos WHERE id =%s", (id))
            cursor.connection.commit()
            return jsonify({'numeros_telefono': 'numeros_telefono deleted successfully'})
    except Exception as e:
            return jsonify({'numeros_telefono': 'numeros_telefono not deleted', 'error': str(e)})