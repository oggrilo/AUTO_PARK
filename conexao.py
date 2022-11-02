import mysql.connector
from mysql.connector import errorcode

config = {
    'host':'AutoPark.autopark.azurewebsites.net',
    'user':'root',
    'password':'',
    'database':'AutoPark'
}

def conectar():
    try:
        db_connection = mysql.connector.connect(**config)
        print('Conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as error: #Salvando o erro na variável error
        if error.errno == errorcode.ER_BAD_DB_ERROR: #Caso banco de dados não exista
            print('Banco de dados não existe!')
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:#Caso haja um erro de usuário
            print('Nome de usuário ou senha errados!')
        else:
            print(error)
    else:
        db_connection.close()