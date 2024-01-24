import os
from flask import Flask, render_template, request, jsonify, send_file
from flask_dropzone import Dropzone

import conversions
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH = os.path.join(basedir,'uploads'),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*60*1000
)

dropzone = Dropzone(app)
@app.route('/',methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')

@app.route('/png_jpg', methods=['POST'])
def png_jpg():
    
    directory = os.fsencode(os.getcwd() + '/uploads')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename == '.DS_Store':
            continue
        conversions.pngTojpg('uploads/' + filename)
    
    orig, _ = os.path.splitext(filename)
    return send_file('uploads/' + orig + '.jpg', as_attachment=True)

    #return '', 204

@app.route('/jpg_png', methods=['POST'])
def jpg_png():

    directory = os.fsencode(os.getcwd() + '/uploads')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename == '.DS_Store':
            continue
        conversions.jpgTopng('uploads/' + filename)
    
    orig, _ = os.path.splitext(filename)
    return send_file('uploads/' + orig + '.png', as_attachment=True)
    #return '', 204
    

if __name__ == '__main__':
    app.run(debug=True)