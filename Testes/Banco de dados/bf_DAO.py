# importar a classe
from bc_classe import Foguete

# importar a biblioteca para trabalhar com MySQL
import mysql.connector

def retornar_foguetes():

    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.27",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE info2026emi")
    
    # executar o comando SQL para selecionar todas as pessoas
    cursor.execute('SELECT nome, altura, peso, empuxo FROM Leonardo_teste_foguete')
    
    # obter os resultados da consulta
    foguetes = cursor.fetchall()

    # preparar uma lista de retorno
    retorno = []

    # percorrer a lista de pessoas obtidas
    for foguete in foguetes:

        # converter cada pessoa obtida em um OBJETO
        nova = Foguete(foguete[0], foguete[1], foguete[2], foguete[3])

        # adicionar a nova pessoa_objeto na lista de retorno
        retorno.append(nova)

    # fechar a conexão com o banco de dados
    conn.close()

    # retornar o retorno :-)
    return retorno


def criar_tabela():
    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.239",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE info2026emi")

    cursor.execute(
        "CREATE TABLE Leonardo_teste_foguete (" \
        "id INT PRIMARY KEY AUTO_INCREMENT," \
        "nome VARCHAR(100)," \
        "altura DECIMAL(10, 5)," \
        "peso DECIMAL(10, 5)," \
        "empuxo DECIMAL(10, 5)" \
    ")")

    conn.commit()
    conn.close()

def inserir_dados(nome, altura, peso, empuxo):
    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.239",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE info2026emi")
    cursor.execute(
        f"INSERT INTO Leonardo_teste_foguete(nome, altura, peso, empuxo) VALUES ('{nome}', {altura}, {peso}, {empuxo})"
    )

    conn.commit()
    conn.close()

def deletar_tabela(nome):
    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.239",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE info2026emi")

    cursor.execute("DROP TABLE Leonardo_teste_foguete")

'''
alternativas:

a) retorno = [Pessoa(nome, email, telefone) for nome, email, telefone in cursor.fetchall()]

b) return [Pessoa(*pessoa) for pessoa in cursor.fetchall()]

'''