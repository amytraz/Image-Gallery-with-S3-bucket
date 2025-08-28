

````markdown
# 📸 Visual Archive  

**Visual Archive** is a simple and elegant Flask-based web application that allows users to upload images securely to **AWS S3** and view them directly on the website.  
This project demonstrates how to integrate **Flask** with **Amazon S3**, manage credentials securely with `.env`, and build a clean, responsive frontend.  

---

## 🚀 Features  
- 📤 Upload images directly from your browser to **AWS S3**  
- 🔒 Secure credential management using `.env`  
- 🎨 Minimal, responsive UI with modern CSS  
- ⚡ Flask backend powered by **boto3** for AWS integration  
- 🌍 View uploaded images instantly on the website  
- 🛠️ Easy to set up and deploy  

---

## 🛠️ Tech Stack  
- **Backend:** Flask (Python)  
- **Storage:** AWS S3  
- **Frontend:** HTML, CSS (custom, responsive)  
- **Environment Management:** python-dotenv  

---

## ⚙️ Setup Instructions  

### 1. Clone the repository  
```bash
git clone https://github.com/amytraz/Image-Gallery-with-S3-bucket.git
cd visual-archive
````

### 2. Create a virtual environment and activate it

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root with the following values:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
S3_BUCKET=your_bucket_name
```

⚠️ **Note:** Never commit your AWS credentials to GitHub. Always use `.env` for security.

### 5. Run the Flask app

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
visual-archive/
│── app.py              # Flask application
│── templates/index.html         # HTML templates
│── requirements.txt    # Python dependencies
│── .env                # Environment variables (ignored in .gitignore)
│── README.md           # Project documentation
```

---


### ✨ Author

**Visual Archive** was built with ❤️ using Flask and AWS.

```

Would you like me to also **add example screenshots placeholders with HTML templates** (like a preview grid for uploaded images), so your README looks even more professional?
```
