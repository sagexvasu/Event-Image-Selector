from flask import Flask, request, redirect, url_for, render_template
import os
import subprocess
import threading

app = Flask(__name__)

app_process = None  
preprocess_process = None  

def run_app():
    global app_process
    app_process = subprocess.Popen(['python', 'app.py'])
    app_process.wait()  
    app_process = None  

def run_preprocess():
    global preprocess_process
    preprocess_process = subprocess.Popen(['python', 'preprocess_and_encode.py'])
    preprocess_process.wait()  
    preprocess_process = None

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('file')
    for file in files:
        if file:
            file.save(os.path.join('AllImages', file.filename))
    return redirect(url_for('index'))

@app.route('/toggle_app', methods=['POST'])
def toggle_app():
    global app_process
    if app_process is None:
        threading.Thread(target=run_app).start()
    else:
        app_process.terminate()
        app_process.wait()
        app_process = None
    return redirect(url_for('index'))

@app.route('/run_preprocess', methods=['POST'])
def run_preprocess_route():
    global preprocess_process
    if preprocess_process is None:
        threading.Thread(target=run_preprocess).start()
    else:
        preprocess_process.terminate()
        preprocess_process.wait()
        preprocess_process = None
    return redirect(url_for('index'))

@app.route('/')
def index():
    app_button_text = "Terminate app.py" if app_process else "Run app.py"
    preprocess_button_text = "Stop preprocess_and_encode.py" if preprocess_process else "Run preprocess_and_encode.py"
    return render_template('admin_index.html', app_button_text=app_button_text, preprocess_button_text=preprocess_button_text)

if __name__ == '__main__':
    app.run(port=8000)
