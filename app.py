#This code is from  https://github.com/prince8801singh/flask-app-ecs/tree/main
#Hello Dosto , har Har Mahadev
#Test
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return None


@app.route('/health')
def health():
    return 'Server is up and running'
