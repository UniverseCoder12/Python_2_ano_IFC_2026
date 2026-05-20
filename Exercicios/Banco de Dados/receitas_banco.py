from pathlib import Path
import sqlite3

class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
    # como expressar uma receita em formato textual        
    # def __str__(self):
    #     x = ""
    #     for ing in self.ingredientes:
    #         x += str(ing)
        # 
        # return f'''
        # Receita: {self.nome}
        # Tempo de preparo: {self.tempo_preparo} minutos
        # Como preparar: {self.modo_preparo}
        # Ingredientes: {x}
        # '''

class Ingrediente:
    def __init__(self,nome, quantidade, unidade, receita):
        self.nome=nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.receita = receita
    def __str__(self):
        return f"\n{self.quantidade} {self.unidade} de {self.nome}"

# teste da classe
r1 = Receita("Bolo de Milho", 50, "Bater tudo no liquidificador e colocar no forno")
i1= Ingrediente("Milho", 1, "lata", r1)
i2= Ingrediente("Leite", 1, "lata (milho)", r1)
i3= Ingrediente("Açúcar", 0.5, "lata (milho)", r1)
i4= Ingrediente("Ovos", 3, "unidade", r1)
i5= Ingrediente("Óleo", 0.5, "lata (milho)", r1)
i6= Ingrediente("Fermento", 1, "colher de chá", r1)    

# print(r1)



'''

Receita: Bolo de Milho
        Tempo de preparo: 50 minutos
        Como preparar: Bater tudo no liquidificador e colocar no forno
        Ingredientes: 
1 lata de Milho
1 lata (milho) de Leite
0.5 lata (milho) de Açúcar
3 unidade de Ovos
0.5 lata (milho) de Óleo
1 colher de chá de Fermento

'''

caminho = Path(__file__).resolve().parent 
arquivo = caminho / 'pessoas.db'
conn = sqlite3.connect(arquivo)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS receita
                  (id_receita INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   modo_de_preparo TEXT NOT NULL,
                   tempo_de_preparo INTEGER NOT NULL)''')
conn.commit()
cursor.execute('''INSERT INTO receita (nome, modo_de_preparo, tempo_de_preparo) VALUES (?, ?, ?)''', 
               (r1.nome, r1.modo_preparo, r1.tempo_preparo))
cursor.execute('''CREATE TABLE IF NOT EXISTS ingrediente
                  (id_ingrediente INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   quantidade INTEGER NOT NULL,
                   unidade TEXT NOT NULL,
                   id_receita INTEGER,
                   FOREIGN KEY (id_receita) REFERENCES receita (id_receita))''')
conn.commit()
cursor.execute('''SELECT id_receita FROM receita WHERE nome = ?''', (r1.nome,))
id_receita = cursor.fetchone()[0]
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i1.nome, i1.quantidade, i1.unidade, id_receita))
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i2.nome, i2.quantidade, i2.unidade, id_receita))
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i3.nome, i3.quantidade, i3.unidade, id_receita))
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i4.nome, i4.quantidade, i4.unidade, id_receita))
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i5.nome, i5.quantidade, i5.unidade, id_receita))
conn.commit()
cursor.execute('''INSERT INTO ingrediente (nome, quantidade, unidade, id_receita) VALUES (?, ?, ?, ?)''', 
               (i6.nome, i6.quantidade, i6.unidade, id_receita))
conn.commit()
conn.commit()
conn.close()