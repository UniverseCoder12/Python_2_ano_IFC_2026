# importar o DAO: Data Access Object (camada de acesso a dados)
import bf_DAO as dao

lista = ["a", "e", "i", "o", "u"]

    #for i in range(5000):
    #    dao.inserir_dados(f"{lista[i % 5]}", i // 5, (i - 10) / 5, i)

# obter a listas de pessoas
foguetes = dao.retornar_foguetes()

# listar as pessoas
for p in foguetes:
    print(p.nome, p.altura, p.peso, p.empuxo)

