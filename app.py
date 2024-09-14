import os
import openai
import pdfkit
from dotenv import load_dotenv
import fitz  # PyMuPDF for PDF parsing
from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Directory to store uploaded files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs('UPLOAD_FOLDER')

# Configure pdfkit
pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.getenv('WKHTMLTOPDF_PATH'))

# Route for homepage
@app.route('/')
def index():
    return render_template("index.html")

# Route to handle file upload and resume generation
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(filepath)

        # Generate HTML resume using OpenAI API
        html_resume = generate_resume_from_text(pdf_text)

        # Save the HTML resume to a file
        resume_filename = filename.replace('.pdf', '.html')
        resume_filepath = os.path.join(UPLOAD_FOLDER, resume_filename)
        with open(resume_filepath, 'w') as file:
            file.write(html_resume)

        return jsonify({"message": "Resume generated", "resume_url": f"/view_resume/{resume_filename}"}), 200
    
    return jsonify({"message": "Invalid file format"}), 400

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF"""
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def generate_resume_from_text(text):
    """Generates an HTML-formatted resume from PDF text using the OpenAI chat model."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use 'gpt-4' if you have access
        messages=[
            {"role": "system", "content": "You are an assistant that formats resumes in HTML."},
            {"role": "user", "content": f"Generate an HTML formatted resume from the following text: {text}"}
        ],
        max_tokens=3000
    )
    return response['choices'][0]['message']['content'].strip()

@app.route('/view_resume/<filename>', methods=['GET'])
def view_resume(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.isfile(filepath):
        return jsonify({"message": "File not found"}), 404

    with open(filepath, 'r') as file:
        html_content = file.read()

    return render_template("resume_viewer.html", html_content=html_content, resume_filename=filename)

@app.route('/downloads/<filename>', methods=['GET'])
def download_pdf(filename):
    filename = secure_filename(filename)
    html_filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.isfile(html_filepath):
        return jsonify({"message": "File not found"}), 404

    pdf_filepath = html_filepath.replace('.html', '.pdf')

    # Convert HTML to PDF
    pdfkit.from_file(html_filepath, pdf_filepath, configuration=pdfkit_config)

    return send_file(pdf_filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
