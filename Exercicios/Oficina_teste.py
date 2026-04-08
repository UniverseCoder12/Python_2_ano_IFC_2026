from Oficina_Classes import Pessoa, Cliente, Mecanico, Servico, ServicoRealizado, Carro, Moto, Onibus, OrdemServico
import unittest

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

class Test_Oficina(unittest.TestCase):
    def test_pessoa(self):
        self.assertEqual(jo.data_nascimento, "01/12/2009")
        self.assertEqual(jo.nome, "João")
        self.assertEqual(jo.telefone, "(99) 9 9999-9999")

    def test_cliente(self):
        self.assertEqual(cl1.pessoa.data_nascimento, "01/12/2009")
        self.assertEqual(cl1.pessoa.nome, "João")
        self.assertEqual(cl1.pessoa.telefone, "(99) 9 9999-9999")
        self.assertEqual(cl1.email, "ciclano@email.com")
    
    def test_mecanico(self):
        self.assertEqual(mec1.pessoa.data_nascimento, "03/02/1965")
        self.assertEqual(mec1.pessoa.nome, "Mario")
        self.assertEqual(mec1.pessoa.telefone, "(99) 9 1999-1991")

    def test_servico(self):
        self.assertEqual(ser.descricao, "Troca do óleo do veículo")
        self.assertEqual(ser.valor, 200)

    def test_servico_realizado(self):
        self.assertEqual(serrel.mecanico.pessoa.data_nascimento, "03/02/1965")
        self.assertEqual(serrel.mecanico.pessoa.nome, "Mario")
        self.assertEqual(serrel.mecanico.pessoa.telefone, "(99) 9 1999-1991")
        self.assertEqual(serrel.servico.descricao, "Troca do óleo do veículo")
        self.assertEqual(serrel.servico.valor, 200)
    
    def test_carro(self):
        self.assertEqual(car.cor, "Branco")
        self.assertEqual(car.lugares, 5)
        self.assertEqual(car.placa, "FJDM-23S3")
        self.assertEqual(car.portas, 4)
    
    def test_onibus(self):
        oni = Onibus("FJDM-23S3", "Branco", 20)

        self.assertEqual(oni.cor, "Branco")
        self.assertEqual(oni.lugares, 20)
        self.assertEqual(oni.placa, "FJDM-23S3")

    def test_moto(self):
        mt = Moto("FJDM-23S3", "Branco")

        self.assertEqual(mt.cor, "Branco")
        self.assertEqual(mt.placa, "FJDM-23S3")

    def test_ordem_e_servico(self):
        self.assertEqual(ordq.cliente.pessoa.data_nascimento, "01/12/2009")
        self.assertEqual(ordq.cliente.pessoa.nome, "João")
        self.assertEqual(ordq.cliente.pessoa.telefone, "(99) 9 9999-9999")
        self.assertEqual(ordq.cliente.email, "ciclano@email.com")
        self.assertEqual(ordq.servicos_realizados[0].mecanico.pessoa.data_nascimento, "03/02/1965")
        self.assertEqual(ordq.servicos_realizados[0].mecanico.pessoa.nome, "Mario")
        self.assertEqual(ordq.servicos_realizados[0].mecanico.pessoa.telefone, "(99) 9 1999-1991")
        self.assertEqual(ordq.servicos_realizados[0].servico.descricao, "Troca do óleo do veículo")
        self.assertEqual(ordq.servicos_realizados[0].servico.valor, 200)
        self.assertEqual(ordq.veiculo.cor, "Branco")
        self.assertEqual(ordq.veiculo.lugares, 5)
        self.assertEqual(ordq.veiculo.placa, "FJDM-23S3")
        self.assertEqual(ordq.veiculo.portas, 4)
        self.assertEqual(ordq.data_entrada, "12/5/2026")
        self.assertEqual(ordq.data_saida, "13/5/2026")
        self.assertEqual(ordq.desconto, 10)
        self.assertEqual(ordq.CalcularTotal(), 440)
        
if __name__ == '__main__':
    unittest.main()


#print(ordq)