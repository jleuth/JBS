import logging
import os
import subprocess
import time
from flask import Flask, request, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/')
def index():
    password = os.getenv('PASSWORD')
    return render_template('index.html', password=password)

@app.route('/build', methods=['POST'])
def build():
    dev_name = request.form['devName']
    folder = request.files.getlist('folderUpload')
    artifact_extension = request.form['artifactExtension']
    
    build_dir = os.path.join('buildfiles')
    os.makedirs(build_dir, exist_ok=True)
    
    for file in folder:
        filename = file.filename
        filepath = os.path.join(build_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)  # Create folders if needed
        file.save(filepath)
    
    print(f"Developer Name: {dev_name}")
    
    # Run the shell script with the developer name as an argument and wait for it to finish
    subprocess.run(['./build_script.sh'], check=True)

    # Remove build files
    subprocess.run(['rm', '-rf', build_dir])

    # Find the newest build artifact in the outputs directory
    outputs_dir = os.path.join('outputs')
    os.makedirs(outputs_dir, exist_ok=True)
    
    # Delete build artifacts older than 1 day
    for f in os.listdir(outputs_dir):
        file_path = os.path.join(outputs_dir, f)
        if f.endswith(artifact_extension) and os.path.isfile(file_path):
            if os.path.getctime(file_path) < (time.time() - 86400):
                os.remove(file_path)
    
    newest_artifact = max([f for f in os.listdir(outputs_dir) if f.endswith(artifact_extension)], key=lambda x: os.path.getctime(os.path.join(outputs_dir, x)))
    
    return send_from_directory(outputs_dir, newest_artifact, as_attachment=True)

app.run(host='0.0.0.0', port=5000)