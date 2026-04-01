class Veiculo():
    def __init__(self, pl, cr):
        self.placa = pl
        self.cor = cr
    def __str__(self):
        return f'''Placa: {self.placa}
Cor: {self.cor}'''

class Moto(Veiculo):
    def __init__(self, placa, cor):
      super().__init__(placa, cor)
    def __str__(self):
        return f'''{super().__str__()}'''

class VeiculosComPassageiros(Veiculo):
    def __init__(self, pl, cr, lg):
        super().__init__(pl, cr)
        self.lugares = lg
    def __str__(self):
        return f'''{super().__str__()}
Lugares: {self.lugares}'''

class Onibus(VeiculosComPassageiros):
    def __init__(self, pl, cr, lg):
        super().__init__(pl, cr, lg)

    def __str__(self):
        return f'''{super().__str__()}'''

class Carro(VeiculosComPassageiros):
    def __init__(self, pl, cr, lg, pr):
        super().__init__(pl, cr, lg)
        self.portas = pr
    def __str__(self):
        return f'''{super().__str__()}
Portas: {self.portas}'''

class Pessoa():
    def __init__(self, nm, tl, dt):
        self.nome = nm
        self.telefone = tl
        self.data_nascimento = dt
    def __str__(self):
        return f'''
Nome: {self.nome}
telefone: {self.telefone}
data de nascimento: {self.data_nascimento}
                '''

class Cliente():
    def __init__(self, pes, em):
        self.pessoa = pes
        self.email = em
    def __str__(self):
        return f'''
{self.pessoa}email: {self.email}
                '''

class Mecanico():
    def __init__(self, pes):
        self.pessoa = pes
    def __str__(self):
        return f"{self.pessoa}"

class Servico():
    def __init__(self, des, vlr):
        self.descricao = des
        self.valor = vlr
    def __str__(self):
        return f'''
Descrição: {self.descricao}
Valor: R$ {self.valor}'''

class ServicoRealizado():
    def __init__(self, ser, mec):
        self.servico = ser
        self.mecanico = mec
    def __str__(self):
        return f'''
mecânico: {self.mecanico.pessoa.nome} {self.servico}
                '''

class OrdemServico():
    def __init__(self, dte, vei, dts, cli, dsc, ser):
        self.data_entrada = dte
        self.veiculo = vei
        self.data_saida = dts
        self.cliente = cli
        self.desconto = dsc
        self.servicos_realizados = ser

    def CalcularTotal(self):
        total = 0
        for i in self.servicos_realizados:
            total = total + i.servico.valor
        total = total - self.desconto
        return total

    def PrintarServicos(self):
        a = ""
        for i in self.servicos_realizados:
            a = a + f"{i.servico.descricao}; "
        return a

    def __str__(self):
        return f'''
data de entrada: {self.data_entrada}
data de saida:{self.data_saida}
{self.veiculo}
Cliente: {self.cliente.pessoa.nome}
Desconto: {self.desconto} reais
Serviços realizados: {self.PrintarServicos()}
Total: {self.CalcularTotal()} reais
'''
        
jo = Pessoa("João", "(99) 9 9999-9999", "01/12/2009")
cl1 = Cliente(jo, "ciclano@email.com")
ma = Pessoa("Mario", "(99) 9 1999-1991", "03/02/1965")
mec1 = Mecanico(ma)
ser = Servico("Troca do óleo do veículo", 200)
ser1 = Servico("Troca dos pneus", 250)
serrel = ServicoRealizado(ser, mec1)
serrel1 = ServicoRealizado(ser1, mec1)
lisSer = [serrel, serrel1]
car = Carro("FJDM-23S3", "Branco", 5, 4)
ordq = OrdemServico("12/5/2026", car, "13/5/2026", cl1, 10, lisSer)

print(ordq)