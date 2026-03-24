class Cliente:
    def __init__(self, nm, em, tl):
        self.nome = nm
        self.email = em
        self.telefone = tl

class Veiculo:
    def __init__(self, tp, pl, cr):
        self.tipo = tp
        self.placa = pl
        self.cor = cr
    
    def __str__(self):
        return f'''
                tipo: {self.tipo}
                cor: {self.cor}        
                placa: {self.placa}
                '''

class Carro:
    def __init__(self, pr):
        self.portas = pr

    def __str__(self):
        return f'''Carro 
                Portas: {self.portas}'''
        

class Onibus:
    def __init__(self, lg):
        self.lugares = lg

    def __str__(self):
        return f'''ônibus 
                Lugares: {self.lugares}'''

class Item_servico:
    def __init__(self, tp, vl, nmm, ve):
        self.tipo = tp
        self.valor = vl
        self.nome_mecanico = nmm
        self.veiculo = ve
    
    def 


    
v = Veiculo(Onibus(20),"F3DS-2134", "Branco")
print(v)