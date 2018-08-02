from app import mywebsite
from flask import request,render_template,url_for,redirect,send_from_directory
 

# Index Route
@mywebsite.route('/')
@mywebsite.route('/index')
@mywebsite.route('/index/')
def index(method='GET'):
    return render_template('index.html')


