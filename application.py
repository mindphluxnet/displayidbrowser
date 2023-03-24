from flask import Flask, render_template, redirect, url_for
import json
import urllib.request

app = Flask(__name__)

images = None

def load_data():
    with urllib.request.urlopen("https://displayidbrowser.mindphlux.net/images.json") as url:
        return json.load(url)

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

@app.route("/api/usedby/<string:displayid>")
def get_used_by(displayid):

    for image in images:
        if image['id'] == displayid:
            return json.dumps(image['used_by'])

@app.route("/update")
def update():
    images = load_data()
    return redirect("http://www.displayidbrowser.com")

if __name__ == '__main__':
    images = load_data()
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000)
