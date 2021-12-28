#pylint: disable=no-member
import os
import logging
from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

host: str = os.getenv('DB_HOST', 'localhost')
port: int = int(os.getenv('DB_PORT', '5432'))
user: str = os.getenv('DB_USER', 'postgres')
password: str = os.getenv('DB_PASSWORD', '')
name = os.getenv('DB_NAME', 'challenge_starter_development')
db_url = f'postgresql://{user}:{password}@{host}:{port}/{name}'

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_url
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(flask_app)

Session = sessionmaker(bind=DB.engine)

CORS(flask_app)

gunicorn_logger = logging.getLogger('gunicorn.error')
gunicorn_logger.setLevel(logging.INFO)

flask_app.logger.handlers = gunicorn_logger.handlers
flask_app.logger.setLevel(gunicorn_logger.level)
