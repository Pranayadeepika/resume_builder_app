from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    rendered = render_template('resume_template.html', data=data)

    output_path = os.path.join('output', 'resume.pdf')
    pdfkit.from_string(rendered, output_path)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
