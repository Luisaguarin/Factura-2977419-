from flask import render_template, request
from flask_controller import FlaskConroller
from src.models.clientes import Clientes
from src.app import app

class ClientesController(FlaskConroller):
    @app.route('/from_clientes')
    def lista_clientes():
        try:
            clientes = Clientes.traer_clientes()
            return render_template('from_clientes.html',titulo='Ver clientes',clientes = clientes)
        except:
            return render_template('from_clientes.html', titulo='Error conexion base de datos')
        