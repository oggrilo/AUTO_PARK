from cgitb import html
import mysql.connector
import conexao
import this

from main import inicialCliente
this.msg = ""

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def cadastrarGerente(nome, cpfGerente, telefone, email, senha):
    try:
        sql = "insert into gerente(nome, cpfGerente, telefone, email, senha) values('{}','{}','{}','{}','{}')".format(nome, cpfGerente, telefone, email, senha)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        return con.rowcount, "Cadastrado com sucesso!"
    except Exception as erro:
        return erro

def trocarSenha(cpfGerente, senhaGerente):
    try:
        sql = "update gerente set senhaFunc = '{}' where cpfGerente = '{}'".format(cpfGerente, senhaGerente)
        con.execute(sql)
        db_connection.commit()
        print(con.rowcount, "Senha Atualizada com sucesso!")
    except Exception as erro:
        print(erro)

def atualizarGerente(cpfGerente, campo, novoDado):
    try:
        sql = "update gerente set {} = '{}' where cpfGerente = '{}'".format(campo, novoDado, cpfGerente)
        con.execute(sql)
        db_connection.commit()
        return "Atualizado com sucesso!".format(con.rowcount)
    except Exception as erro:
        return erro

def consultar(cpfGerente):
    try:
        sql = "select * from gerente where cpfGerente = '{}'".format(cpfGerente)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"
        for(cpfGerente, nome, celular, email, senha) in con:
            if int(cpfGerente) == int(cpfGerente):
                this.msg = "Cpf: {}, Nome: {}, Telefone: {}, Email: {}, Senha: {}".format(cpfGerente, nome, celular, email, senha)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro

def deletar(cpfGerente):
    try:
        sql = "delete from gerente where cpfGerente = '{}'".format(cpfGerente)
        con.execute(sql)
        db_connection.commit()
        return "{} deletado!".format(con.rowcount)
    except Exception as erro:
        return erro