from cgitb import html
from operator import truediv
from random import random
from select import select
from shutil import ExecError
import email
import mysql.connector
import conexao
import this

this.msg = ""
this.cpf = ""

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


#Cadastrar Dados
def inserirInsc(codigo, cpfFunc, nome, manha, tarde, noite):
    try:
        sql = "insert into inscricao(cpfFunc, nome, manha, tarde, noite) values('', '{}','{}','{}','{}','{}')".format(codigo, cpfFunc, nome, manha, tarde, noite)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        if cpfFunc =="":
            return "Por favor, digite um CPF a ser cadastrado."
        elif nome == "":
            return "Por favor, digite um Nome a ser cadastrado."
        elif manha == "" and tarde == "" and noite == "":
            return "Por favor, selecione um Período a ser cadastrado."
        else:
            return "Cadastrado com sucesso!"
            
    except Exception as erro:
        return erro

#Consultar os dados do BD
def selecionar_insc(cpfFunc):
    try:
        sql = "select * from inscricao where cpfFunc = '{}'".format(cpfFunc)
        con.execute(sql)

        this.msg = ""
        this.msg = " Nenhuma Inscrição Encontrada! "
        for (codigo, cpfFunc, nome, manha, tarde, noite) in con:
            if cpfFunc == cpfFunc:
                this.msg = "Código: {}, CPF: {}, Nome: {}, Manhã: {}, Tarde: {}, Noite: {}".format(codigo, cpfFunc, nome, manha, tarde, noite)
            return this.msg 
        if cpfFunc =="" or cpfFunc != '{}':
            return "Por favor, digite um CPF cadastrado."
        else:
            return this.msg
    except Exception as erro:
        return erro

#Atualizar os dados do BD
def atualizar(cpfFunc, campo, novoDado):
    try:
        sql = "update inscricao set {} = '{}' where cpfFunc = '{}'".format(campo, novoDado, cpfFunc)
        con.execute(sql)
        db_connection.commit()
        if cpfFunc =="" or cpfFunc != '{}':
            return "Por favor, digite um CPF cadastrado."
        elif novoDado =="":
            return "Por favor, digite um novo dado a ser atualizado."
        else:
            return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

def atualizarPeriodo(cpfFunc, novaManha, novaTarde, novaNoite):
    try:
        sql = "update inscricao set manha = '{}', tarde = '{}', noite = '{}' where cpfFunc = '{}'".format(novaManha, novaTarde, novaNoite, cpfFunc)
        con.execute(sql)
        db_connection.commit()
        if cpfFunc =="" or cpfFunc != '{}':
            return "Por favor, digite um CPF cadastrado."
        else:
            return "{} Atualizado!".format(con.rowcount)
    except Exception as erro:
        return erro

#Deletar os dados do BD
def deletar(cpfFunc):
    try:
        sql = "delete from inscricao where cpfFunc = '{}'".format(cpfFunc)
        con.execute(sql)
        db_connection.commit()
        if cpfFunc =="":
            return "Por favor, digite um CPF cadastrado."
        else:
            return "{} deletado!".format(con.rowcount)
    except Exception as erro:
        return erro