import operacoes
import operacoesInscricao
import operacoes_sorteio

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
    if request.method == 'POST':
        this.cpfFunc = request.form['coletarCPF']
        this.nome = request.form['coletarNome']
        this.manha = request.form['coletarManha']
        this.tarde = request.form['coletarTarde']
        this.noite = request.form['coletarNoite']
        this.dados = operacoesInscricao.inserirInsc( this.cpfFunc, this.nome, this.manha, this.tarde , this.noite)
            
    return render_template('/cadastrarInscricao.html', titulo='Página De Cadastro', resultado=this.dados)

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




#cadastrar Inscrição
this.cpfFunc = ""
this.nomeFunc = ""
this.manha = 1
this.tarde = 1
this.noite = 1
this.dados = ""
this.mensagem = ""
this.nDado = ""
this.nDadoCheckbox = ""


@pessoa.route('/cadastrarInscricao.html', methods=['GET', 'POST'])
def inserirInsc():
    if request.method == 'POST':
        if request.form['coletarCPF'] == "" or request.form['coletarNome'] == "":
            this.dados = "Preencha o campo de CPF e Nome, por favor!"
        else:
            this.cpfFunc    = request.form['coletarCPF']
            this.nomeFunc  = request.form['coletarNome']
            try:
                this.manha = request.form['coletarManha']
                this.manha = 0
            except: 
                this.manha = 1

            try:
                this.tarde = request.form['coletarTarde']
                this.tarde = 0
            except: 
                this.tarde = 1

            try:
                this.noite = request.form['coletarNoite']
                this.noite = 0
            except: 
                this.noite = 1

            this.dados = operacoesInscricao.inserirInsc(this.cpfFunc, this.nomeFunc, this.manha, this.tarde, this.noite)
    return render_template('/cadastrarInscricao.html', titulo='Cadastrar Inscricao', resultado = this.dados)

#consultar Inscrição por CPF
@pessoa.route('/consultarInscricao.html', methods=['GET', 'POST'])
def selecionar_insc():
    if request.method == 'POST':
        this.cpfFunc = request.form['coletarCPF']
        this.mensagem = operacoesInscricao.selecionar_insc(this.cpfFunc)
    else:
        this.mensagem = ""
    return render_template('/consultarInscricao.html', titulo='Página De Consulta Dos Funcionários', dados=this.mensagem)


#Atualizar Inscrição por CPF
@pessoa.route('/atualizarInscricao.html', methods=['GET','POST'])
def atualizar():
    if request.method == 'POST':
        this.cpfFunc = request.form['cpfFunc']
        this.campo = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dados = operacoesInscricao.atualizar(this.cpfFunc, this.campo, this.nDado)
    return render_template('/atualizarInscricao.html', titulo='Atualizar', resultado=this.dados)

@pessoa.route('/atualizarPeriodoInscricao.html', methods=['GET','POST'])
def atualizarPeriodo():
    if request.method == 'POST':
        this.cpfFunc = request.form['cpfFunc']
        try:
            this.nManha = request.form['tNovaManha']
            this.nManha = 0
        except: 
            this.nManha = 1

        try:
            this.nTarde = request.form['tNovaTarde']
            this.nTarde = 0
        except: 
            this.nTarde = 1

        try:
            this.nNoite = request.form['tNovaNoite']
            this.nNoite = 0
        except: 
            this.nNoite = 1
        this.dados = operacoesInscricao.atualizarPeriodo(this.cpfFunc, this.nManha, this.nTarde, this.nNoite)
    return render_template('/atualizarPeriodoInscricao.html', titulo='Atualizar', resultado=this.dados)

#Deletar Inscrição pelo CPF
@pessoa.route('/deletarInscricao.html', methods=['GET', 'POST'])
def deletar():
    if request.method == 'POST':
        this.cpfFunc = request.form['cpfFunc']
        this.dados = operacoesInscricao.deletar(this.cpfFunc)
    return render_template('/deletarInscricao.html', titulo='Excluir', resultado=this.dados)



#sorteio

@pessoa.route('/pag_sorteio.html', methods=['GET', 'POST'])
def selecionar_sorteio():

    return render_template('/pag_sorteio.html', titulo='Sortear', resultadoSorteio=this.dados)



if __name__ == "__main__":
    pessoa.run(debug=True, port=5003)