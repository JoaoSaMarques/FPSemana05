class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    


produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()