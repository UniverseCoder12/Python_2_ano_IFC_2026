from pathlib import Path
import sqlite3

class Pessoa():
    def __init__(self, nm, em, tl):
        self.nome = nm
        self.email = em
        self.telefone = tl

caminho = Path(__file__).resolve().parent 
arquivo = caminho / 'pessoas.db'
conn = sqlite3.connect(arquivo)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT NOT NULL)''')
conn.commit()
p1 = Pessoa("Josenildo", "jojo@gmail.com", "47 9 97866567")
cursor.execute('''INSERT INTO pessoas (nome, email, telefone) VALUES (?, ?, ?)''', 
               (p1.nome, p1.email, p1.telefone))
conn.commit()
conn.close()