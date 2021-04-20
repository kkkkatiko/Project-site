from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def form_sample():
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
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h4 align="center">на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <br>
                                    <input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <br>
                                    <label> Какие у вас профессии?</label>
                                    
                                    <label class="container">пилот
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">строитель
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">экзобиолог
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">врач
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">климатолог
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">метеоролог
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <label class="container">киберинженер
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    </br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                    </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        </br>
                                    </div>
                                    <label class="container">Готовы остаться на Марсе?
                                            <input type="checkbox">
                                            <span class="checkmark"></span>
                                    </label>
                                    <br></br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
