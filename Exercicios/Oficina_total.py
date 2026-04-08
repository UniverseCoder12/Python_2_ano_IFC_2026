from Oficina_Classes import Pessoa, Cliente, Mecanico, Servico, ServicoRealizado, Carro, Moto, Onibus, OrdemServico

def calcular_Total_Cliente(tbl, lstcli):
    a =0




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
oni = Onibus("JUJU-31G4", "rosa-choque", 50)
ordq = OrdemServico("12/5/2026", car, "13/5/2026", cl1, 10, lisSer)
ju = Pessoa("Jubiscleuso", "(47) 9 2376-2343", "11/09/1849")
cl2 = Cliente(ju, "jujudograu@gaymail.com")
serj = Servico("Refazer o motor", 7000)
serrelj = ServicoRealizado(ser, ma)
serrelj1 = ServicoRealizado(ser1, ma)
serrelj2 = ServicoRealizado(serj, ma)
lisSer2 = [serrelj]
lisSer3 = [serrelj1, serrelj2]
ordj1 = OrdemServico("11/12/2026", oni, "12/12/2026", cl2, 0, lisSer2)
ordj2 = OrdemServico("13/12/2026", oni, "01/02/2027", cl2, 500, lisSer3)

lstcli = [cl1, cl2]
lstord = [ordj1, ordj2, ordq]
tbl = {}

for i in lstcli:
    tbl[i.pessoa.nome] = []
    for k in lstord:
        if i.pessoa.nome == k.cliente.pessoa.nome:
            tbl[i.pessoa.nome].append(k)

print(tbl)
