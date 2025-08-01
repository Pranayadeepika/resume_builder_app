from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

resume_data = {}

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resume', methods=['POST'])
def resume():
    global resume_data
    resume_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'address': request.form['address'],
        'linkedin': request.form['linkedin'],
        'photo': request.form['photo'],
        'education': request.form['education'].split(','),
        'projects': request.form['projects'].split(','),
        'courses': request.form['courses'].split(','),
        'skills': request.form['skills'].split(','),
        'languages': request.form['languages'].split(','),
        'hobbies': request.form['hobbies'].split(','),
        'dob': request.form['dob'],
        'gender': request.form['gender'],
        'sign': request.form['sign']
    }
    return render_template('resume_template.html', **resume_data)

@app.route('/download')
def download_pdf():
    rendered = render_template('resume_template.html', **resume_data)
    pdfkit.from_string(rendered, 'resume.pdf')
    return send_file('resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
