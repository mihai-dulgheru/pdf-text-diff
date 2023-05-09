import os
import tempfile

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flask-health-check')
def flask_health_check():
    return "success"


@app.route('/upload', methods=['POST'])
def upload():
    # Get the files
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Download temporary files
    file1_path = os.path.join(tempfile.gettempdir(), secure_filename(file1.filename))
    file2_path = os.path.join(tempfile.gettempdir(), secure_filename(file2.filename))
    file1.save(file1_path)
    file2.save(file2_path)

    # Display a message to the console
    print(f"Files '{file1.filename}' and '{file2.filename}' have been loaded successfully.")

    # Delete temporary files
    os.remove(file1_path)
    os.remove(file2_path)

    return "Files have been uploaded and processed successfully."
