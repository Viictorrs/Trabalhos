import json
import secaoprodutos
import listamaterialfinal
import material
import os

almoxarifadoPath = "almoxarifado.json"

# Função para carregar o almoxarifado
def carregar_almoxarifado():
    with open(almoxarifadoPath, "r") as file:
        return json.load(file)

# Promoção dos Produtos
def promocao():
    for key, produto in material.getAlmoxarifado().items():
        produto["preco"] = produto["preco"] - 0.15 * produto["preco"]
    print("-"*42)
    print("Todos os Produtos estão sobre Promoção!")
    print("-"*42)

# Função para calcular o custo total
def calcular_custo(codigo, quantidade, desconto=0):
    almoxa = material.getAlmoxarifado()
    produto = almoxa[str(codigo)]
    preco_unitario = produto["preco"]
    preco_unitario_com_desconto = preco_unitario * (1 - desconto)
    custo_total = preco_unitario_com_desconto * quantidade

    return custo_total

# Função para calcular o peso total
def calcular_peso_total(codigo, quantidade):
    almoxa = material.getAlmoxarifado()
    produto = almoxa[str(codigo)]
    peso = produto["peso"]
    
    if produto["secao"] in ["CERAMICAS","FLORESTAL", "CONSTRUCAO", "OUTROS"]:
        peso_total = peso * quantidade
    else:  # FLORESTAL ou outros materiais com peso por m3
        peso_total = peso * quantidade
    
    return peso_total

# Função para sugerir produtos mais sustentáveis
def sugerir_produto_sustentavel(codigo):
    sugestoes = {
        "aco": "Uma alternativa mais sustentável para o aço na construção pode ser o bambu, que é renovável e tem baixo impacto ambiental.",
        "madeira": "Para substituir a madeira, você pode considerar o uso de madeira de reflorestamento certificada, que é mais sustentável.",
        "gesso": "O gesso é um material bastante utilizado, porém para um opção mais sustentável, pode-se considerar o uso de materiais como o barro.",
        "vidro": "Uma alternativa mais sustentável para o vidro na construção pode ser o uso de materiais transparentes à base de polímeros ou até mesmo painéis solares translúcidos.",
        "argamassa": "Para substituir a argamassa, você pode considerar o uso de adobes ou tijolos de barro, que são materiais mais naturais e sustentáveis.",
        "tijolos": "Em vez de tijolos convencionais, você pode considerar o uso de tijolos de solo-cimento, que são mais sustentáveis e têm menor impacto ambiental.",
        "telhas": "Uma alternativa mais sustentável para telhas de cerâmica ou metal pode ser o uso de telhados verdes, que são mais eficientes energeticamente e contribuem para a biodiversidade urbana.",
        "isolamentos": "Em vez de isolamentos convencionais, você pode considerar o uso de isolamentos feitos com materiais reciclados, como papelão ou espuma de celulose."
    }
    produto_atual = material.getAlmoxarifado().get(str(codigo)).get("nome")
    return sugestoes.get(produto_atual, "Não há sugestões disponíveis.")

# Função para atualizar o almoxarifado
def atualizar_almoxarifado(codigo, quantidade):
    if str(codigo) in material.getAlmoxarifado():
        return material.atualizarAlmoxarifado(str(codigo), quantidade)
    return True  # Para produtos que não estão gerenciados no almoxarifado

def menuConsumidor():
    os.system("clear || cls")
    # Interface com o usuário
    peso_total_acumulado = 0
    custo_total_acumulado = 0
    continuar = True
    contador_compras = 0
    desconto = 0

    secaoprodutos.mostrarSecao()

    print('Itens disponíveis no almoxarifado:')
    for i, p in material.getAlmoxarifado().items():
        print(f'{p["nome"]}: {p["quantidade"]}')

    while continuar:
        codigo = listamaterialfinal.lista_de_materiais()
        quantidade = int(input("Digite a quantidade desejada: "))

        contador_compras += 1
        if contador_compras > 2:
            desconto = 0.15
            print()
            print("-"*45)
            print("Você ganhou um desconto de 15% nos produtos!")
            print("-"*45)
            print()

        peso_total = calcular_peso_total(codigo, quantidade)
        print("-"*38)
        print(f"O peso total dos produtos é: {peso_total:.2f} kg")
        print("-"*38)

        # Calcular o custo total com o desconto
        custo_total = calcular_custo(codigo, quantidade, desconto)

        if atualizar_almoxarifado(codigo, quantidade):
            custo_total_acumulado += custo_total
            peso_total_acumulado += peso_total
            print(f"O custo total é: R$ {custo_total:.2f}")
            print(f"Custo total acumulado: R$ {custo_total_acumulado:.2f}")
            print()
            print(f"O peso dos produtos é: {peso_total:.2f}kg")

            print(f"O peso total acumulado é: {peso_total_acumulado:.2f}kg")
            
        else:
            print("Agradecemos a preferência.")

            # Sugerir produto mais sustentável
            sugestao_sustentavel = sugerir_produto_sustentavel(codigo)
            print("Para uma opção mais sustentável, você pode considerar:", sugestao_sustentavel)
        
        resposta = input("Deseja adicionar mais algum produto? (sim/não) ").lower()
        if resposta != "sim":
            continuar = False

    if peso_total_acumulado > 80:
        print("-"*100)
        frete = input("O peso total dos produtos excede 80 kg. Deseja adicionar frete de 10% ao custo total? (sim/não) ").lower()
        print("-"*100)
        if frete == "sim":
            custo_total_acumulado *= 1.10
            print()
            print("Frete adicionado ao custo total.")
            print(f"Custo total acumulado com frete: R$ {custo_total_acumulado:.2f}")
            print()

    print("Obrigado por sua compra!")
    print('\nQuantidade restante no almoxarifado após as compras:')
    for i, p in material.getAlmoxarifado().items():
        print(f'{p["nome"]}: {p["quantidade"]}')
    input("Pressione enter para voltar ao menu")
    