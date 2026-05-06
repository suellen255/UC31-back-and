from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome = "Alice"
    return render_template('index.html', title='Página Inicial', nome=nome)

@app.route('/usuario')
def usuario():
    usuario = {'Nome:', 'Suellen', 'Email:', 'suellenlourenco@gmail.com'}
    return render_template('index.html', title='Página Inicial', usuario=usuario)

@app.route('/dados', defauls={"nome":"usuario comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}!'

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no semestre' + str(x)
    
@app.route('/somar', defaults={"n1": "0", "n2":"0"})
@app.route('/somar/<int:n1>/<int:n2>')    
def somar(n1,n2):
    resultado = n1 + n2
    return render_template('somar.html', n1=n1, n2=n2, resultado=resultado)

# 1
@app.route('/dados', defaults={"nome": "usuario comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return render_template('saudacao.html', nome=nome)

#
#  2
@app.route('/calculo/<int:n1>/<int:n2>')
def somar(n1, n2):
    resultado = n1 + n2
    return render_template('soma.html', resultado=resultado, n1=n1, n2=n2)

# 3
@app.route('/idade/<nome>/<int:idade> ')
def verificar_idade(nome, idade):
    if idade >= 18:
        mensagem = f"{nome} é maior de idade"
    else:
        mensagem = f"{nome} é menor de idade"
    
    return render_template('idade.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run()

    
#   4
@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return render_template('produto.html', nome=nome, preco=preco)
