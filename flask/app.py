from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flask-health-check')
def flask_health_check():
    return "success"
