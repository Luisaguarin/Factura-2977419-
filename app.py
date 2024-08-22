

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///facturacion.db'

db = SQLAlchemy(app)


   
    
with app.app_context():
    db.create_all()
    
from controllers import *

if __name__ == '_main_':
    app.run(debug-True)
    




    