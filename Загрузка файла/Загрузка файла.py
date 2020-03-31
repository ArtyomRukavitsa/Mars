from flask import Flask, request, render_template
import os


app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    photo = "static/img/photo.png"
    if request.method == 'GET':
        return render_template('test.html', os=os, photo=photo)
    elif request.method == 'POST':
        f = request.files['file']
        with open(photo, "wb") as file:
            file.write(f.read())
        return render_template('test.html', os=os, photo=photo)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')