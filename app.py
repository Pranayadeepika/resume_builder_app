from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    data = request.form.to_dict(flat=False)
    photo = request.files['photo']
    if photo and photo.filename:
        photo_path = os.path.join('static', photo.filename)
        photo.save(photo_path)
        data['photo_path'] = photo_path
    else:
        data['photo_path'] = None
    return render_template('resume_template.html', data=data, datetime=datetime)

if __name__ == '__main__':
    app.run(debug=True)
