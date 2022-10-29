from random import random
import random
import email
import mysql.connector
import conexao
import this
import this
import array


db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

this.msg = ""
this.cpf = ""
this.sorteados = ""

this.vetorNome = []
this.vetorCPF = []
this.vetorManha = []
this.vetorTarde = []
this.vetorNoite = []
this.dados_sorteio = []


#Consultar os dados do BD
def selecionarSort():
    try:
        sql = "select * from inscricao".format()
        con.execute(sql)

        this.msg = ""
        this.msg = " Nenhuma Inscrição Encontrada! "
        for (cpfFunc, nome, manha, tarde, noite) in con:
                this.vetorCPF.append(cpfFunc)
                this.vetorNome.append(nome)
                this.vetorManha.append(manha)
                this.vetorTarde.append(tarde)
                this.vetorNoite.append(noite)

    except Exception as erro:
        return erro

def sorteio():

        lista_sorteados = [this.vetorCPF, this.vetorNome, this.vetorManha, this.vetorTarde, this.vetorNoite]
        resultado_lista = random.choice(lista_sorteados)
        return "Os sorteados são {} ".format(resultado_lista)