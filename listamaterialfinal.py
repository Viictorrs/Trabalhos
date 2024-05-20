def listaDeMateriais() -> int:
    codigo = int(input("Digite o código do produto: "))
    if codigo==1:
        print('Item selecionado: Aço')
    elif codigo==2:
        print("Item selecionado: Madeira")
    elif codigo==3:
        print("Item selecionado: Gesso")
    elif codigo==4:
        print("Item selecionado: Vidro")
    elif codigo==5:
        print("Item selecionado:Argamassa")
    elif codigo==6:
        print("Item selecionado: Tijolos")
    elif codigo==7:
        print("Item selecionado: Telhas")
    elif codigo==8:
        print("Item selecionado: Isolamentos")
    elif codigo==9:
        print("Item selecionado: Ferro")
    elif codigo==10:
        print("Item selecionado: Viga")
    elif codigo==11:
            print("Item selecionado: Brita")
    elif codigo==12:
        print("Item selecionado: Tabua")
    elif codigo==13:
        print("Item selecionado: Concreto")
    else:
        print("CÓDIGO INVÁLIDO!")

    return codigo