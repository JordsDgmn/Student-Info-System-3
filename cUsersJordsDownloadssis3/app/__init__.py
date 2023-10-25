from flask import Flask, render_template
from flask_mysql_connector import MySQL
from flask_sqlalchemy import SQLAlchemy
#flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ssis123@localhost/SSISv3'

#routes
@app.route('/')

def index():
    return render_template("index.html")
