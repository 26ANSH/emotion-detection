from flask import Flask, render_template, request
import os
from detect import capture_image, detect_faces

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    #  If method was post
    if request.method == 'GET':
        return render_template('basic.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    #  If method was post
    if request.method == 'GET':
        return render_template('basic2.html')
    else:
        file = request.files['file']
        name = request.form.get('name')
        path = "static/images/"+file.filename
        file.save(path)
        try:
            emotions = detect_faces(path)
        except Exception:
            emotions = "Error"
    return render_template('result.html', name=name, emotions=emotions)


@app.route('/emotion', methods=['POST'])
def camera():
    name = request.form.get('name')
    path = capture_image(name)
    try:
        emotions = detect_faces(path)
    except Exception:
        emotions = "Error"
    return render_template('result.html', name=name, emotions=emotions)
             

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api_key.json'
    app.run(host='127.0.0.1', port=8080, debug=True)