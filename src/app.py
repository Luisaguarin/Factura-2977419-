from flask import Flask, render_template, request, redirect, url_for
from src.controllers.productos import productos_bp  
from src.models import Base, engine
from src.routes.clientes import clientes_bp


app = Flask(__name__)
app.register_blueprint(productos_bp)
app.register_blueprint(clientes_bp)


Base.metadata.create_all(engine)


@app.route('/')
def home():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)

