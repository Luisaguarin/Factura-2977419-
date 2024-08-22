from flask import flask
from models import Base, engine

appm = flask(__name__)


from controller import* 
Base.netadata.create_all (engine)



if _name_ == '_main_':
    app.run (debug-True)




    