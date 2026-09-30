from sqlalchemy import create_engine, String, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class Marca(Base):
    __tablename__ = "tabela_marcas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250))
    telefone: Mapped[str] = mapped_column(String(11))
    categoria: Mapped[str] = mapped_column(String(250))

   
class Produto(Base):
    __tablename__ = "tabela_produtos"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_marca: Mapped[int] = mapped_column(ForeignKey("tabela_marcas.id"), primary_key=True)
#   ingrediente: Mapped["Ingrediente"] = relationship(back_populates="receitas") 
    nome: Mapped[str] = mapped_column(String(250))
    preco: Mapped[float] = mapped_column(Float())
    quantidade: Mapped[int] = mapped_column(Integer)


    
engine = create_engine("mysql+pymysql://root:@localhost:3306/meubanco")

Base.metadata.create_all(engine)

with Session(engine) as session:
  session.add()

  # salvar tudo!
  session.commit()









