from vpn import app
import os

if __name__ == '__main__':
    from waitress import serve
    serve(app, host=os.environ.get('APP_HOST'), port=os.environ.get('APP_PORT'))
