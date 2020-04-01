from flask import Flask, render_template

app = Flask(__name__)


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    if gender == 'female':
        if age < 21:
            return render_template('cabin_color.html', color='ffe5b4', photo='/static/img/baby.jpg')
        return render_template('cabin_color.html', color='red', photo='/static/img/adult.png')
    elif gender == 'male':
        if age < 21:
            return render_template('cabin_color.html', color='87ceeb', photo='/static/img/baby.jpg')
        return render_template('cabin_color.html', color='blue', photo='/static/img/adult.png')
    else:
        return '''<p>Ошибка!</p>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')