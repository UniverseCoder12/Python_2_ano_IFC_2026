from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Receita(Base):
    __tablename__ = "tabela_receitass"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    tempo_preparo: Mapped[int] = mapped_column(Integer)
    modo_preparo: Mapped[str] = mapped_column(Text)

    ingredientes: Mapped[List["IngredienteNaReceita"]] = relationship(back_populates="receita")

'''
a Receita tem uma lista de objetos IngredienteNaReceita. 
Mas para o SQLAlchemy saber como montar essa lista automaticamente, 
ele precisa saber qual é o "outro lado" dessa relação, 
ou seja, qual atributo, dentro de IngredienteNaReceita, 
aponta "de volta" para a Receita.
Esse "outro lado" é o back_populates.'''
   

class Ingrediente(Base):
    __tablename__ = "tabela_ingredientes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))

    # lista reversa
    receitas: Mapped[List["IngredienteNaReceita"]] = relationship(back_populates="ingrediente")

class IngredienteNaReceita(Base):
    __tablename__ = "tabela_ingrediente_na_receita"

    # chave estrangeira
    ingrediente_id: Mapped[int] = mapped_column(
        ForeignKey("tabela_ingredientes.id"), 
        primary_key=True)

    # chave estrangeira
    receita_id: Mapped[int] = mapped_column(
        ForeignKey("tabela_receitass.id"), 
        primary_key=True)

    # atributos de acesso ao objeto
    # (acima só temos o "id", nesses atributos 
    # abaixo conseguimos ter acesso ao objeto "inteiro")
    ingrediente: Mapped["Ingrediente"] = relationship(
        back_populates="receitas")    
    receita: Mapped["Receita"] = relationship(
        back_populates="ingredientes")    

    unidade: Mapped[str] = mapped_column(String(250))
    quantidade: Mapped[float] = mapped_column(Float())
    
engine = create_engine("mysql+pymysql://root:@localhost:3306/meubanco")

Base.metadata.create_all(engine)

with Session(engine) as session:

  r1 = Receita(nome = "Tapioca", tempo_preparo = 30,

      modo_preparo = "Em uma tigela, coloque o polvilho e vá adicionando a água até cobrir e ficar dois dedos acima."+\
      "Deixe de um dia para o outro."+\
      "Retire toda a água com a ajuda de um pano limpo sem deixar excesso."+\
      "Vai ficar parecendo um bloco."+\
      "Esfarele essa massa com as mãos."+\
      "Passe pela peneira e acrescente o sal."+\
      "Em uma frigideira anti-aderente, modele a tapioca como uma panqueca."+\
      "Quando estiver pronta, a massa estará unida."+\
      "Não deixe escurecer."+\
      "Vire rapidamente e deixe secar do outro lado."+\
      "Deve ser retirada do fogo ainda branquinha."+\
      "Recheie a gosto.",
   )

  i1 = Ingrediente(nome = "Farinha para tapioca")
  i2 = Ingrediente(nome = "Água")
  i3 = Ingrediente(nome = "Sal")

  ir1 = IngredienteNaReceita(ingrediente = i1, 
                             receita = r1, 
                             quantidade=500, 
                             unidade="gramas")

  ir2 = IngredienteNaReceita(ingrediente = i2, 
                               receita = r1, 
                               quantidade=1, 
                               unidade="sulficiente para dar o ponto")
  
  ir3 = IngredienteNaReceita(ingrediente = i3, 
                               receita = r1, 
                               quantidade=1, 
                               unidade="a gosto")
  
  # podemos adicionar apenas a receita, que já contém 
  # todos os outros objetos
  session.add(r1)

  # salvar tudo!
  session.commit()

  print("A tabela foi criada (se não existia) e os dados da receita foram inseridos.")
  print(f"A receita chamada {r1.nome} foi salva sob o número {r1.id}.")

  print("Ingredientes da receita:")
  for item in r1.ingredientes:
    print(item.ingrediente.nome, item.quantidade, item.unidade)
