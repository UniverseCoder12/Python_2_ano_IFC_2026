from Oficina_Classes import Pessoa, Cliente, Mecanico, Servico, ServicoRealizado, Carro, Moto, Onibus, OrdemServico
        
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