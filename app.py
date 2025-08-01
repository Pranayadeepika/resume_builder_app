from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    data = request.form.to_dict()
    photo = request.files['photo']
    if photo:
        filename = secure_filename(photo.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        photo.save(filepath)
        data['photo_path'] = filepath
    else:
        data['photo_path'] = None

    return render_template('resume_template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
