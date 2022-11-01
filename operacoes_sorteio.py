from random import random
import random
import mysql.connector
import conexao
import this
import this

import operacoesInscricao

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def selecionar_sorteado():
    try:
        sql = "select * from vaga".format()
        con.execute(sql)
        random.shuffle(sql)
        sweep = list(zip(sql))
        for s in sweep:
            print(s[0] + '--->' + s[1])

    except Exception as erro:
        return erro