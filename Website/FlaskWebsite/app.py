"""
This script runs the FlaskWebsite application using a development server.
"""

from os import environ
from FlaskWebsite import app

#if __name__ == '__main__':
#    HOST = environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)