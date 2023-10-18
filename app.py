# Main Math py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    return render_template("soma.html")

@app.route("/resultado")
def kkkkkk():
    numero1 = int(request.args.get('num1'))
    numero2 = int(request.args.get('num2'))
    resultado = numero1 + numero2
    return str(resultado)


@app.route("/resultado2")
def aaaaaa():
    numero1 = int(request.args.get('num1'))
    numero2 = int(request.args.get('num2'))
    resultado = numero1 + numero2
    return render_template("re2.html", valor=resultado)