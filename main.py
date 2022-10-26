import operacoes
from flask import Flask, render_template, request, flash, url_for
import this

this.dados = 0

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html', titulo='Página Principal')


@pessoa.route('/login.html', methods=['GET', 'POST'])
def pag_login():
    return render_template('/login.html', titulo='Página Principal')

@pessoa.route('/cadastroFunc.html', methods=['GET', 'POST'])
def pag_cadastro():
    return render_template('/cadastroFunc.html', titulo='Página Principal')

@pessoa.route('/atualizarsenha.html', methods=['GET', 'POST'])
def pag_atualizarsenha():
    return render_template('/atualizarsenha.html', titulo='Página Principal')


@pessoa.route('/inicialGerente.html', methods=['GET', 'POST'])
def pag_inicialGerente():
    return render_template('/inicialGerente.html', titulo='Página Principal')




#cadastrar Funcionário
@pessoa.route('/cadastrarFunc.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.cpf = request.form['coletarCpf']
        this.nome = request.form['coletarNome']
        this.celular = request.form['coletarCelular']
        this.email = request.form['coletarEmail']
        this.senha = request.form['coletarSenha']

        if operacoes.cpf_validate(this.cpf) == True:
            this.dados = operacoes.inserir(this.cpf, this.nome, this.celular, this.email, this.senha)
            return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)
        else:
            this.dados = "ERRO, favor informe um CPF válido!"
    return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)

#login funcionário
@pessoa.route('/cadastrarFunc.html', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        this.cpf = request.form['coletarCpf']
        this.nome = request.form['coletarNome']
        this.celular = request.form['coletarCelular']
        this.email = request.form['coletarEmail']
        this.senha = request.form['coletarSenha']

        if operacoes.cpf_validate(this.cpf) == True:
            this.dados = operacoes.inserir(this.cpf, this.nome, this.celular, this.email, this.senha)
            return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)
        else:
            this.dados = "ERRO, favor informe um CPF válido!"
    return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)


@pessoa.route('/atualizarFunc.html', methods=['GET','POST'])
def atualizarDados():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dados = operacoes.atualizar(this.cpf, this.campo, this.nDado)
    return render_template('/atualizarFunc.html', titulo='Atualizar', resultado=this.dados)


@pessoa.route('/consultarFunc.html', methods=['GET','POST'])
def consultarIndividual():
    if request.method == 'POST':
        this.cpfGerente = request.form['coletarCPF']
        this.mensagem = operacoes.consultar(this.cpfGerente)
    else:
        this.mensagem = ""
    return render_template('/consultarFunc.html', titulo='Consultar por cpf', dados=this.mensagem)

@pessoa.route('/excluirFunc.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method == 'POST':
        this.cpfGerente = request.form['cpfGerente']
        this.dados = operacoes.deletar(this.cpfGerente)
    return render_template('/excluirFunc.html', titulo='Excluir', resultado=this.dados)


@pessoa.route('/inicialCliente.html', methods=['GET','POST'])
def inicialCliente():
    return render_template('/inicialCliente.html', titulo='Página Inicial Cliente', resultado=this.dados)

if __name__ == "__main__":
    pessoa.run(debug=True, port=5003)