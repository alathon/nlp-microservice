from gevent import monkey; monkey.patch_all()
from bottle import Bottle, run, debug
import os
from routes import one

# Environment variables
debugMode = os.environ.get('DEBUG', False)
appPort = int(os.environ.get('PORT', 5000))

# Create parent app and mount child routes
app = Bottle()
app.mount('/one/', one.app)

if __name__ == '__main__':
    if debugMode:
        debug(True)
    run(app, host = '0.0.0.0', port=appPort, server='gevent', reloader=True)
