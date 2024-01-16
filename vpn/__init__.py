from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from flask import Flask
from sqlalchemy.orm import Session
from vpn.models import Base
from vpn.dbconnection import engine
import os

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            )

# SECRET_KEY is used for CSRF
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Create the database tables (SERIOUSLY. REMEMBER TO DELETE)
Base.metadata.create_all(bind=engine)

# Create a SQLAlchemy session
db = Session(bind=engine)

from vpn import routes
