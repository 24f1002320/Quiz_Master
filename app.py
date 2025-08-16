from flask import Flask
from application.database import db # import database
from application.api_controllers import * 

app=None

def create_app():
    app=Flask(__name__)
    app.debug=True
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ecard.sqlite3" #3 databse file name 
    api.init_app(app) # flask app connect to api
    db.init_app(app) #3 database
    app.app_context().push()#runtime error,everything under context of flask application 
    return app 

app=create_app()
from application.controllers import *  #2
#from application.database import * indirect import by controllers.py

if __name__=="__main__":
    app.run()

#pip install -r requirements.txt