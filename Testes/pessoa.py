class pessoa:
    def __init__(self, e, c, t, n):
        self.nome = n
        self.cpf = c
        self.email = e
        self.telefone = t
    def __str__(self):
        return f'''#Nome: {self.nome}
Telefone: {self.telefone}
Email: {self.email}
CPF: {self.cpf}'''

nm = input("Digite seu nome: ")
em = input("Digite seu email: ")
tel = input("Digite seu telefone: ")
cpf = input("Digite seu CPF: ")



p1 = pessoa(em, cpf, tel, nm)
p1.__str__()

#print(f''' 
#Nome: {p1.nome}
#Telefone: {p1.telefone}
#Email: {p1.email}
#CPF: {p1.cpf}
#''')