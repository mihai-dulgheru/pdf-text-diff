import json
import os
import tempfile

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from functions import extract_text_from_pdfs, find_text_differences

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flask-health-check')
def flask_health_check():
    return "success"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the files
        file1 = request.files['file1']
        file2 = request.files['file2']

        # Download temporary files
        file1_path = os.path.join(tempfile.gettempdir(), secure_filename(file1.filename))
        file2_path = os.path.join(tempfile.gettempdir(), secure_filename(file2.filename))
        file1.save(file1_path)
        file2.save(file2_path)

        ocr_dic = extract_text_from_pdfs([file1.filename, file2.filename])
        diffs = find_text_differences(ocr_dic)

        # Delete temporary files
        os.remove(file1_path)
        os.remove(file2_path)

        return render_template('index.html', diffs=json.dumps(diffs, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        return render_template('index.html')
