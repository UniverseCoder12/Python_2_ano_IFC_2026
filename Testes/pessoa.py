class pessoa:
    def __init__(self, e, c, t, n):
        self.nome = n
        self.cpf = c
        self.email = e
        self.telefone = t

nm = input("Digite seu nome: ")
em = input("Digite seu email: ")
tel = input("Digite seu telefone: ")
cpf = input("Digite seu CPF: ")



p1 = pessoa(em, cpf, tel, nm)

print(f''' 
Nome: {p1.nome}
Telefone: {p1.telefone}
Email: {p1.email}
CPF: {p1.cpf}
''')