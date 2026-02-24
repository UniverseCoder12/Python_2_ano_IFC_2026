class Pessoa:
        def __init__(self, nm, em):
            self.nome = nm
            self.email = em
        
class celular:
        def __init__(self, num, mrc, opr, dn):
            self.numero = num
            self.marca = mrc
            self.operadora = opr
            self.dono = dn
        
joao = Pessoa("João", "jo@gmail.com")
k10 =celular("991164350", "LG", "Vivo", joao)
print(k10.dono.nome)