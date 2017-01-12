from bottle import Bottle, route
from sklearn import datasets
from time import sleep

app = Bottle()

@app.route('/')
def hello():
    datasets.load_iris()
    yield 'Example of yielded output..'
    sleep(1)
    yield 'Simulating some asynchronous stuff...'
    sleep(2)
    yield '...and more!!'
