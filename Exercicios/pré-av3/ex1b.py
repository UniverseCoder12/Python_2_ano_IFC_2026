import datetime

class Cliente():
    def __init__(self, nm: str, dtns, cpf: str):
        self.nome = nm
        self.data_nasciento = dtns
        self.cpf = cpf

class Prato():
    def __init__(self, nm: str, ing: list[str], mdpr: str, pr: float):
        self.nome = nm
        self.ingredientes = ing
        self.modo_de_preparo = mdpr
        self.preco = pr

class Item_do_pedido():
    def __init__(self, pr: Prato, vl: float, qn: int):
        self.prato = pr
        self.valor_prato = vl
        self.quantidade = qn

        
class Pedido():
    def __init__(self, dtpd, prdes: float, cl: Cliente, it: list[Item_do_pedido]):
        self.data_pedido = dtpd
        self.percentual_desconto = prdes
        self.cliente = cl
        self.itens = it
        self.valor_final = 0
    def definirValorFinal(self):
        vlto = 0
        for i in self.itens:
            vlto += i.valor_prato * i.quantidade
        self.valor_final = vlto / (1 + self.percentual_desconto/100)
    def printarItens(self):
        prt = ""
        for i in self.itens:
            prt += "Nome: " + i.prato.nome+", "
            prt += f"Quantidade: {i.quantidade}, "
            prt += f"Valor: {i.valor_prato:.2f}; "
        return prt
            
    def __str__(self):
        prt = self.printarItens()
        self.definirValorFinal()
        return f'''Data do pedido: {self.data_pedido},
percentual de desconto: {self.percentual_desconto}%,
cliente: {self.cliente.nome}
Pratos: {prt}
Valor Final: {self.valor_final:.2f}
'''
        

cl1 = Cliente("JOSISBELTO", datetime.date(2006, 6, 15), "123.456.789-01")
pr1 = Prato("Carbonara", ["Macarrão","Ovo","Bacon"], "coloca macarrão, ovo e bacon", 40.50)
pr2 = Prato("Miojo do Mario", ["Miojo, Mario"], "esquente o miojo e misture com o mario triturado", 1000.34)
pr3 = Prato("Lasanha", ["lasanha", "carne"], "coloque uma camada massa, outra carne", 20.23)
it1 = Item_do_pedido(pr1, 40.50, 2)
it2 = Item_do_pedido(pr2, 1000.34, 1)
it3 = Item_do_pedido(pr3, 20.23, 4)
lis_it = [it1,it2,it3] 
pd = Pedido(datetime.date(2026, 6, 12), 20.5, cl1, lis_it)

print(pd)

'''
2) no diagrama II o preço no registro também muda, no diagrama III isso não acontece.
3) a) Vetor x = 600
b) dentro do def update:"    
if quad.top > 600 or quad.top < 0:
    exit()
"
'''

        