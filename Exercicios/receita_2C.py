class Receita:
    def __init__(self, nm, tmp_pr, md_pr, ingr):
        self.nome = nm
        self.tempo_preparo = tmp_pr
        self.modo_preparo = md_pr
        self.ingredientes = ingr
    def __str__(self):
        return f'''
Receita: {self.nome}
Tempo de preparo: {self.tempo_preparo} min
ingredientes: {self.ingredientes}
modo de preparo:
{self.modo_preparo}
                '''

class Ingredientes:
    def __init__(self, nm, quant, uni):
        self.nome = nm
        self.quantidade = quant
        self.unidade = uni
    
    def __str__(self):
        return f'{self.quantidade} {self.unidade} {self.nome}'

ing1 = Ingredientes("Cogumelo", 1, "unidade")
ing2 = Ingredientes("Miojo")
r_ing = []
r1 = Receita("Mario", 50, ' 1-Pegue um cogumelo, 2-Queime ele e grite tres vezes mario, 3- coma um miojo da nitendo',ing)