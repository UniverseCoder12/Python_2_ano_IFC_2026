from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass

class Marca(Base):
    __tablename__ = "tabela_marcas"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250))
    telefone: Mapped[str] = mapped_column(String(11))
    categoria: Mapped[str] = mapped_column(String(250))
    produtos: Mapped[List["Produto"]] = relationship(back_populates="marca")


class Produto(Base):
    __tablename__ = "tabela_produtos"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    id_marca: Mapped[int] = mapped_column(ForeignKey("tabela_marcas.id"))
    nome: Mapped[str] = mapped_column(String(250))
    preco: Mapped[float] = mapped_column(Float)
    quantidade: Mapped[int] = mapped_column(Integer)
    marca: Mapped["Marca"] = relationship(back_populates="produtos")

def menu():

    print("""
┍──────────────────────────────┑
| 1 - Adicionar produto        |
| 2 - Buscar produtos          |
| 3 - Adicionar/Retirar itens  |
| 4 - Mostrar o estoque        |
| 5 - Produtos fora do estoque |
| 6 - Cadastrar marca          |
| 7 - Mudar o preço            |
| 8 - Deletar produto          |
| 9 - Mostrar marcas           |
| 0 - Sair do Banco            |
┕──────────────────────────────┙
""")

def cadastrar_marca(session):
    nome = input("Nome da marca: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    categoria = input("Categoria: ")

    marca = Marca(nome=nome,email=email,telefone=telefone,categoria=categoria)

    session.add(marca)
    session.commit()

    print("\nMarca cadastrada com sucesso!")
    print("ID da marca:", marca.id)

def mostrar_marcas(session):

    marcas = session.query(Marca).order_by(Marca.id).all()

    if not marcas:
        print("\nNenhuma marca cadastrada.")
        return

    for marca in marcas:
        print(
            f"ID: {marca.id}"
            f"Nome: {marca.nome}"
            f"Categoria: {marca.categoria} \n"
        )

def cadastrar_pro(session):

    nome = input("Nome do produto: ")

    try:
        id_marca = int(input("Código da marca: "))
        quantidade = int(input("Quantidade no estoque: "))
        preco = float(input("Preço do produto: "))

    except ValueError:
        print("\nValor inválido.")
        return
    
    marca = session.get(Marca, id_marca)

    if marca is None:
        print("\nEssa marca não existe.")
        print("Cadastre a marca antes de cadastrar o produto.")
        return

    produto = Produto(nome=nome,id_marca=id_marca,preco=preco,quantidade=quantidade)

    session.add(produto)
    session.commit()

    print("\nProduto cadastrado com sucesso!")
    print("ID do produto:", produto.id)

def buscar_pro(session):

    tipo = input("\nDigite o nome, marca ou categoria que deseja buscar: ")
    produtos = (session.query(Produto).join(Marca).filter((Produto.nome.ilike(f"%{tipo}%")) | (Marca.nome.ilike(f"%{tipo}%")) | (Marca.categoria.ilike(f"%{tipo}%"))).order_by(Produto.id).all())

    if not produtos:
        print("\nNenhum produto encontrado.")
        return

    for produto in produtos:

        print(
            f"\nID: {produto.id} "
            f"Produto: {produto.nome} "
            f"Marca: {produto.marca.nome} "
            f"Categoria: {produto.marca.categoria} "
            f"Preço: R$ {produto.preco:.2f} "
            f"Quantidade: {produto.quantidade}"
        )

def adicionar_retirar_pro(session):

    try:
        id_produto = int(input("\nDigite o ID do produto: "))
        quantidade = int(input("Quantidade (+ para adicionar / - para retirar): "))

    except ValueError:
        print("\nValor inválido.")
        return

    produto = session.get(Produto,id_produto)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    nova_quantidade = produto.quantidade + quantidade

    if nova_quantidade < 0:
        print("\nNão é possível retirar mais produtos")
        print("do que existem no estoque.")

        print(f"Quantidade atual: {produto.quantidade}")

        return

    produto.quantidade = nova_quantidade

    session.commit()

    print("\nEstoque atualizado!")
    print(
        f"{produto.nome}: "
        f"{produto.quantidade} unidades"
    )

def mostrar_estoque(session):

    produtos = (session.query(Produto).join(Marca).order_by(Produto.nome).all())

    if not produtos:

        print("\nO estoque está vazio.")
        return

    for produto in produtos:

        print(
            f"ID: {produto.id:<4} "
            f"Produto: {produto.nome:<25} "
            f"Marca: {produto.marca.nome:<15} "
            f"Quantidade: {produto.quantidade:<5} "
            f"Preço: R$ {produto.preco:.2f}"
        )

def mostrar_pro_fora_estoque(session):

    produtos = (session.query(Produto).filter(Produto.quantidade <= 0).order_by(Produto.nome).all())

    if not produtos:
        print("\nNão existem produtos fora de estoque.")
        return

    for produto in produtos:
        print(
            f"ID: {produto.id}"
            f"Produto: {produto.nome}"
            f"Marca: {produto.marca.nome}"
            f"Quantidade: {produto.quantidade}"
        )

def mudar_preco(session):

    try:
        id_produto = int(input("\nDigite o ID do produto: "))
        novo_preco = float(input("Digite o novo preço: "))

    except ValueError:
        print("\nValor inválido.")
        return

    produto = session.get(Produto,id_produto)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    if novo_preco < 0:
        print("\nO preço não pode ser negativo.")
        return

    produto.preco = novo_preco

    session.commit()

    print("\nPreço alterado com sucesso!")

def deletar(session):

    try:
        id_produto = int(input("\nDigite o ID do produto que deseja deletar: "))

    except ValueError:
        print("\nID inválido.")
        return

    produto = session.get(Produto, id_produto)

    if produto is None:
        print("\nProduto não encontrado.")
        return

    print(f"\nProduto selecionado: {produto.nome}")

    confirmacao = input("Tem certeza que deseja deletar? (s/n): ")

    if confirmacao.lower() != "s":
        print("\nOperação cancelada.")
        return

    session.delete(produto)
    session.commit()

    print("\nProduto deletado com sucesso!")

def main():

    while True:

        print("┍──────────────────────────────┑")
        print("|       ESCOLHA O BANCO        |")
        print("|                              |")
        print("| 1 - SQLite                   |")
        print("| 2 - MySQL                    |")
        print("| 3 - Fechar Programa          |")
        print("┕──────────────────────────────┙")
        
        escolha = input("Selecione uma opção: ")
        
        if escolha == "1":
            engine = create_engine("sqlite:///estoque.db",echo=False)
            print("\nBanco SQLite selecionado.")
        
        elif escolha == "2":
        
            usuario = os.getenv("MYSQL_USER")
            senha = os.getenv("MYSQL_PASSWORD")
            host = os.getenv("MYSQL_HOST")
            porta = os.getenv("MYSQL_PORT")
            banco = os.getenv("MYSQL_DATABASE")
            print(usuario)
        
            senha = senha or ""
        
            url = (f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}")
        
            try:
                engine = create_engine(url,echo=False)
        
                with engine.connect():
                    pass
        
                print("\nBanco MySQL selecionado.")
        
            except Exception as erro:
                print("\nNão foi possível conectar ao MySQL.")
                print("Erro:", erro)
        
        elif escolha == "3":
            print("Tenha um Bom dia")
            break
        
        else:
            print("Opção inválida.")


        Base.metadata.create_all(engine)

        print("\nBanco de dados pronto!")

        with Session(engine) as session:

            while True:

                menu()

                try:
                    opcao = int(input("Selecione uma opção: "))

                except ValueError:
                    print("\nDigite um número válido.")
                    continue

                if opcao == 1:
                    cadastrar_pro(session)

                elif opcao == 2:
                    buscar_pro(session)

                elif opcao == 3:
                    adicionar_retirar_pro(session)

                elif opcao == 4:
                    mostrar_estoque(session)

                elif opcao == 5:
                    mostrar_pro_fora_estoque(session)

                elif opcao == 6:
                    cadastrar_marca(session)

                elif opcao == 7:
                    mudar_preco(session)

                elif opcao == 8:
                    deletar(session)

                elif opcao == 9:
                    mostrar_marcas(session)

                elif opcao == 0:
                    break

                else:
                    print("\nOpção inválida.")

if __name__ == "__main__":
    main()