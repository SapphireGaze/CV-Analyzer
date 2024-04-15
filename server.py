import os
from werkzeug.utils import secure_filename
from flask import Flask, Response, request, jsonify

from lib import analyze_cv

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(file_name: str) -> bool:
    return "." in file_name and file_name.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def create_upload_dir() -> None:
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route("/analyze_cv", methods=["POST"])
def analyze_cv_endpoint() -> Response:
    if "cv_file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["cv_file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        file_name = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_name)
        file.save(file_path)

        position = request.form.get("position")

        if not position:
            return jsonify({"error": "position is a required field"}), 400

        analysis_result = analyze_cv(file_path, position)
        os.remove(file_path)

        return jsonify(analysis_result)

    return jsonify({"error": "Invalid file format"}), 400

if __name__ == "__main__":
    create_upload_dir()
    app.run()
