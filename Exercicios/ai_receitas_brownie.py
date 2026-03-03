class Receita:
    def __init__(self, nome, tempo_preparo, modo_preparo):
        self.nome = nome
        self.tempo_preparo = tempo_preparo
        self.modo_preparo = modo_preparo
    # como expressar uma receita em formato textual        
    def __str__(self):
        return f'''
        Receita: {self.nome}
        Tempo de preparo: {self.tempo_preparo} minutos
        Como preparar: {self.modo_preparo}
        '''

class Ingrediente:
    def __init__(self,nome):
        self.nome=nome

class IngredienteDaReceita:
    def __init__(self, receita, ingrediente, quantidade, unidade):
        self.receita = receita
        self.ingrediente = ingrediente
        self.quantidade = quantidade
        self.unidade = unidade

# teste da classe

r1 = Receita("Brownie", 40,
              '''1-Misture os ovos e o açúcar.
              2-Em seguida, agregue todos os outros ingredientes até formar um creme uniforme.
              3-Despeje em uma assadeira, forrada com papel-manteiga e leve ao forno médio por 40 minutos.
              4-O brownie estará pronto quando a parte de cima estiver levemente corada e, ao se espetar um palito, ele esteja levemente úmido (devido ao chocolate derretido).
              5-Corte em quadrados ainda quente e sirva com uma bola de sorvete de creme, ou congele num saquinho para freezer.
              6-Para descongelar, coloque o brownie num prato de sobremesa e aqueça no micro-ondas, potência alta, por 1 minuto.''')    

i1= Ingrediente("Margarina sem sal")
i2= Ingrediente("Achocolatado")
i3= Ingrediente("Chocolate em pó")
i4= Ingrediente("Açúcar")
i5= Ingrediente("Sal")
i6= Ingrediente("Chocolate meio amargo picado em cubinhos")
i7= Ingrediente("Farinha de trigo")
i8= Ingrediente("Ovos")
i9= Ingrediente("Essência de baunilha")
i10= Ingrediente("Nozes Picadas")

ir1 = IngredienteDaReceita(r1, i1, 6, "Colheres de sopa")
ir2 = IngredienteDaReceita(r1, i2, 0.75, "Xícaras")
ir3 = IngredienteDaReceita(r1, i3, 0.5, "Xícaras")
ir4 = IngredienteDaReceita(r1, i4, 2, "Xícaras")
ir5 = IngredienteDaReceita(r1, i5, 2, "Pitadas de")
ir6 = IngredienteDaReceita(r1, i6, 1, "Tablete")
ir7 = IngredienteDaReceita(r1, i7, 1.25, "Xícaras")
ir8 = IngredienteDaReceita(r1, i8, 4, "Unidades de")
ir9 = IngredienteDaReceita(r1, i9, 1, "colher de chá")
ir10 = IngredienteDaReceita(r1, i10, 0.5, "Xícaras")

irs = [ir1, ir2, ir3, ir4, ir5, ir6, ir7, ir8, ir9, ir10]
print(r1) # .nome, r1.tempo_preparo, r1.modo_preparo)
#print(ir1, ir2, ir3, ir4, ir5, ir6)

for ir in irs:
    print(ir.quantidade, ir.unidade, ir.ingrediente.nome)