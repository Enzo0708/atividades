class Starbucks: # super classe
    def pedido(self, nome, preço):
        self.nome = nome
        self.preço = preço
        

# ////////////////////////////////////////////////////////////////////////////////////////////////

class Carrinho(Starbucks):
    def __init__(self):
        self.produtos = {}

    def adicionar_item(self, produto, quantidade=1):
        if produto.nome in self.produtos:
            self.produtos[produto.nome] += quantidade
        else:
            self.produtos[produto.nome] = quantidade
        print(f"{quantidade}x {produto.nome} foi adicionado ao carrinho")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.produtos.items():
            total += produto.valor * quantidade
        return total

    def mostrar_carrinho(self):
        print("Carrinho de Compras:")
        for produto, quantidade in self.produtos.items():
            print(f"{quantidade}x {produto.nome} - Preço Unitário: R${produto.valor:.2f}")


# ///////////////////////////////////////////////


class Bebida(Starbucks): # classe de bebidas
    pass


#BEBIDAS QUENTES
class Quente(Bebida): # classe das bebidas quentes
    pass

class Cha(Quente): # classe filha "Chá"
    def __init__(self):
        self.valor = 11.50 # valor da bebida
        self.nome = "Chá"

class Cafe(Quente): # classe filha "Café"
    def __init__(self):
        self.valor = 10.00 # valor da bebida
        self.nome = "Café"
        

class Capuccino(Quente): # classe filha "Capuccino"
    def __init__(self):
        self.valor = 12.65 # valor da bebida
        self.nome = "Capuccino"
        

class chocolateQuente(Quente): # classe filha "Chocolate Quente"
    def __init__(self):
        self.valor = 13,00 # valor da bebida
        self.nome = "Chocolate Quente"
        

class Macchiato(Quente): # classe filha "Macchiato"
    def __init__(self):
        self.valor = 15.50 # valor da bebida
        self.nome = "Macchiato"
        

# ///////////////////////////////////////////////

#BEBIDAS GELADAS
class Gelado(Bebida): # classe das bebidas geladas
    pass

class Milkshake(Gelado): # classe filha "Milkshake"
    def __init__(self):
        self.valor = 13.00 # valor da bebida
        self.nome = "Milkshake"
        
        
class Frapuccino(Gelado): # classe filha "Frapuccino"
    def __init__(self):
        self.valor = 23.50 # valor da bebida
        self.nome = "Frapuccino"
        
            
class ChaG(Gelado): # classe filha "Chá Gelado"
    def __init__(self):
        self.valor = 10.50 # valor da bebida
        self.nome = "Chá Gelado"
        
        
class Coldbrew(Gelado): # classe filha "Cold Brew"
    def __init__(self):
        self.valor = 15.50 # valor da bebida
        self.nome = "Coldbrew"
        

class MacchiatoG(Gelado): # classe filha "Macchiato Gelado"
    def __init__(self):
        self.valor = 15.50 # valor da bebida
        self.nome = "Macchiato Gelado"
        

# ////////////////////////////////////////////////////////////////////////////////////////////////


class Comida(Starbucks): # classe das comidas
    pass


# ///////////////////////////////////////////////

#SALGADOS
class Salgado(Comida): # classe dos salgados
    pass

class Coxinha(Salgado): # classe filha "Coxinha"
    def __init__(self):
        self.valor = 11.00 # valor do salgado
        self.nome = "Coxinha"
        

class Paodequeijo(Salgado): # classe filha "Pão de Queijo"
    def __init__(self):
        self.valor = 13.50 # valor do salgado
        self.nome = "Pão de Queijo"
        
class Croissant(Salgado): # classe filha "Croissant"
    def __init__(self):
        self.valor = 11.50 # valor do salgado
        self.nome = "Croissant"
        

class Torrada(Salgado): # classe filha "Torrada"
    def __init__(self):
        self.valor = 9.00 # valor do salgado
        self.nome = "Torrada"
        

class Esfirra(Salgado): # classe filha "Esfirra"
    def __init__(self):
        self.valor = 11.50 # valor do salgado
        self.nome = "Torrada"
        

# ///////////////////////////////////////////////

    
#DOCES
class Doce(Comida): # classe dos doces
    pass
    
class Bolo(Doce):# classe filha "Bolo"
    def __init__(self):
        self.valor = 16.50 # valor do doce
        self.nome = "Bolo"
        
         
class Cookie(Doce):# classe filha "Cookie"
    def __init__(self):
        self.valor = 10.00 # valor do doce 
        self.nome = "Cookie"
        

class Muffin(Doce): # classe filha "Muffin"
    def __init__(self):
        self.valor = 10,50 # valor do doce 
        self.nome = "Muffin"
        

class Donuts(Doce): # classe filha "Donuts"
    def __init__(self):
        self.valor = 11,50 # valor do doce 
        self.nome = "Donuts"
        
          
class Brownie(Doce): # classe filha "Brownie"
    def __init__(self):
        self.valor = 11.00 # valor do doce
        self.nome = "Brownie"