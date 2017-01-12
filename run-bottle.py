from bottle import route, run
from sklearn import datasets

@route('/')
def hello():
    datasets.load_iris()
    return "Hello World!"

appPort = int(os.environ.get('PORT', 5000))
run(host='0.0.0.0', port=appPort, debug=True)
