import json
import requests
from flask import Flask, render_template, request
import os
from gtts import gTTS
from playsound import playsound

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
NO_VALID_IMAGE = 'No se ha proporcionado ninguna imagen válida'
IS_DOCKER_ENV = os.environ.get('IS_DOCKER', 'False') == 'True'
FASTAPI_URL = 'http://nginx/upload'

if IS_DOCKER_ENV:
    UPLOAD_FOLDER = '/usr/src/app/images'
else:
    UPLOAD_FOLDER = 'images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method != 'POST' or not request.files:
        return render_template('home.html')

    f = request.files['image']

    try:
        # Do POST to FastAPI
        response = requests.post(FASTAPI_URL, files={'image': f})
        data = json.loads(response.content)

        if response.status_code != 200 or data['status'] != 'ok':
            return render_template('results.html', text='Ha ocurrido un error')

        if not IS_DOCKER_ENV:
            audio_path = app.config['UPLOAD_FOLDER'] + '/speech.mp3'
            myobj = gTTS(text=text, lang='es', slow=False)
            myobj.save(audio_path)
            playsound(audio_path)

        return render_template('results.html', text=data['text'])
    except Exception as e:
        return render_template('results.html', text=e)


if __name__ == '__main__':
    app.run(debug=True)
