from flask import Flask, render_template
from validate_docbr import CPF, CNPJ


app = Flask(__name__)

# rota = função

# / - home page
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def xxxxx():
    return render_template("contato.html")

# /produtos - págian e produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome" : "Tigrinho", "descricao" : "Multiplica seu dinheiro", "imagem" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjByqUxAwkmJj3JFDKw2-YgNmg200MKGNl6A&s"},
        {"nome" : "Agiotagem", "descricao" : "Te da dinheiro para jogar no tigrinho", "imagem" : "https://ambitojuridico.com.br/wp-content/uploads/2023/03/Captura-de-tela_20230303_152020.webp"},
        {"nome" : "RDR2", "descricao" : "Te da uma nova experiencia de vida", "imagem" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYhTdrfXk0LVl96VEdgauqXRMzn6cvUJ6nzA&s"},        
    ]


    return render_template("produtos.html", produtos=lista_produtos) 

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