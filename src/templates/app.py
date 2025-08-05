from Flask import Flask

app = Flask(__name__)

if __name__ == '_main_':
    app.run()
    
    
 from flask import Flask, render_template, request

app = Flask(__name__)

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
   
    