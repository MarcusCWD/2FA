from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from flask import Flask
from sqlalchemy.orm import Session
from vpn.models import Base
from vpn.dbconnection import engine
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            )

bcrypt = Bcrypt(app)

# SECRET_KEY is used for CSRF
app.config['SECRET_KEY'] = os.environ.get('CSRF_SECRET_KEY')

# Create the database tables
if os.environ.get('DEVELOPER_MODE'):
    Base.metadata.create_all(bind=engine)

# Create a SQLAlchemy session
db = Session(bind=engine)

from vpn import routes
