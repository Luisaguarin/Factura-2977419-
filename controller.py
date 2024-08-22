from Flask import render_template
from app import app

@app.route("/")
def index():
    return render_template('index.html' , title= "App facturacion")

@app.route("/clientes")
def clientes():
    return render_template('clientes.html' , title="Lista de clientes")

@app.route ("/from_cliente")
def form_cliente():
    return render_template('from_cliente.html' , title="Formulario de clientes")

from controllers import *

if __name__ == '_main_':
    app.run(debug-True)
    
@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
     # Aquí puedes procesar los datos, como guardarlos en una base de datos
    return f'Formulario enviado! Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}'

if __name__ == '__main__':
    app.run(debug=True)
   
   # Simulando una base de datos de usuarios
usuarios = {
    "usuario1": "contrasena1",
    "usuario2": "contrasena2"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in usuarios and usuarios[username] == password:
        return "Bienvenido, " + username + "!"
    else:
        return "Usuario o contraseña incorrectos."

if __name__ == '__main__':
 app.run(debug=True)
    