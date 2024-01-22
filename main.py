from vpn import app
import os

if __name__ == '__main__':
    if os.environ.get('DEVELOPER_MODE'):
        app.run(debug=True, port=os.environ.get('APP_PORT'))
    else:
        from waitress import serve
        serve(app, host=os.environ.get('APP_HOST'), port=os.environ.get('APP_PORT'))
