# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Configure the Flask application to use PostgreSQL as the database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost/mg_connect"

# Create a SQLAlchemy instance and bind it to the Flask app
db = SQLAlchemy(app)

# Create a Migrate instance and associate it with the Flask app and SQLAlchemy instance
migrate = Migrate(app, db)

# Import routes and models to ensure they are registered with the app
from app import routes, models
