
from functools import wraps
from sqlite3 import connect
import pymysql
from distutils.command.config import config
from conection_db.connection import *    
from flask import Flask, jsonify, render_template, request, session
from config import config



'''rutas get clients, user_plans, sms send, paises, admin, user contrl'''
app = Flask(__name__)




''' Endpoins post

'/users_data'
'/message'
'/clientes_empresa'
'/prueba_sms
'/support_tickets'
'/support_messages'
'/registro_clientes_planes'
 '''


from flask import request



def userData():
    try:
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
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO users_data(name, email, mobile, username, password, country, city, post_code, address) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, email, mobile, username, password, country, city, post_code, address))
            cursor.connection.commit()
            return jsonify({'message': 'user data added successfully' +
                str(name) + str(email) + str(mobile) + str(username) + str(password) + str(country) + str(city) + str(post_code) + str(address)})
    except Exception as e:
        return jsonify({'message': 'user data not added' + str(e)})



def messages():
    try:
        mensaje = request.form['mensaje']
        fecha = request.form['fecha']
        estado = request.form['estado']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO messages(mensaje, fecha, estado) VALUES(%s, %s, %s)",
            (mensaje, fecha, estado))
            cursor.connection.commit()
            return jsonify({'message': 'message added successfully' +
             str(mensaje) + str(fecha) + str(estado)})
    except Exception as e:
        return jsonify({'message': 'message not added' + str(e)})


def cleintes_empresa():
    try:
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        numero_telefono = request.form['numero_telefono']
        pais = request.form['pais']
        ciudad = request.form['ciudad']
        direccion = request.form['direccion']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO clientes_empresa(nombre, apellidos, numero_telefono, pais, ciudad, direccion) VALUES(%s, %s, %s, %s, %s, %s)",
            (nombre, apellidos, numero_telefono, pais, ciudad, direccion))
            cursor.connection.commit()
            return jsonify({'message': 'clientes empresa added successfully'  +
                str(nombre) + str(apellidos) + str(numero_telefono) + str(pais) + str(ciudad) + str(direccion)})
    except Exception as e:
            return jsonify({'message': 'clientes empresa not added' + str(e)})


def prueba_sms():
    try:
        documento = request.form['documento']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        ciudad = request.form['ciudad']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO prueba_sms(documento, nombre, telefono, ciudad) VALUES(%s, %s, %s, %s)",
            (documento, nombre, telefono, ciudad))
            cursor.connection.commit()
            return jsonify({'message': 'prueba addes successfully' + str(documento) +
                str(nombre) + str(telefono) + str(ciudad)})
    except Exception as e:
            return jsonify({'message': 'prueba sms not added' + str(e)})



def support_tickets():
    try:
        ticket = request.form['ticket']
        from_sms = request.form['from_sms']
        to_sms = request.form['to_sms']
        subject = request.form['subject']
        status = request.form['status']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO support_tickets(ticket, from_sms, to_sms, subject, status) VALUES(%s, %s, %s, %s, %s)",
            (ticket, from_sms, to_sms, subject, status))
            cursor.connection.commit()
            return jsonify({'message': 'support ticket added successfully' +
                str(ticket) + str(from_sms) + str(to_sms) + str(subject) + str(status)})
    except Exception as e:
            return jsonify({'message': 'support ticket not added' + str(e)})



def supportMessages():
    try:
        support_ticket_id = ['support_ticket_id']
        type_message = ['type_message']
        message = ['message']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO support_messages(support_ticket_id, type_message,  message) VALUES(%s, %s, %s')",
            (support_ticket_id, type_message,  message ))
            cursor.connection.commit()
            return jsonify({'message': 'support message added successfully' + str(support_ticket_id) +
                str(type_message) + str(message)})
    except Exception as e:
            return jsonify({'message': ' support message no added Error' + str(e)})



def registroClientePlanes():
    try:
        email = request.form['email']
        nombre_empresa = request.form['nombre_empresa']
        nit_empresa = request.form['nit_empresa']
        ciudad = request.form['ciudad']
        telefono = request.form['telefono']
        representante = request.form['representante']
        planes_sms = request.form['planes_sms']
        sms_1_alerta = request.form['sms_1_alerta']
        sms_2_alerta = request.form['sms_2_alerta']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("INSERT INTO registro_clientes_planes(email, nombre_empresa, nit_empresa, ciudad, telefono, representante, planes_sms, sms_1_alerta, sms_2_alerta) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (email ,nombre_empresa, nit_empresa, ciudad, telefono, representante, planes_sms, sms_1_alerta, sms_2_alerta))
            cursor.connection.commit()
            return jsonify({'message': 'clientes planes added successfully' + str(email) +
                str(nombre_empresa) + str(nit_empresa) + str(ciudad) + str(telefono) + str(representante) + str(planes_sms) + str(sms_1_alerta) + str(sms_2_alerta)})
    except Exception as e:
            return jsonify({'message': 'clientes planes not added' + str(e)})


def authUser():
    try:
         email = request.form['email']
         password = request.form['password']
         conn = mysql.connect()
         cursor = conn.cursor(pymysql.cursors.DictCursor)
         cursor.execute("SELECT email, password FROM users WHERE email = %s AND password = %s", (email, password))
         row = cursor.fetchone()
         if row:
             session['loggedin'] = True
             session['email'] = row['email']
             session['password'] = row['password']
             return jsonify({'message': 'User logged in successfully'})
         else:
             return jsonify({'message': 'User not found'})
    except Exception as e:
         return jsonify({'message': 'User not logged in users table ' + str(e)})