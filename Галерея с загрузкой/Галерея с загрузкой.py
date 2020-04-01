from flask import Flask, request, render_template
import os


app = Flask(__name__)
pic = ['/static/img/mars1.jpg', '/static/img/mars2.jpg', '/static/img/mars3.jpg']


@app.route('/galery', methods=['POST', 'GET'])
def load_photo():
    photo = f'/static/img/mars{len(pic) + 1}.jpg'
    if request.method == 'GET':
        return render_template('galery.html', featuredStory=pic)
    elif request.method == 'POST':
        f = request.files['file']
        with open(photo.lstrip('/'), "wb") as file:
            file.write(f.read())
        pic.append(photo)
        return render_template('galery.html', featuredStory=pic)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')