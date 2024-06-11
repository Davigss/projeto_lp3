from flask import Flask

app = Flask(__name__)

# rota = função

# / - home page
@app.route("/")
def home():
    return "<h1> Página principal</h1>"

# /contato - página de contato
@app.route("/contato")
def xxxxx():
    return "<h1>Contato</h1>"

# /produtos - págian e produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>" 