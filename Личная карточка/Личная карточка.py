from flask import Flask, render_template
import json
from random import randint

app = Flask(__name__)


@app.route('/member')
def member():
    with open('templates/info.json', 'r', encoding='utf8') as file:
        data = json.loads(file.read())['info'][randint(0, 3)]
    return render_template('card.html', name=data['name'],
                           photo=data['photo'], profession=data['profession'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')