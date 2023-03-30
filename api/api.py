
import os
import sqlalchemy
import pandas as pd
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text, engine
from datetime import datetime
from flask_restx import Api, Namespace, Resource, reqparse, inputs, fields

# Set up Google Cloud SQL connection information
user = 'root'
passw = 'MCSbt2023'
host = '34.175.175.68'
database = 'HyM'
port = 3306

# Set up the API key
api_key= "SecretCapstoneKey"

#Define decortaor for API key

def require_appkey(view_function):
    def wrapper(*args, **kwargs):
        provided_key = request.headers.get('X-API-KEY')
        print("Provided API Key: ", provided_key)	
        if provided_key == api_key:
            return view_function(*args, **kwargs)
        else:
            return {'message': 'Unauthorized'}, 401
    return wrapper

# Create a Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = host

# Create a Flask-RESTX API instance
api = Api(app, version = '1.0',
    title = 'H&M KPIs',
    description = """
        This RESTS API is an API to build a dashboard for H&M. 
        It is built using the FLASK
        """,
    contact = "edgardo.alvarez@student.ie.edu",
    endpoint = "/api/v1"
)

def connect():
    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}:{3}/{4}' \
        .format(user, passw, host,port, database), \
    connect_args = {'connect_timeout': 10})
    conn = db.connect()
    return conn

def disconnect(conn):
    conn.close()

customers = Namespace('customers',
    description = 'All details related to customers',
    path='/api/v1')
api.add_namespace(customers)

@customers.route("/customers")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM customers
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

articles = Namespace('articles',
    description = 'All details related to articles',
    path='/api/v1')
api.add_namespace(articles)

@articles.route("/articles")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM articles
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
        
transactions = Namespace('transactions',
    description = 'All details related to transactions',
    path='/api/v1')
api.add_namespace(transactions)

@transactions.route("/transactions")
class get_all_users(Resource):
    @require_appkey   
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM transactions
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

KPI = Namespace('KPI',
    description = 'All details related to KPI',
    path='/api/v1')
api.add_namespace(KPI)

@KPI.route("/KPI")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM KPI
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})
            
KPI_age = Namespace('KPI_age',
    description = 'All details related to KPI_age',
    path='/api/v1')
api.add_namespace(KPI_age)

@KPI_age.route("/KPI_age")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM KPI_age
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

KPI_date = Namespace('KPI_date',
    description = 'All details related to KPI_date',
    path='/api/v1')
api.add_namespace(KPI_date)

@KPI_date.route("/KPI_date")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM KPI_date
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

KPI_product_group = Namespace('KPI_product_group',
    description = 'All details related to KPI_product_group',
    path='/api/v1')
api.add_namespace(KPI_product_group)

@KPI_product_group.route("/KPI_product_group")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM KPI_product_group
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

KPI_saleschannel = Namespace('KPI_saleschannel',
    description = 'All details related to KPI_saleschannel',
    path='/api/v1')
api.add_namespace(KPI_saleschannel)

@KPI_saleschannel.route("/KPI_saleschannel")
class get_all_users(Resource):
    @require_appkey
    def get(self):
        conn = connect()
        select = text("""
            SELECT *
            FROM KPI_saleschannel
            LIMIT 1000;""")
        result = conn.execute(select).fetchall()
        disconnect(conn)
        return jsonify({'result': [dict(row) for row in result]})

if __name__ == '__main__':
    app.run(debug=True)
