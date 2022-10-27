import operacoes
from flask import Flask, render_template, request, flash, url_for
import this

this.dados = 0

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html', titulo='Página Principal')

#login gerente
@pessoa.route('/login.html', methods=['GET', 'POST'])
<<<<<<< HEAD
def pag_login():
    return render_template('/login.html', titulo='Página Principal')
    
@pessoa.route('/trocarSenha.html', methods=['GET', 'POST'])
def pag_trocarSenha():
    if request.method == 'POST':
        this.cpf = request.form['campoCPF']
        this.dado  = request.form['novaSenha']
        this.dados = operacoes.trocarSenha(this.cpf, this.dado)
    return render_template('/trocarSenha.html', titulo='Atualizar', resultado=this.dados)
=======
def loginGerente():
    if request.method == 'POST':
        this.emailGerente = request.form['emailGerente']
        this.senhaGerente = request.form['senhaGerente']
        this.msg = operacoes.loginGerente(this.emailGerente, this.senhaGerente)
        if this.msg == "Aprovado": 
            return render_template('/inicialGerente.html', titulo='Login Gerente', resultado=this.msg)
    return render_template('/login.html', titulo='Login Gerente', resultado=this.msg)

@pessoa.route('/cadastroFunc.html', methods=['GET', 'POST'])
def pag_cadastro():
    return render_template('/cadastroFunc.html', titulo='Página Principal')

@pessoa.route('/atualizarsenha.html', methods=['GET', 'POST'])
def pag_atualizarsenha():
    return render_template('/atualizarsenha.html', titulo='Página Principal')
>>>>>>> 43e78f0014332136966cc5ccee6443ab2ce747be


@pessoa.route('/inicialGerente.html', methods=['GET', 'POST'])
def pag_inicialGerente():
    return render_template('/inicialGerente.html', titulo='Página Principal')

#cadastrar Funcionário
@pessoa.route('/cadastrarGerente.html', methods=['GET','POST'])
def cadastrarGerente():
    if request.method == 'POST':
        this.nome = request.form['coletarNome']
        this.cpfGerente = request.form['coletarCpfGerente']
        this.telefone = request.form['coletarTelefone']
        this.email = request.form['coletarEmail']
        this.senha = request.form['coletarSenha']

        if operacoes.cpf_validate(this.cpfGerente) == True:
            this.dados = operacoes.cadastrarGerente(this.nome, this.cpfGerente, this.telefone, this.email, this.senha)
            return render_template('/cadastrarGerente.html', titulo='Página De Cadastro', resultado=this.dados)
        else:
            this.dados = "ERRO, favor informe um CPF válido!"
    return render_template('/cadastrarGerente.html', titulo='Página De Cadastro', resultado=this.dados)

<<<<<<< HEAD
@pessoa.route('/atualizarGerente.html', methods=['GET','POST'])
=======

@pessoa.route('/atualizarFunc.html', methods=['GET','POST'])
>>>>>>> 43e78f0014332136966cc5ccee6443ab2ce747be
def atualizarDados():
    if request.method == 'POST':
        this.cpf = request.form['tCpf']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dados = operacoes.atualizarGerente(this.cpf, this.campo, this.nDado)
    return render_template('/atualizarGerente.html', titulo='Atualizar', resultado=this.dados)


@pessoa.route('/consultarGerente.html', methods=['GET','POST'])
def consultarIndividual():
    if request.method == 'POST':
        this.cpfGerente = request.form['coletarCPF']
        this.mensagem = operacoes.consultar(this.cpfGerente)
    else:
        this.mensagem = ""
    return render_template('/consultarGerente.html', titulo='Consultar por cpf', dados=this.mensagem)

@pessoa.route('/excluirGerente.html', methods=['GET', 'POST'])
def excluirDados():
    if request.method == 'POST':
        this.cpfGerente = request.form['cpfGerente']
        this.dados = operacoes.deletar(this.cpfGerente)
    return render_template('/excluirGerente.html', titulo='Excluir', resultado=this.dados)


@pessoa.route('/inicialCliente.html', methods=['GET','POST'])
def inicialCliente():
    return render_template('/inicialCliente.html', titulo='Página Inicial Cliente', resultado=this.dados)

if __name__ == "__main__":
    pessoa.run(debug=True, port=5003)