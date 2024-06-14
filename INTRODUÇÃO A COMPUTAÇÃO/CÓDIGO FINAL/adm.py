import secaoprodutos
import material
import os

def adicionarProduto():
    for key in secaoprodutos.getSecoes().keys():
        print(key)
    
    secao = input("Para qual secao gostaria de adicionar o produto? ").upper()
    nomeProduto = input("Nome do produto: ")
    quantidade = int(input("Quantidade no estoque: "))
    preco = float(input('Digite o preco do produto'))
    codigo = input("Digite o numero do codigo: ")
    peso = float(input('digite o peso '))

    material.adicionarMaterial(codigo, secao, nomeProduto, quantidade, preco,peso)
    secaoprodutos.adicionarItem(secao, codigo, nomeProduto)

    input("Pressione enter para voltar ao menu")

def removerProduto():
    for key, value in material.getAlmoxarifado().items():
        produtoNome = value.get("nome")
        print(f"Codigo: {key} - Nome: {produtoNome}") 
    
    codigo = input("Digite o codigo do produto a ser removido: ")

    almoxarifado = material.getAlmoxarifado()
    nomeSecao = almoxarifado[codigo].get("secao")

    secaoprodutos.removerItem(nomeSecao, codigo)
    material.removerProduto(codigo)

    input("Pressione enter para voltar ao menu")
