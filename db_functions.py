import mysql.connector
from config import *

#Estabele conexão com o Banco de dados
def conectar_db ():
    conexao = mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
        )

    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor

#Encerrar a conexão com o BD
def encerrar_db(cursor, conexao):
    cursor.close()
    conexao.close()

def limpar_input(campo):
    campolimpo = campo.replace(".","").replace("/","").replace("-","").replace("","").replace("(","").replace(")","").replace("()","")
    return campolimpo
    