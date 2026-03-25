class Veiculo:
   def __init__(self, placa, cor):
      self.placa = placa
      self.cor = cor

class Carro(Veiculo):
   def __init__(self, por):
      super().__init__(placa, cor)