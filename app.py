# simple flask app
from flask import Flask
import json

app = Flask(__name__)

images = json.load(open('images.json'))

dirs = []
for image in images:    
    if image['path'] not in dirs:
        dirs.append(image['path'])

@app.route('/')
def hello_world():
    
    for dir in dirs:
        print('<a href="/{dir}">{dir}</a>').format(dir=dir)

if __name__ == '__main__':
    app.run()


