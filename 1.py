from flask import Flask, url_for, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
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
                          <body style="background: url(/static/nubex.jpg)">
                          <center>
                          <div style='margin-top:35%;'>
                          
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
                          <body style="background: url(/static/nubex.jpg)">
                          <center>
                          <div style='margin-top:35%;'>
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
                          <body style="background: url(/static/nubex.jpg)">
                          <center>
                          <div style='margin-top:35%;'>
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
        about = request.form.get('about')
        anim = request.form.get('anim')
        result = cur.execute("""SELECT login FROM users WHERE login = ?""",(log, )).fetchone()
        if result != None:
            return "Такой пользователь уже есть"
        elif pas == '' or pas == ' ' or log == '' or log == ' ':
            return "not verno"
        else:
            res = cur.execute("""INSERT INTO users(login, password, name, about, anim, kind) VALUES(?, ?, ?, ?, ?, 'cat')""",(log, pas, name, about, anim)).fetchall()
            con.commit()
            con.close()
            return redirect('/vhod')


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
        about = request.form.get('about')
        anim = request.form.get('anim')
        result = cur.execute("""SELECT login FROM users WHERE login = ?""",(log, )).fetchone()
        if result != None:
            return "Такой пользователь уже есть"
        elif pas == '' or pas == ' ' or log == '' or log == ' ':
            return "not verno"
        else:
            res = cur.execute("""INSERT INTO users(login, password, name, about, anim, kind) VALUES(?, ?, ?, ?, ?, 'dog')""",(log, pas, name, about, anim)).fetchall()
            con.commit()
            con.close()
            return "Форма отправлена"

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
            return "not verno"
        else:
            b = result[0]
            if b == pas:
                return "OK"
            else:
                return "not verno"
        
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
