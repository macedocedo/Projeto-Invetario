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

    #Lista (Banco)
    lista_produtos = ft.ListView()

    #Cadastro no banco
    def cadastrar(e):
        novo_produto = Produto(titulo=produto.value, preco=preco.value)
        session.add(novo_produto)
        session.commit()
        lista_produtos.controls.append( ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )
        page.update()
        print('salvo!')

    #Valor 2
    txt_titulo = ft.Text('Produto:')
    produto = ft.TextField(label="Digite o Produto:", text_align=ft.TextAlign)

    #Valor 2
    txt_preco = ft.Text('Digite Valor do produto')
    preco = ft.TextField(value="", label="Digite o preço", text_align=ft.TextAlign)

    #Botão de cadastrar
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    page.add(
        txt_titulo,
         produto,
        txt_preco,
         preco,
        btn_produto
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

        page.add(
            lista_produtos,
    )
    

ft.app(target=main)

