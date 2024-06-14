import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pickle
import os

# Classe Produto
class Produto:
    def __init__(self, nome, quantidade, peso, preco, secao):
        self.nome = nome
        self.quantidade = quantidade
        self.peso = peso
        self.preco = preco
        self.secao = secao

    def __str__(self):
        return f"{self.nome} - Quantidade: {self.quantidade}, Peso: {self.peso}kg, Preço: R${self.preco}, Seção: {self.secao}"

# Classe Loja
class Loja:
    def __init__(self):
        self.produtos = []
        self.clientes = {}
        self.carregar_dados()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.salvar_dados()

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                self.salvar_dados()
                return True
        return False

    def listar_produtos_por_secao(self, secao):
        return [produto for produto in self.produtos if produto.secao == secao]

    def listar_secoes(self):
        secoes = set(produto.secao for produto in self.produtos)
        return list(secoes)

    def encontrar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return produto
        return None

    def salvar_dados(self):
        with open('produtos.pkl', 'wb') as f:
            pickle.dump(self.produtos, f)
        with open('clientes.pkl', 'wb') as f:
            pickle.dump(self.clientes, f)

    def carregar_dados(self):
        if os.path.exists('produtos.pkl'):
            with open('produtos.pkl', 'rb') as f:
                self.produtos = pickle.load(f)
        else:
            self.produtos = self.produtos_iniciais()
            self.salvar_dados()
        
        if os.path.exists('clientes.pkl'):
            with open('clientes.pkl', 'rb') as f:
                self.clientes = pickle.load(f)
        else:
            self.clientes = {}
            self.salvar_dados()

    def produtos_iniciais(self):
        return [
            Produto("aco", 1000, 7.4, 8.99, "CONSTRUCAO"),
            Produto("madeira", 300, 5, 12.99, "FLORESTAL"),
            Produto("gesso", 300, 40, 31.99, "OUTROS"),
            Produto("vidro", 300, 10, 49.99, "OUTROS"),
            Produto("argamassa", 350, 20, 14.99, "OUTROS"),
            Produto("tijolos", 3000, 2.2, 1.28, "CERAMICAS"),
            Produto("telhas", 2500, 2.4, 1.23, "CERAMICAS"),
            Produto("isolamentos", 100, 0.5, 17.78, "OUTROS"),
            Produto("ferro", 1500, 7.5, 25.96, "CONSTRUCAO"),
            Produto("viga", 250, 15, 755.24, "CONSTRUCAO"),
            Produto("brita", 250, 1360, 32, "CONSTRUCAO"),
            Produto("tabua", 100, 20, 33.65, "FLORESTAL"),
            Produto("concreto", 200, 8.7, 350, "CONSTRUCAO"),
            Produto("Areia", 300, 1500, 34, "CONSTRUCAO"),
            Produto("Cimento", 500, 50, 36.29, "CONSTRUCAO")
        ]

# Função para sugerir produtos mais sustentáveis
def sugerir_produto_sustentavel(nome):
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
    return sugestoes.get(nome, "Nenhuma sugestão disponível para este produto.")

# Função para exibir a interface do Administrador
def administrador_interface():
    admin_window = tk.Toplevel(root)
    admin_window.title("Administrador")

    frame = tk.Frame(admin_window)
    frame.pack(pady=10, padx=10)

    def adicionar():
        nome = simpledialog.askstring("Adicionar Produto", "Nome do Produto:")
        if nome:
            quantidade = simpledialog.askinteger("Adicionar Produto", "Quantidade em Estoque:")
            peso = simpledialog.askfloat("Adicionar Produto", "Peso do Produto (kg):")
            preco = simpledialog.askfloat("Adicionar Produto", "Preço do Produto (R$):")
            secao = simpledialog.askstring("Adicionar Produto", "Seção do Produto:")
            if quantidade is not None and peso is not None and preco is not None and secao:
                produto = Produto(nome, quantidade, peso, preco, secao)
                loja.adicionar_produto(produto)
                messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado!")

    def remover():
        nome = simpledialog.askstring("Remover Produto", "Nome do Produto:")
        if nome:
            if loja.remover_produto(nome):
                messagebox.showinfo("Sucesso", f"Produto '{nome}' removido!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado")

    add_button = tk.Button(frame, text="Adicionar Produto", command=adicionar)
    add_button.pack(pady=10)

    remove_button = tk.Button(frame, text="Remover Produto", command=remover)
    remove_button.pack(pady=10)

# Função para exibir a interface do Consumidor
def consumidor_interface():
    consumer_window = tk.Toplevel(root)
    consumer_window.title("Consumidor")

    frame = tk.Frame(consumer_window)
    frame.pack(pady=10, padx=10)

    secoes = loja.listar_secoes()
    secao_var = tk.StringVar(consumer_window)
    secao_var.set(secoes[0] if secoes else "")

    def listar():
        secao = secao_var.get()
        produtos = loja.listar_produtos_por_secao(secao)
        produtos_list = "\n".join(str(produto) for produto in produtos)
        messagebox.showinfo(f"Produtos na Seção '{secao}'", produtos_list if produtos_list else "Nenhum produto disponível")

    def comprar():
        secao = secao_var.get()
        produtos = loja.listar_produtos_por_secao(secao)
        produto_nomes = [produto.nome for produto in produtos]
        produto_nome = simpledialog.askstring("Comprar Produto", f"Nome do Produto ({', '.join(produto_nomes)}):")
        if produto_nome:
            produto = loja.encontrar_produto(produto_nome)
            if produto:
                quantidade_desejada = simpledialog.askinteger("Comprar Produto", "Quantidade Desejada:")
                if quantidade_desejada and quantidade_desejada <= produto.quantidade:
                    cliente_nome = simpledialog.askstring("Comprar Produto", "Nome do Cliente:")
                    if cliente_nome:
                        if cliente_nome in loja.clientes:
                            loja.clientes[cliente_nome] += 1
                        else:
                            loja.clientes[cliente_nome] = 1

                        preco_total = quantidade_desejada * produto.preco
                        peso_total = quantidade_desejada * produto.peso
                        produto.quantidade -= quantidade_desejada
                        loja.salvar_dados()

                        # Aplicar desconto se o cliente comprou mais de 2 vezes
                        if loja.clientes[cliente_nome] > 2:
                            desconto = 0.15 * preco_total
                            preco_total -= desconto
                            messagebox.showinfo("Promoção", f"Você ganhou um desconto de 15%! Desconto: R${desconto:.2f}")

                        # Propor transporte adicional se o peso total exceder 80 kg
                        if peso_total > 80:
                            custo_carreto = 0.10 * preco_total
                            if messagebox.askyesno("Peso Excedido", f"O peso total da compra é {peso_total}kg, o que excede o limite de 80kg.\nDeseja adicionar o transporte adicional por R${custo_carreto:.2f}?"):
                                preco_total += custo_carreto

                        messagebox.showinfo("Compra Realizada", f"Compra de {quantidade_desejada} unidade(s) do produto '{produto.nome}' realizada com sucesso!\nPreço Total: R${preco_total:.2f}\nPeso Total: {peso_total}kg")

                        # Sugerir produto sustentável
                        sugestao = sugerir_produto_sustentavel(produto.nome)
                        messagebox.showinfo("Sugestão Sustentável", sugestao)

                        # Aviso de estoque baixo
                        if produto.quantidade < 0.3 * quantidade_desejada:
                            messagebox.showwarning("Estoque Baixo", f"O produto '{produto.nome}' está com estoque baixo.")
                    else:
                        messagebox.showerror("Erro", "Nome do cliente não informado")
                else:
                    messagebox.showerror("Erro", "Quantidade desejada indisponível")
            else:
                messagebox.showerror("Erro", "Produto não encontrado")

    secao_label = tk.Label(frame, text="Selecione a Seção:")
    secao_label.pack(pady=5)
    secao_menu = ttk.Combobox(frame, textvariable=secao_var, values=secoes)
    secao_menu.pack(pady=5)

    list_button = tk.Button(frame, text="Listar Produtos", command=listar)
    list_button.pack(pady=10)

    buy_button = tk.Button(frame, text="Comprar Produto", command=comprar)
    buy_button.pack(pady=10)

# Função para sair da aplicação
def sair():
    root.destroy()

# Inicialização da Loja
loja = Loja()

# Configuração da Janela Principal
root = tk.Tk()
root.title("Loja")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

admin_button = tk.Button(frame, text="Administrador", command=administrador_interface)
admin_button.pack(pady=10)

consumer_button = tk.Button(frame, text="Consumidor", command=consumidor_interface)
consumer_button.pack(pady=10)

exit_button = tk.Button(frame, text="Sair", command=sair)
exit_button.pack(pady=10)

root.mainloop()
