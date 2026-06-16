class Veiculo():
    def __init__(self, pl, an):
        self.placa = pl
        self.ano = an

class Moto(Veiculo):
    def __init__(self, pl:str, an: int):
        super().__init__(pl, an)
        
class Caminhao(Veiculo):
    def __init__(self, pl: str, an: int, ps_kg: int):
        super().__init__(pl, an)
        self.peso_em_kg = ps_kg

moto = Moto("sddf-as12", 2000)
caminhao = Caminhao("fdfs-2133", 1980, 8000)

print(moto.placa, moto.ano)
print(caminhao.ano, caminhao.peso_em_kg, caminhao.placa)
        