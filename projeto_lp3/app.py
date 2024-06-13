from flask import Flask
from validate_docbr import CPF, CNPJ


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

# página /serviços retornar "Nossos Serviços"
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"
# gerar CPF
@app.route("/gerar-cpf")
def gerar_cpf():
    return CPF().generate(True)

@app.route("/gerar-cnpj")
def gerar_cnpj():
    return CNPJ().generate(True)

app.run()