class Produto:
    pass


produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()