from flask import Flask, request
#from deep import match
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/search', methods=['POST'])
def search():
    if 'image' not in request.json:
        return 'whoops'
    
    if 'image' in request.json:
        print('here?')
        return request.json['image']

@app.route('/test', methods=['GET'])
def test():
    return 'hello'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)