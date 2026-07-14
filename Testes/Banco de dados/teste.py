import mysql.connector

def deletar_tabela():
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

deletar_tabela()