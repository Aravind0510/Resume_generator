# Resume Generator

## Project Overview

The **Resume Generator** is a web application designed to convert LinkedIn profile PDFs into HTML resumes. This project leverages the Flask framework for backend processing and provides a user-friendly interface to upload LinkedIn PDFs, convert them to HTML, and preview the results. The application is deployed on Heroku and demonstrates effective use of AI tools for text extraction from PDFs.

## Features

- **Upload LinkedIn PDF**: Users can upload their LinkedIn profile in PDF format.
- **Generate HTML Resume**: The application processes the PDF and generates an HTML version of the resume.
- **Preview Resume**: Users can view the HTML resume directly on the web page.

## Technologies Used

- **Flask**: A lightweight Python web framework used for backend development.
- **PyPDF2**: A Python library for reading and extracting text from PDF files.
- **HTML/CSS**: For creating the user interface and styling the application.
- **Heroku**: For deploying the application online.

## Installation and Setup

### Prerequisites

- Python 3.x
- Virtual Environment
- Flask
- PyPDF2

### Steps to Set Up Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/resume-generator.git
   cd resume-generator

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`

3. **Run the Application**

   ```bash
   python app.py
- This will start a local server. You can access the application at http://127.0.0.1:5000 in your web browser.

## How It Works
### 1. User Interface

-  **Home Page:** Provides a form to upload the LinkedIn PDF file.
-  **Preview Page**: Displays the generated HTML resume.
## 2. Backend Processing

-  **PDF Upload**: The user uploads a PDF file through a form.
- **PDF Processing**: The generate_html_resume function extracts text from the PDF using PyPDF2 and converts it into HTML.
- **HTML Generation**: An HTML file is generated and saved on the server.
- **Preview**: The HTML resume is served to the user for preview.

## Usage
- Navigate to the home page of the application.
- Upload your LinkedIn PDF using the file input field.
- Click the "Generate Resume" button.
- The generated HTML resume will be displayed in an iframe below the form.

## Directory Structure
  ```bash
   resume-generator/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── Procfile               # Heroku process file
├── static/
│   └── style.css         # Stylesheet for the application
├── templates/
│   └── index.html        # HTML template for the application
└── README.md             # Project documentation
```

## Contributing
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.
  
## Demo Video
Watch a demonstration of the Resume Generator application on YouTube: **https://youtu.be/egV8onYpeH0**


## License
This project is licensed under the MIT License - see the LICENSE file for details.
