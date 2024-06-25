from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ


app = Flask(__name__)


lista_produtos = [
        {"nome" : "Tigrinho", "descricao" : "Multiplica seu dinheiro", "imagem" : "https://veja.abril.com.br/wp-content/uploads/2024/06/tigrinho.jpg?crop=1&resize=1212,909"},
        {"nome" : "Elden Ring", "descricao" : "Absolute Game, mais de 300 de jogo ", "imagem" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU_cspEzfgMdenwt0VS7QHBJCOdWaVkrXyvA&s"},
        {"nome" : "RDR2", "descricao" : "Te da uma nova experiencia de vida", "imagem" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYhTdrfXk0LVl96VEdgauqXRMzn6cvUJ6nzA&s"},
        {"nome" : "Stardew valley", "descricao" : "joguinho para apaziguar a vida", "imagem" : "https://4.bp.blogspot.com/-UkrL69U4Pvk/Vw6F9_oI12I/AAAAAAAAAtg/oRTty0rp4Igz2lTzwplBAjQgR_UKoSA8wCK4B/s1600/Stardew-Valley.jpg"},       
    ]
# rota = função

# / - home page
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def xxxxx():
    return render_template("contato.html")

@app.route("/termo")
def termo():
    return render_template("termo.html")

@app.route("/politicas")
def politicas():
    return render_template("politicas.html")

@app.route("/comousar")
def comousar():
    return render_template("comousar.html")

# /produtos - págian e produtos
@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos) 

# página /serviços retornar "Nossos Serviços"
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"

# gerar CPF
@app.route("/gerar-cpf")
def gerar_cpf():
    cpf = CPF()

    return render_template("gerar-cpf.html", cpfs = cpf.generate(True))

@app.route("/gerar-cnpj")
def gerar_cnpj():
    cnpj = CNPJ()

    return render_template("gerar-cnpj.html", cpfs = cnpj.generate(True))

#GET

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

#POST 
@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    imagem = request.form["imagem"]
    produto = {"nome": nome, "descricao": descricao, "imagem": imagem}
    lista_produtos.append(produto)
    return render_template("produtos.html", produtos = lista_produtos)

app.run()



