from flask import Flask, render_template, request, send_file
from io import BytesIO
from xhtml2pdf import pisa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    rendered = render_template('resume_template.html', data=data)

    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(rendered, dest=pdf)

    if pisa_status.err:
        return "Error generating PDF", 500

    pdf.seek(0)
    return send_file(pdf, as_attachment=True, download_name='resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)
