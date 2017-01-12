from bottle import route, run
from sklearn import datasets

@route('/')
def hello():
    datasets.load_iris()
    return "Hello World!"

run(host='localhost', port=8080, debug=True)
