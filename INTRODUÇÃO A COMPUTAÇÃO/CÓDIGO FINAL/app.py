import os
from projetointegrado import menuConsumidor
import adm
import sys

def menu():
    while True:
        os.system("clear || cls")
        menuOptions = {
            "1": ["adminstrador", menuAdmin],
            "2": ["consumidor", menuConsumidor],
            "3": ["sair", sys.exit]
        }

        print("Menu")
        for key, value in menuOptions.items():
            print(f"{key} - {value[0]}")

        escolha = input("Digite a opcao: ")

       # try:
        opcao = menuOptions[escolha]
        opcao[1]()
       # except Exception:
        #    pass

def menuAdmin():
    os.system("clear || cls")
    print("Menu Administrador")
    menuOptions = {
            "1": ["Adicionar produto", adm.adicionarProduto],
            "2": ["Remover produto", adm.removerProduto]
        }

    for key, value in menuOptions.items():
        print(f"{key} - {value[0]}")

    escolha = input("Digite a opcao: ")

   # try:
    opcao = menuOptions[escolha]
    opcao[1]()
    #except Exception:
        #pass

if __name__ == "__main__":
    menu()
