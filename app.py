
from flask import Flask, render_template
from flask_swagger_ui import get_swaggerui_blueprint
from endpoints.endpoints_get import *
from endpoints.endpoints_post import *
from endpoints.endpoints_put import clientes_empresa_update, messages_update



app = Flask(__name__)

'''Rutas de endpoints get sms MADS'''
@app.route('/')
def wellcome():
    return render_template('user_data.html')


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "MADS"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/users_data/<int:id>', methods=['GET'])
def userdata(id):
    return listar_users_get(id)

@app.route('/message/<int:id>', methods=['GET'])
def message(id):
    return message_get(id)

@app.route('/clientes_empresa/<int:id>', methods=['GET'])
def clientes(id):
    return clientes_empresa_get(id)

@app.route('/prueba_sms/<int:documento>', methods=['GET'])
def prueba(documento):
    return prueba_sms_get(documento)

@app.route('/transactions/<int:id>', methods=['GET'])
def transactions(id):
    return transactions_get(id)

@app.route('/token_api/<int:id>', methods=['GET'])
def token_api(id):
    return token(id)

@app.route('/support_tickets/<int:id>', methods=['GET'])
def support(id):
    return support_tickets_get(id)

@app.route('/support_messages/<int:id>', methods=['GET'])
def support_messages(id):
    return support_messages_get(id)

@app.route('/sms_logs/<int:id>', methods=['GET'])
def sms_logs(id):
    return sms_logs_get(id)

@app.route('/registro_clientes_planes/<int:id>', methods=['GET'])
def registro_clientes_planes(id):
    return registro_clientes_planes_get(id)

@app.route('/receptor_sms/<int:documento>', methods=['GET'])
def receptor_sms(documento):
    return receptor_sms_get(documento)

@app.route('/numeros_telefonos/<int:id>', methods=['GET'])
def numeros_telefonos(id):
    return numeros_telefono_get(id)

@app.route('/respuesta/ticket/<int:id>', methods=['GET'])
def respuesta_ticket(id):
    return respuesta_ticket_get(id)



# endpoints post

@app.route('/add/user/data', methods=['POST'])
def userDa():
    return userData() #endpoint post

@app.route('/message', methods=['POST'])
def messagesPost():
    return messages()  # endpoints post

@app.route('/add/clientes/empresa', methods=['POST'])
def clientesEmpresa():
    return cleintes_empresa()  # endpoints post

@app.route('/prueba_sms', methods=['POST'])
def pruebSms():
    return prueba_sms()  # endpoints post

@app.route('/support_tickets', methods=['POST'])
def supportTickets():
    return support_tickets() # endpoints post

@app.route('/support_messages', methods=['POST'])
def supportMess():
    return supportMessages()

@app.route('/registro_clientes_planes', methods=['POST'])
def registroClientes(): # endpoints post
    return registro_clientes_planes()


#endpoins put

@app.route('/update_messages/<int:id>', methods=['PUT'])
def messagesPut(id):
    return messages_update(id)

@app.route('/update_clientes_empresa/<int:id>', methods=['PUT'])
def clientesEmpresaPut(id):
    return clientes_empresa_update(id)
    

if __name__ == '__main__':
    app.run(debug=True)







    