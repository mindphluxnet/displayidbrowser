from flask import Flask, render_template, redirect
import json
import urllib.request

app = Flask(__name__)

images = None

def load_data():
    with urllib.request.urlopen("https://displayidbrowser.mindphlux.net/images.json") as url:
        return json.load(url)

def check_maintenance():
    try:
        with urllib.request.urlopen("https://displayidbrowser.mindphlux.net/maintenance") as url:
            return True
    except:
        return False

@app.route('/')
def show_dirs():
    if not check_maintenance():
        dirs = []

        for image in images:
            if image['path'] not in dirs:
                dirs.append(image['path'])

        return render_template('index.html', dirs=dirs)
    else:
        return render_template('maintenance.html')

@app.route("/<string:dir>")
def show_dir(dir):
    if not check_maintenance():
        images_in_dir = []
        dirs = []

        for image in images:
            if image['path'] not in dirs:
                dirs.append(image['path'])
            if image['path'] == dir:
                images_in_dir.append(image)

        return render_template('dir.html', images=images_in_dir, dir=dir, dirs=dirs)
    else:
        return render_template('maintenance.html')

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
