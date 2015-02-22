__author__ = 'torresmateo'

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = '/tmp/database.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# create application
app = Flask(__name__)
app.config.from_object(__name__)

#run app
if __name__ == '__main__':
    app.run()