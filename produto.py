class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    #This will add to our stock
    def adicionar_stock(self, quantidade):
        self.quantidade += quantidade
        
        #This will be used to tell you whether or not you can sell the stock
        if quantidade > 0:
            print(1)  
        else:
            print(0)
            
    #This will take away from the stock quantity
    def vender(self, quantidade):
        
        #We are only able to  sell if our current stock meets the demands
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(1)  
        else:
            print(0)  
        
    #Represents the product's information     
    def exibir_info(self):
        print(f"Item: {self.nome} {self.preco} {self.quantidade}")
    
    
produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info()