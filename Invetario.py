#Fremework Flet
import flet as ft
from Banco import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQ = "sqlite:///Bancopy.db"

engine = create_engine(SQ, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

#Criação da pagina
def main(page: ft.Page):

    #Titulo da pagina
    page.title = "Inventario/Cadastro"

    #Cadastro no banco
    def cadastrar(e):
        novo_produto = produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()

        print('produto salvo')
        print('produto Não salvo')

    #Valor 2
    txt_titulo = ft.Text('produto: ')
    produto = ft.TextField(label="Digite o Produto:", text_align=ft.TextAlign)

    #Valor 2
    txt_preco = ft.Text('Digite Valor do produto')
    preco = ft.TextField(value="0", label="Digite o preço", text_align=ft.TextAlign)

    #Botão de cadastrar
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_titulo,
         produto,
        txt_preco,
         preco,
        btn_produto
    )
    

ft.app(target=main)

