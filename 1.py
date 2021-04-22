from flask import Flask, url_for, request, redirect
from flask import render_template
import random
from flask_ngrok import run_with_ngrok
import requests
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index3():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Здравствуй!</title>
                          </head>
                          <body style="background: url(/static/nubex.jpg); -webkit-background-size: 100%; -o-background-size: 100%; background-size: 100%;">
                          <center>
                          <div style='margin-top:25%; '>
                          
                        <a href="/dg" type="submit" class="btn btn-primary">
                                    Собаки!
                                    </a>
                                  <a>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</a>
                            <a href="/ct" type="submit" class="btn btn-primary" >
                                    Кошки!
                                    </a>
                            </div>
                        </center>
                          </body>
                        </html>'''

@app.route('/dg', methods=['POST', 'GET'])
def index1():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Здравствуй!</title>
                          </head>
<body style="background: url(/static/nubex.jpg); -webkit-background-size: 100%; -o-background-size: 100%; background-size: 100%;">                          <center>
                          <div style='margin-top:30%;'>
                          <a href="/vhod" type="submit" class="btn btn-primary">
                                    Войти!
                                    </a>
                        <a>&nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</a>
                        <a href="/dogs" type="submit" class="btn btn-primary">
                                    Зарегистрироваться!
                                    </a>
                          </div>
                        </center>
                          </body>
                        </html>'''

@app.route('/ct', methods=['POST', 'GET'])
def index2():
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Здравствуй!</title>
                          </head>
<body style="background: url(/static/nubex.jpg); -webkit-background-size: 100%; -o-background-size: 100%; background-size: 100%;">                          <center>
                          <div style='margin-top:30%;'>
                          <a href="/vhod" type="submit" class="btn btn-primary">
                                    Войти!
                                    </a>
                        <a>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
                                    &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</a>
                        <a href="/cats" type="submit" class="btn btn-primary">
                                    Зарегистрироваться!
                                    </a>
                          </div>
                        </center>
                          </body>
                        </html>'''

@app.route('/cats', methods=['POST', 'GET'])
def cats():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Здравствуй, любитель кошек!</title>
                          </head>
                          <body style="background: #E6E6FA">
                            <h1 align="center" style="color:#4B0082">Анкета любителя кошек</h1>
                            <div>
                                <form class="login_form" method="post" style="color:#4B0082">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя и фамилию" name="name" >
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                                    <br>
                                    <input type="login" class="form-control" id="login" placeholder="Введите логин" name="login">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                     <br>
                                     <div class="form-group">
                                        <label for="form-check">Есть ли у вас животное?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="anim" id="yes" value="yes" checked>
                                          <label class="form-check-label" for="yes">
                                            Да
                                          </label>
                                        </div>
                                    </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="anim" id="no" value="no">
                                          <label class="form-check-label" for="no">
                                            Нет
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="about">Расскажите немного о совей кошке или какую кошку вы бы хотели завести.</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br></br>
                                    <button type="submit" class="btn btn-primary">Зарегистрироваться!</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        con = sqlite3.connect("database.sqlite")
        cur = con.cursor()
        name = request.form.get('name')
        email = request.form.get('email')
        file = request.form.get('file')
        log = request.form.get('login')
        pas = request.form.get('password')
        if len(pas)<5:
            return redirect('/corot')
        about = request.form.get('about')
        anim = request.form.get('anim')
        result = cur.execute("""SELECT login FROM users WHERE login = ?""",(log, )).fetchone()
        if result != None:
            return redirect('/est')
        elif pas == '' or pas == ' ' or log == '' or log == ' ':
            return redirect('/not')
        else:
            res = cur.execute("""INSERT INTO users(login, password, name, about, anim, kind) VALUES(?, ?, ?, ?, ?, 'cat')""",(log, pas, name, about, anim)).fetchall()
            con.commit()
            con.close()
            return redirect('/not')


@app.route('/dogs', methods=['POST', 'GET'])
def dogs():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Здравствуй, любитель собак!</title>
                          </head>
                          <body style="background: #E6E6FA">
                            <h1 align="center" style="color:#4B0082">Анкета любителя собак</h1>
                            <div>
                                <form class="login_form" method="post" style="color:#4B0082">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя и фамилию" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">

                                    <br>
                                    <input type="login" class="form-control" id="login" placeholder="Введите логин" name="login">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                     <br>
                                     <div class="form-group">
                                        <label for="form-check">Есть ли у вас животное?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="anim" id="yes" value="yes" checked>
                                          <label class="form-check-label" for="yes">
                                            Да
                                          </label>
                                        </div>
                                    </div>
                                        <div class="form-check" style="color:#4B0082">
                                          <input class="form-check-input" type="radio" name="anim" id="no" value="no">
                                          <label class="form-check-label" for="no">
                                            Нет
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="about">Расскажите немного о совей собаке или какую собаку вы бы хотели завести.</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br></br>
                                    <div ng-controller="exampleCtrl as ctrl">
                                     <button type="submit" class="btn btn-primary">Зарегистрироваться!</button>
                                     </div>
                                    
                                    
                                    </form>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        con = sqlite3.connect("database.sqlite")
        cur = con.cursor()
        name = request.form.get('name')
        email = request.form.get('email')
        log = request.form.get('login')
        pas = request.form.get('password')
        if len(pas)<5:
            return redirect('/corot')
        about = request.form.get('about')
        anim = request.form.get('anim')
        result = cur.execute("""SELECT login FROM users WHERE login = ?""",(log, )).fetchone()
        if result != None:
            return redirect('/est')
        elif pas == '' or pas == ' ' or log == '' or log == ' ':
            return redirect('/not')
        else:
            res = cur.execute("""INSERT INTO users(login, password, name, about, anim, kind) VALUES(?, ?, ?, ?, ?, 'dog')""",(log, pas, name, about, anim)).fetchall()
            con.commit()
            con.close()
            return redirect('/vhod')

@app.route('/vhod', methods=['POST', 'GET'])
def vhod():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Здравствуй!</title>
                          </head>
                          <body>
                            <h1 align="center" style="color:#4B0082">Вход</h1>
                            <div>
                                <form class="login_form" method="post" >
                                    <input type="login" class="form-control" id="login" placeholder="Введите логин" name="login">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <br>
                                    <button type="submit" class="btn btn-primary">Войти!</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        con = sqlite3.connect("database.sqlite")
        cur = con.cursor()
        log = request.form.get('login')
        pas = request.form.get('password')
        result = cur.execute("""SELECT password FROM users WHERE login = ?""",(log, )).fetchone()
        if result == None:
            return redirect('/not')
        else:
            b = result[0]
            if b == pas:
                return redirect('/index')
            else:
                return redirect('/not')

@app.route('/not', methods=['GET'])
def ne():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Не верно!</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post" >
                                <h1 align="center" style="color:#4B0082">Не верно!</h1>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/corot', methods=['GET'])
def corot():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Такой пользователь уже есть</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post" >
                                <h1 align="center" style="color:#4B0082">Слишком короткий пароль!</h1>
                                <h1 align="center" style="color:#4B0082">Пароль должен быть длиннее 5 символов</h1>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/est', methods=['GET'])
def est():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Такой пользователь уже есть</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post" >
                                <h1 align="center" style="color:#4B0082">Такой пользователь уже есть</h1>
                                </form>
                            </div>
                          </body>
                        </html>'''

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

@app.route('/index')
def index():
    param = {}
    return render_template('index.html', **param)

@app.route('/testdog')
def testdog():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Много ли ты знаешь о собаках?</title>
                  </head>
                  <body>
                    <div id="vopr">
                <h3>Кого называют «собакой-убийцей»?</h3>
                    <input name=v1 onclick="vopr1true()" type="radio">Питбуля
                    <br>
                    <input name=v1 type="radio">Добермана
                    <br>
                    <input name=v1 type="radio">Джека-рассела
                    <br>
                    <input name=v1 type="radio">Хаски
                <h3>Собаки какой пароды-любимчики королевы Великобритани?</h3>
                    <input name=v2 type="radio">Шпицы
                    <br>
                    <input name=v2 onclick="vopr2true()" type="radio" >Корги
                    <br>
                    <input name=v2 type="radio">Лабрадоры
                    <br>
                    <input name=v2 type="radio">Борзые
                <h3>Какая порода собак считается самой умной?</h3>
                    <input name=v3 onclick="vopr3true()" type="radio">Колли
                    <br>
                    <input name=v3 type="radio">Ротвейлер
                    <br>
                    <input name=v3 type="radio">Той-спаниель
                    <br>
                    <input name=v3 type="radio">Пудель
                <h3>Собака — проводник в загробный мир это?</h3>
                    <input name=v4 type="radio">Зенненхунд
                    <br>
                    <input name=v4 type="radio">Такса
                    <br>
                    <input name=v4 type="radio">Малинуа
                    <br>
                    <input name=v4 onclick="vopr4true()" type="radio">Ксолоитцкуинтли
                <h3>У какой породы собак сине-чёрный язык?</h3>
                    <input name=v5 type="radio">Маламута
                    <br>
                    <input name=v5 type="radio">Акиты-ину
                    <br>
                    <input name=v5 onclick="vopr5true()" type="radio">Чау-чау
                    <br>
                    <input name=v5 type="radio">Немецкой оффчарки
                    <br>
                    </div>
                    <button onclick="otvety();">Закончить тест</button>
                    <div id="otvety" style="display:none">
                      <div id="1" style="background:#f00">1-неправильно</div>
                      <div id="2" style="background:#f00">2-неправильно</div>
                      <div id="3" style="background:#f00">3-неправильно</div>
                      <div id="4" style="background:#f00">4-неправильно</div>
                      <div id="5" style="background:#f00">5-неправильно</div>
                    </div>
                    <script>
                      function vopr1true() {
                        document.getElementById("1").style.background = "#0f0";
                        document.getElementById("1").innerHTML = "1-правильно";}
 
                      function vopr2true() {
                        document.getElementById("2").style.background = "#0f0";
                        document.getElementById("2").innerHTML = "2-правильно";}
                        
                      function vopr3true() {
                        document.getElementById("3").style.background = "#0f0";
                        document.getElementById("3").innerHTML = "3-правильно";}
                      function vopr4true() {
                        document.getElementById("4").style.background = "#0f0";
                        document.getElementById("4").innerHTML = "4-правильно";}
                      function vopr5true() {
                        document.getElementById("5").style.background = "#0f0";
                        document.getElementById("5").innerHTML = "5-правильно";}
 
                      function otvety() {
                        document.getElementById("otvety").style.display = "block";
                        for (var i = 0; i < document.getElementsByTagName("input").length; i++) {
                          document.getElementsByTagName("input")[i].disabled = true}}
                    </script>
                  </body>
                </html><div id="vopr">'''

@app.route('/testcat')
def testcat():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Много ли ты знаешь о кошках?</title>
                  </head>
                  <body>
                    <div id="vopr">
                <h3>Kаких кошек/котов называют "денежными"?</h3>
                    <input name=v1 onclick="vopr1true()" type="radio">Трёхцветных
                    <br>
                    <input name=v1 type="radio">Белоснежных
                    <br>
                    <input name=v1 type="radio">Чёрных с белыми "носочками"
                    <br>
                    <input name=v1 type="radio">Богатых
                <h3>В честь какого полководца названа порода кошек/котов?</h3>
                    <input name=v2 type="radio">Кутузова
                    <br>
                    <input name=v2 onclick="vopr2true()" type="radio" >Наполеона
                    <br>
                    <input name=v2 type="radio">Ушакова
                    <br>
                    <input name=v2 type="radio">Чингисхана
                <h3>Какие кошки/коты самые большие из всех?</h3>
                    <input name=v3 onclick="vopr3true()" type="radio">Мейн-куны
                    <br>
                    <input name=v3 type="radio">Чаузи
                    <br>
                    <input name=v3 type="radio">Рагамаффины
                    <br>
                    <input name=v3 type="radio">Саванны
                <h3>Самые популярные кошки/коты мира?</h3>
                    <input name=v4 type="radio">Рэгдоллы
                    <br>
                    <input name=v4 type="radio">Мейн-куны
                    <br>
                    <input name=v4 type="radio">Персидские
                    <br>
                    <input name=v4 onclick="vopr4true()" type="radio">Экзотические
                <h3>У какой породы кошек нет шерсти?</h3>
                    <input name=v5 type="radio">Гавана
                    <br>
                    <input name=v5 type="radio">Шотландской
                    <br>
                    <input name=v5 onclick="vopr5true()" type="radio">Сфинксов
                    <br>
                    <input name=v5 type="radio">Бенгальской
                    <br>
                    </div>
                    <button onclick="otvety();">Закончить тест</button>
                    <div id="otvety" style="display:none">
                      <div id="1" style="background:#f00">1-неправильно</div>
                      <div id="2" style="background:#f00">2-неправильно</div>
                      <div id="3" style="background:#f00">3-неправильно</div>
                      <div id="4" style="background:#f00">4-неправильно</div>
                      <div id="5" style="background:#f00">5-неправильно</div>
                    </div>
                    <script>
                      function vopr1true() {
                        document.getElementById("1").style.background = "#0f0";
                        document.getElementById("1").innerHTML = "1-правильно";}
 
                      function vopr2true() {
                        document.getElementById("2").style.background = "#0f0";
                        document.getElementById("2").innerHTML = "2-правильно";}
                        
                      function vopr3true() {
                        document.getElementById("3").style.background = "#0f0";
                        document.getElementById("3").innerHTML = "3-правильно";}
                      function vopr4true() {
                        document.getElementById("4").style.background = "#0f0";
                        document.getElementById("4").innerHTML = "4-правильно";}
                      function vopr5true() {
                        document.getElementById("5").style.background = "#0f0";
                        document.getElementById("5").innerHTML = "5-правильно";}
 
                      function otvety() {
                        document.getElementById("otvety").style.display = "block";
                        for (var i = 0; i < document.getElementsByTagName("input").length; i++) {
                          document.getElementsByTagName("input")[i].disabled = true}}
                    </script>
                  </body>
                </html><div id="vopr">'''

@app.route('/cat')
def cat():
    response = requests.get('https://some-random-api.ml/img/cat')
    json_response = response.json()
    a = json_response.get("link")
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Котейки</title>
                  </head>
                  <body>
                    <img src="{a}">
                  </body>
                </html>"""

@app.route('/dog')
def dog():
    response1 = requests.get('https://some-random-api.ml/img/dog')
    json_response1 = response1.json()
    a1 = json_response1.get("link")
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Собачки</title>
                  </head>
                  <body>
                    <img src="{a1}">
                  </body>
                </html>"""
        
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
