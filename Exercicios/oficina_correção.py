class Veiculo:
   def __init__(self, placa, cor):
      self.placa = placa
      self.cor = cor
   
   def __str__(self):
      return f'''
Placa: {self.placa}
Cor: {self.cor}'''

class Carro(Veiculo):
   def __init__(self, por, placa, cor):
      super().__init__(placa, cor)
      self.porta = por
   
   def __str__(self):
      return f'''
{super().__str__()}
portas: {self.porta}
              '''

a = Carro(2, "fwf-hehe", "azul")
print(a)