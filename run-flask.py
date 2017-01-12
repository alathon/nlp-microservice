from flask import Flask
from sklearn import datasets

application = Flask(__name__)

@application.route("/")
def hello():
  iris = datasets.load_iris()
  X = iris.data[:, :2]
  Y = iris.target

  return 'Items: %s' % (', '.join([str(x) for x in X]))

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=5000, debug=True)
