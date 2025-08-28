# Image-Gallery-with-S3-bucket

A simple Flask-based web application that allows users to upload files securely to AWS S3 storage.
This project demonstrates how to integrate Flask with Amazon S3, manage credentials using dotenv, and build a clean frontend for uploading files.

🚀 Features

Upload files directly from the browser to AWS S3

Secure credential management using .env

Minimal and responsive UI with modern CSS

Flask backend with boto3 for AWS integration

Easy setup and deployment

🛠️ Tech Stack

Backend: Flask (Python)

Storage: AWS S3

Frontend: HTML, CSS (custom, responsive)

Environment Management: python-dotenv

⚙️ Setup Instructions

Clone the repo:

git clone https://github.com/your-username/cloud-file-uploader.git
cd cloud-file-uploader


Create a virtual environment and activate it:

python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/Mac


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
S3_BUCKET=your_bucket_name


Run the Flask app:

python app.py


Open in your browser:

http://127.0.0.1:5000
