from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np
from PIL import Image
from collections import Counter

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = "static/images/"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def new_get_colors(pic, num):
    hexalist = []
    img = Image.open(pic)
    img_array = np.array(img)
    for color in img_array:
        rgb = tuple(color[1])
        hexacode = '{:02x}{:02x}{:02x}'.format(*rgb)
        if hexacode not in hexalist:
            hexalist.append(hexacode)
    length = len(hexalist)
    if num <= 0 or num > length:
        return hexalist
    step = int(length / num)
    return hexalist[:length:step]


@app.route("/")
def home():
    home_list = ['dde4e0', 'aac9de', '625217', '24291c', '8db9da', '5f6159', '74aed8', '976b0e', 'd8a10e', '4e360e']
    return render_template("index.html", home_list=home_list)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(app.config['UPLOAD_FOLDER'] + secure_filename(f.filename))
        path = app.config['UPLOAD_FOLDER'] + secure_filename(f.filename)
        number = request.values['number']
        colors = new_get_colors(path, int(number))
        return render_template("index.html", uploaded_image=f.filename, list=colors)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='images/' + filename), code=301)
    # return send_from_directory(app.config["IMAGE_UPLOADS"], filename)


if __name__ == "__main__":
    app.run(debug=True)
