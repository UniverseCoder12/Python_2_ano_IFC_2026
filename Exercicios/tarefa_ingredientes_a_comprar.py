class Receita:
    def __init__(self, nm, tmp_pr, md_pr, ingr):
        self.nome = nm
        self.tempo_preparo = tmp_pr
        self.modo_preparo = md_pr
        self.ingredientes = ingr
    def __str__(self):
        ing = ""
        for i in self.ingredientes:
            ing = ing + str(i)
        x= f'''
Receita: {self.nome}
Tempo de preparo: {self.tempo_preparo} min
ingredientes: {ing}
modo de preparo:
{self.modo_preparo}
                '''
        return x

class Ingredientes:
    def __init__(self, nm, quant, uni):
        self.nome = nm
        self.quantidade = quant
        self.unidade = uni

    def __str__(self):
        return f'|{self.quantidade} {self.unidade} {self.nome}|'

ing1 = Ingredientes("Cogumelo", 1, "unidade")
ing2 = Ingredientes("Miojo", 1, "Pacote")
r_ing = [ing1, ing2]
r1 = Receita("Mario", 50, ' 1-Pegue um cogumelo, 2-Queime ele e grite tres vezes mario, 3- coma um miojo da nitendo', r_ing)
print(r1)

ing11 = Ingredientes("Miojo", 1, "pacote")
ing12 = Ingredientes("água", 100, "ml")
r_ing12 = [ing11, ing12]
r2 = Receita("miojo cozido", 5, ' 1-Ferva a água 2-Coloque o miojo na água fervendo, 3- espera amolecer e coma', r_ing12)
print(r2)
rec = [r1,r2]
tbl = {}
#lst_ing = []

for re in rec:
    for ing in re.ingredientes:
            if ing.nome in tbl:
                tbl[ing.nome].quantidade += ing.quantidade
            else:
                tbl[ing.nome] = ing
#               lst_ing.append(ing.nome)

for nome in tbl:
    print(tbl[nome])

#for i in lst_ing:
#   print(f"{tbl[i].quantidade} {tbl[i].unidade} de {tbl[i].nome}")