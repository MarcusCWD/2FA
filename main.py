from vpn import app
import os

if __name__ == '__main__':
    host=os.environ.get('APP_HOST')
    port = os.environ.get('APP_PORT')
    print(f'App Starting on host {host} with port {port}')
    from waitress import serve
    serve(app, host=host, port=port)

