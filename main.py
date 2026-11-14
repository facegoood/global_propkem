from flask import Flask, render_template  # импортируем Flask и функцию показа страниц

app = Flask(__name__)  # создаём приложение


@app.route("/")  # адрес главной страницы
def index():
    return render_template("index.html")  # показать index.html из папки templates


@app.route("/prichiny")  # адрес страницы про причины
def prichiny():
    return render_template("prichiny.html")


@app.route("/posledstviya")  # адрес страницы про последствия
def posledstviya():
    return render_template("posledstviya.html")


@app.route("/chto-delat")  # адрес страницы «что делать»
def cto_delat():
    return render_template("chto_delat.html")


if __name__ == "__main__":  # запуск сервера, когда файл запускают напрямую
    app.run(debug=True)  # debug=True — автоперезагрузка и понятные ошибки
