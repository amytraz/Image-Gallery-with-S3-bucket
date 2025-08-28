from flask import Flask, render_template, request, redirect, url_for
import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# --------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------
load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET", "your-s3-bucket-name")
S3_REGION = os.getenv("AWS_REGION", "your-region")  # e.g., "ap-south-1")

app = Flask(__name__)

# --------------------
# CONFIGURATION
# --------------------
USE_S3 = False   # ⬅️ Change to True when deploying with AWS
UPLOAD_FOLDER = "static/uploads"  # for local mode
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# AWS S3 client (only used if USE_S3 = True)
s3_client = boto3.client("s3", region_name=S3_REGION)


# --------------------
# ROUTES
# --------------------
@app.route("/")
def index():
    if USE_S3:
        # List images from S3
        try:
            objects = s3_client.list_objects_v2(Bucket=S3_BUCKET)
            if "Contents" in objects:
                images = [
                    f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{obj['Key']}"
                    for obj in objects["Contents"]
                ]
            else:
                images = []
        except (NoCredentialsError, ClientError) as e:
            print("Error accessing S3:", e)
            images = []
    else:
        # List images from local folder
        images = []
        if os.path.exists(app.config["UPLOAD_FOLDER"]):
            images = [
                f"{app.config['UPLOAD_FOLDER']}/{img}"
                for img in os.listdir(app.config["UPLOAD_FOLDER"])
                if img.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
            ]

    return render_template("index.html", images=images)


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]
    if file.filename == "":
        return "No selected file"

    if USE_S3:
        # Upload to AWS S3
        try:
            s3_client.upload_fileobj(file, S3_BUCKET, file.filename)
            print("Uploaded to S3:", file.filename)
        except (NoCredentialsError, ClientError) as e:
            print("Error uploading to S3:", e)
            return "S3 Upload Failed"
    else:
        # Save locally
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        print("Saved locally:", filepath)

    return redirect(url_for("index"))


# --------------------
# MAIN
# --------------------
if __name__ == "__main__":
    app.run(debug=True)
