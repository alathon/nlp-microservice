# Test of Scikit-Learn deployed via Flask microservice

A barebones Python 2.7.x Flask application, served via Gunicorn using WSGI,
using Miniconda to install Scikit-Learn and required dependencies.

## Installing

1. Install Miniconda2
2. Clone repository
3. Create new conda environment: `conda create -n yourEnvName python`
4. Run `conda install --file conda-requirements.txt --yes`

Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and
[Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

## Running locally

You can either run `heroku local`, which will run the WSGI through gunicorn, or
you can run `python main.py`. Suggest running python, as this will use the Werkzeug
webserver which has debug-mode allowing automatic reload on code change.

The app should now be running on [localhost:5000](http://localhost:5000/).

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
