# simple flask app
from flask import Flask, render_template
import json

app = Flask(__name__)

images = json.load(open('images.json'))


@app.route('/')
def show_dirs():
    dirs = []

    for image in images:
        if image['path'] not in dirs:
            dirs.append(image['path'])    

    return render_template('index.html', dirs=dirs)

@app.route("/<string:dir>")
def show_dir(dir):
    images_in_dir = []
    dirs = []

    for image in images:
        if image['path'] not in dirs:
            dirs.append(image['path'])  
        if image['path'] == dir:
            images_in_dir.append(image)

    return render_template('dir.html', images=images_in_dir, dir=dir, dirs=dirs)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000)    
