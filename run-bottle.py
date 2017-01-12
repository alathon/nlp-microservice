from bottle import route, run
from sklearn import datasets

@route('/')
def hello():
    datasets.load_iris()
    return "Hello World!"

run(host='0.0.0.0', port=5000, debug=True)
