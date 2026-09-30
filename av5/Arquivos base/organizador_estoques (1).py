import json

estoque = []

print('''  Organizador de Estoque 3000
      
▶︎ Pressione enter para Iniciar''')

dec = 0
inutil = input()

#Adiciona ou retira a quantidade de um produto do estoque(Se tentar retirar mais que tem no estoque, manda uma mensagem avisando e não retira), o parametro pro refere se ao produto cadastrado e o parametro quant é a quantidade retirada ou adicionada no estoque
def adicionar_retirar_pro(pro, quant):
    for i in estoque:
        if i["nome"] == pro and i["quant"] + quant > -1:
            i["quant"] += quant
        elif i["nome"] == pro and i["quant"] + quant < 0:
            print("Estoque insuficiente")
            
def deletar(pro):
    for i in range(len(estoque)):
        if estoque[i]["nome"] == pro:
            estoque.pop(i)
            return

#Cadastra produtos e guarda eles em uma lista chamada "estoque", o parametro nome refere se ao nome do produto, o parametro tipo refere se ao tipo do produto cadastrado, o parametro quant refere se a quantidade de produtos, e o parametro preco refere se ao preço do produto
def cadastrar_pro(nome, tipo, quant, preco):
    estoque.append({"nome": nome, "tipo": tipo, "quant": quant, "preco": preco})

#Muda o Preço do Produto, o parametro preco se refere a uma variavel float que armazena o novo preço do produto, quanto o parametro pro, se refere uma variavel string utilizada para selecionar o produto desejado
def mudar_preco(preco, pro):
    for i in estoque:
        if i["nome"] == pro:
            i["preco"] = preco

#Mostra todos os produtos que estão fora do Estoque  
def mostrar_pro_fora_estoque():
    print("Produtos fora do estoque:")
    for i in estoque:
        if i["quant"] < 1:
            print(i["nome"])    

#Mostra todo o Estoque
def mostrar_estoque():
    for i in estoque:
        print("Produto: ", i["nome"])
        print("Tipo: ", i["tipo"])
        print("Quantidade no estoque: ", i["quant"])
        print("Preço: ", i["preco"])
        print("")

#Busca Produtos no Estoque por tipo do produto, o parametro tipo refere a uma string temporaria que se refere ao tipo do produto
def buscar_pro(tipo):
    for i in estoque:
        if i["tipo"] == tipo:
            print("Nome: ", i["nome"])
            print("Quantidade no estoque: ", i["quant"])

#Organiza o Estoque pelo nome do produto em ordem alfabética utilizando o insertion sort, o parametro estoque se refere a lista onde está localizados os produtos no estoque 
def organizar_est(estoque):
    for i in range(1, len(estoque)):
        for k in range(i-1, -1, -1):
            if estoque[i]["nome"] < estoque[k]["nome"]:
                aux = estoque[i]
                estoque[i] = estoque[k]
                estoque[k] = aux

#Lê o arquivo "Estoque.txt" e coloca o que tem dentro na lista estoque
def carregar():
    global estoque
    with open('Estoque.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        if linhas:
            estoque = json.loads(linhas[0].strip())
        else:
            estoque = []

#Salva o que está contido na lista estoque e coloca no arquivo "Estoque.txt"
def salvar():
    with open('Estoque.txt', 'w') as arquivo:
        json.dump(estoque, arquivo)    

#Digita o menu no terminal
def menu():
    print("┍──────────────────────────────┑ \n| 1- Cadastrar produtos        | \n| 2- Buscar Produtos (por tipo)| \n| 3- Adicionar/Retirar itens   | \n| 4- Mostrar o estoque         | \n| 5- Produtos fora do estoque  |\n| 6- Salvar                    | \n| 7- Carregar                  | \n| 8- Mudar o Preço             | \n| 9- Sair                      | \n┕──────────────────────────────┙")

#Organiaza todas as funções
def main():

    global dec

    while dec != 9:
        menu()
        dec = int(input("Selecione uma opção: "))
        if dec == 1:
            nome = input("Coloque o nome do produto: ")
            tipo = input("Coloque o tipo do produto: ")
            quant = int(input("Coloque a quantidade do produto no estoque: "))
            preco = float(input("Coloque o preço do produto: "))
            cadastrar_pro(nome, tipo, quant, preco)
        elif dec == 2:
            tipo = input("Qual tipo de produto você quer buscar: ")
            buscar_pro(tipo)
        elif dec == 3:
            pro = input("Selecione o produto: ")
            quant = int(input("Quanto você quer retirar ou adicionar no estoque(números positivos: adicionar/ números negativos com o - na frente: retirar): "))
            adicionar_retirar_pro(pro, quant)
            deletar(pro)
        elif dec == 4:
            organizar_est(estoque)
            mostrar_estoque()
        elif dec == 5:
            mostrar_pro_fora_estoque()
        elif dec == 6:
            salvar()
        elif dec == 7:
            carregar()
        elif dec == 8:
            pro = input("Selecione o produto: ")
            preco = float(input("Mude o Preço do Produto: "))
            mudar_preco(preco, pro)
        elif dec == 9:
            print("Tenha um bom dia!")

if __name__ == "__main__":
    main()