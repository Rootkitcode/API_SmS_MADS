
from functools import wraps
from pickle import GET
from sqlite3 import connect
import pymysql
from distutils.command.config import config
from conection_db.connection import *    
from flask import Flask, jsonify, render_template, request
from config import config



'''rutas get clients, user_plans, sms send, paises, admin, user contrl'''
app = Flask(__name__)

from endpoints.endpoints_post import app



''' Endpoins post

'/users_data'
'/message'
'/clientes_empresa'
'/prueba_sms
'/support_tickets'
'/support_messages'
'/sms_logs/<int:id>'
'/registro_clientes_planes/<int:id>'
'/receptor_sms/<int:documento>'
'/numeros_telefonos/<int:id>' '''


from flask import request



def userData():
    # try:
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    username = request.form['username']
    password = request.form['password']
    country = request.form['country']
    city = request.form['city']
    post_code = request.form['post_code']
    address = request.form['address']
    if request.method =='POST':
            # conn = mysql.connect()
            # cursor = conn.cursor(pymysql.cursors.DictCursor)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users_data(name, email, mobile, username, password, country, city, post_code, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (name, email, mobile, username, password, country, city, post_code, address))
        cur.connection.commit()
        return jsonify({'message': 'user data added successfully' +
            str(name) + str(email) + str(mobile) + str(username) + str(password) + str(country) + str(city) + str(post_code) + str(address)})
    # except Exception as e:
    #     return jsonify({'message': 'user data not added'})



def messages():
    try:
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO messages(id, mensaje, fecha, estado) VALUES(%s, %s, %s, %s)",
            (id, mensaje, fecha, estado))
            mysql.connection.commit()
            id = request.form['id']
            mensaje = request.form['mensaje']
            fecha = request.form['user_id']
            estado = request.form['date']
            return jsonify({'message': 'message added successfully' + str(id) +
             str(mensaje) + str(fecha) + str(estado)})
    except Exception as e:
        return jsonify({'message': 'message not added'})


def cleintes_empresa():
    try:
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO clientes_empresa(id, nombre, apellidos, numero_telefono, pais, ciudad, direccion) VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (id, nombre, apellidos, numero_telefono, pais, ciudad, direccion))
            mysql.connection.commit()
            id = request.form['id']
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            numero_telefono = request.form['numero_telefono']
            pais = request.form['pais']
            ciudad = request.form['ciudad']
            direccion = request.form['direccion']
            return jsonify({'message': 'clientes empresa added successfully' + str(id) +
                str(nombre) + str(apellidos) + str(numero_telefono) + str(pais) + str(ciudad) + str(direccion)})
    except Exception as e:
            return jsonify({'message': 'clientes empresa not added'})


def prueba_sms():
    try:
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO prueba_sms(documento, nombre, telefono, ciudad) VALUES(%s, %s, %s, %s)",
            (documento, nombre, telefono, ciudad))
            mysql.connection.commit()
            documento = request.form['documento']
            nombre = request.form['nombre']
            telefono = request.form['telefono']
            ciudad = request.form['ciudad']
            return jsonify({'message': 'prueba addes successfully' + str(documento) +
                str(nombre) + str(telefono) + str(ciudad)})
    except Exception as e:
            return jsonify({'message': 'prueba sms not added'})



def support_tickets():
    try:
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO support_tickets(id, ticket, from_sms, to_sms, subject, status) VALUES(%s, %s, %s, %s, %s, %s)",
            (id, ticket, from_sms, to_sms, subject, status))
            mysql.connection.commit()
            id = request.form['id']
            ticket = request.form['ticket']
            from_sms = request.form['from_sms']
            to_sms = request.form['to_sms']
            subject = request.form['subject']
            status = request.form['status']
            return jsonify({'message': 'support ticket added successfully' + str(id) +
                str(ticket) + str(from_sms) + str(to_sms) + str(subject) + str(status)})
    except Exception as e:
            return jsonify({'message': 'support ticket not added'})



def supportMessages():
    try:
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.Discursosr)
            cursor.execute("INSERT INTO support_messages(id, support_ticket_id, type_message,  message) VALUES(%s, %s, %s, %s')",
            (id, support_ticket_id, type_message,  message ))
            mysql.connection.commit()
            id = request.form['id']
            support_ticket_id = ['support_ticket_id']
            type_message = ['type_message']
            message = ['message']
            return jsonify({'message': 'support message added successfully' + str(id) + str(support_ticket_id) +
                str(type_message) + str('message')})
    except Exception as e:
            return jsonify({'message': ' support message no added Error'})
