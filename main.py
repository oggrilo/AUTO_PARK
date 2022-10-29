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
def loginGerente():
    if request.method == 'POST':
        this.emailGerente = request.form['emailGerente']
        this.senhaGerente = request.form['senhaGerente']
        this.msg = operacoes.loginGerente(this.emailGerente, this.senhaGerente)
        if this.msg == "Aprovado": 
            return render_template('/inicialGerente.html', titulo='Login Gerente', resultadoLogin=this.msg)
        if this.msg == "Dados incorretos":        
            return render_template('/login.html', titulo='Login Gerente', resultadoLogin=this.msg)
    return render_template('/login.html', titulo='Login Gerente', resultadoLogin=this.msg)

@pessoa.route('/cadastrarInscricao.html', methods=['GET', 'POST'])
def pag_cadastrarInscricao():
    return render_template('/cadastrarInscricao.html', titulo='Página Principal')

@pessoa.route('/atualizarInscricao.html', methods=['GET', 'POST'])
def pag_atualizarIncricao():
    return render_template('/atualizarInscricao.html', titulo='Página Principal')

@pessoa.route('/consultarInscricao.html', methods=['GET', 'POST'])
def pag_consultarInscricao():
    return render_template('/consultarInscricao.html', titulo='Página Principal')

@pessoa.route('/deletarInscricao.html', methods=['GET', 'POST'])
def pag_deletarInscricao():
    return render_template('/deletarInscricao.html', titulo='Página Principal')

@pessoa.route('/atualizarPeriodoInscricao.html', methods=['GET', 'POST'])
def pag_periodoInscricao():
    return render_template('/atualizarPeriodoInscricao.html', titulo='Página Principal')


#cadastrar Funcionário
@pessoa.route('/cadastrarGerente.html', methods=['GET','POST'])
def cadastrarGerente():
    if request.method == 'POST':
        this.cpfGerente = request.form['coletarCpfGerente']
        this.nome = request.form['coletarNome']
        this.email = request.form['coletarEmail']
        this.celular = request.form['coletarCelular']
        this.senha = request.form['coletarSenha']

        if operacoes.cpf_validate(this.cpfGerente) == True:
            this.dados = operacoes.cadastrarGerente(this.cpfGerente, this.nome, this.email, this.celular, this.senha)
            return render_template('/cadastrarGerente.html', titulo='Página De Cadastro', resultado=this.dados)
        else:
            this.dados = "ERRO, favor informe um CPF válido!"
    return render_template('/cadastrarGerente.html', titulo='Página De Cadastro', resultado=this.dados)

@pessoa.route('/atualizarGerente.html', methods=['GET','POST'])
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