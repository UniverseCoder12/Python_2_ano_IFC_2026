from pathlib import Path
import sqlite3

class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

caminho = Path(__file__).resolve().parent 

arquivo = caminho / 'pessoas.db'
conn = sqlite3.connect(arquivo)
cursor = conn.cursor()

cursor.execute('SELECT nome, email, telefone FROM pessoas')

pessoas = cursor.fetchall()

for pessoa in pessoas:
    # mostrar as informações de cada pessoa
    print(f'Nome: {pessoa[0]}, Email: {pessoa[1]}, Telefone: {pessoa[2]}')

conn.close()