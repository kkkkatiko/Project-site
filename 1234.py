from flask import Flask, url_for, request
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = 'Любителям собак и любителям кошек'
    param['title'] = 'Hi!'
    return render_template('index.html', **param)

@app.route('/zv')
def zv():
    a = random.randint(1, 13)
    if a == 1:
        return f'''<img src="{url_for('static', filename='img/10.jpg')}">'''
    elif a == 2:
        return f'''<img src="{url_for('static', filename='img/11.jpg')}">'''
    elif a == 3:
        return f'''<img src="{url_for('static', filename='img/22.png')}">'''
    elif a == 4:
        return f'''<img src="{url_for('static', filename='img/33.png')}">'''
    elif a == 5:
        return f'''<img src="{url_for('static', filename='img/44.png')}">'''
    elif a == 6:
        return f'''<img src="{url_for('static', filename='img/55.png')}">'''
    elif a == 7:
        return f'''<img src="{url_for('static', filename='img/66.png')}">'''
    elif a == 8:
        return f'''<img src="{url_for('static', filename='img/77.png')}">'''
    elif a == 9:
        return f'''<img src="{url_for('static', filename='img/88.jpg')}">'''
    elif a == 10:
        return f'''<img src="{url_for('static', filename='img/99.jpg')}">'''
    elif a == 11:
        return f'''<img src="{url_for('static', filename='img/12.jpg')}">'''
    elif a == 12:
        return f'''<img src="{url_for('static', filename='img/13.jpg')}">'''
    elif a == 13:
        return f'''<img src="{url_for('static', filename='img/14.png')}">'''
    print(a)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
