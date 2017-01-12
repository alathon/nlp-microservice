from gevent import monkey; monkey.patch_all()
from time import sleep
from bottle import route, run
import os
from sklearn import datasets

@route('/')
def hello():
    datasets.load_iris()
    yield 'START'
    sleep(5)
    yield 'MORE'

appPort = int(os.environ.get('PORT', 5000))
run(host='0.0.0.0', port=appPort, server='gevent', debug=True)
