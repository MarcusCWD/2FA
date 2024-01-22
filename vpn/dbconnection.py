import os
from sqlalchemy import create_engine
from urllib.parse import quote

# Connection to Database i.e 'mysql+mysqlconnector://root:password@localhost:3307/market.db'
database_connector = 'mysql+mysqlconnector'
DATABASE_URL = (
    f'{database_connector}://'
    + os.environ.get('DATABASE_USER')
    + ':'
    + quote(os.environ.get('DATABASE_PASSWORD'))
    + '@'
    + os.environ.get('DATABASE_ADDRESS')
    + ':'
    + os.environ.get('DATABASE_PORT')
    + '/'
    + os.environ.get('DATABASE_NAME')
)

engine = create_engine(DATABASE_URL)