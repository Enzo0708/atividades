from classeStarBucks import *

def iniciar_pedido(carrinho):
    carrinho = Carrinho()
    print ("Qual o seu pedido? \n [1] Bebida \n [2] Comida")
    escolha = int(input("> "))
    if escolha == 1:
        print("Sua bebida será: \n [1] Quente \n [2] Gelada")
        escolha2 = int(input("> "))
        if escolha2 == 1:
            print("Qual será a sua bebida quente? \n [1] Chá \n [2] Café \n [3] Capuccino \n [4] chocolate Quente \n [5] Macchiato")
            escolhabq = int(input("> "))
            print("Qual será a quantidade?")
            quantidade = int(input(">"))
            if escolhabq == 1:
                produto = Cha()
                carrinho.adicionar_item(produto)
                print(f"O item foi adicionado ao carrinho")
            elif escolhabq == 2:
                cafe = Cafe()
                carrinho.adicionar_item(cafe,quantidade)
                print(f"O item foi adicionado ao carrinho")
            elif escolhabq == 3:
                capuccino = Capuccino()
                carrinho.adicionar_item(capuccino, quantidade)
                print(f"O item foi adicionado ao carrinho")
            elif escolhabq == 4:
                chocolatequente = chocolateQuente()
                carrinho.adicionar_item(chocolatequente, quantidade)
                print(f"O item foi adicionado ao carrinho") 
            elif escolhabq == 5:
                macchiato = Macchiato()
                carrinho.adicionar_item(macchiato, quantidade)
                print(f"O item foi adicionado ao carrinho")

            else:
                print("Opção inválida")             
        
        if escolha2 == 2:
            print("Qual será sua bebida gelada? \n [1] Milkshake [2] Frapuccino [3]Cha Gelado [4]ColdBrew [5]Macchiato Gelado ")
            escolhabg = int(input("> "))    
            print("Qual será a quantidade?") 
            quantidade == int(input("> "))
            
            if escolhabg == 1:
                milkshake = Milkshake()
                carrinho.adicionar_item(milkshake, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhabg == 2:
                frapuccino = Frapuccino()
                carrinho.adicionar_item(frapuccino, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhabg == 3:
                chagelado = ChaG()
                carrinho.adicionar_item(chagelado, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhabg == 4:
                coldbrew = Coldbrew()
                carrinho.adicionar_item(coldbrew, quantidade)
                print(f"O item foi adicionado ao carrinho")
            
            elif escolha == 5: 
                macchiatog = MacchiatoG()
                carrinho.adicionar_item(macchiatog, quantidade)
                print(f"O item foi adicionado ao carrinho")
                
            else:
                print("Opção inválida")
                            
    
    elif escolha == 2:
        print("Sua comida será: \n [1] Salgada \n [2] Doce")
        escolha3 = int(input("> "))
        if escolha3 == 1:
            print("Qual será sua escolha de comida salgada? \n [1] Croissant 11,50 \n [2] Pão de Queijo 13,50 \n [3] Torrada 9,00 \n [4] Coxinha 11,00 \n [5] Esfirra 11,50")
            escolhacs = int(input("> "))
            print("Qual será a quantidade?")
            quantidade = int(input(">"))
            if escolhacs == 1:
                croissant = Croissant()
                carrinho.adicionar_item(croissant, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacs == 2:
                paodequeijo = Paodequeijo()
                carrinho.adicionar_item(paodequeijo, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacs == 3:
                torrada = Torrada()
                carrinho.adicionar_item(torrada, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacs == 4:
                coxinha = Coxinha()
                carrinho.adicionar_item(coxinha, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacs == 5:
                esfirra = Esfirra()
                carrinho.adicionar_item(esfirra, quantidade)
                print(f"O item foi adicionado ao carrinho")

            else:
                print("Opção inválida")
        
        elif escolha3 == 2:
            print("Qual será sua escolha de comida doce? \n [1] Bolo \n [2] Cookie \n [3] Muffin \n [4] Donuts \n [5] Brownie")
            escolhacd = int(input("> "))
            print("Qual será a quantidade?") 
            quantidade = int(input("> "))
            if escolhacd == 1:
                bolo = Bolo()
                carrinho.adicionar_item(bolo, quantidade)
                print(f"O item foi adicionado ao carrinho")
                
            elif escolhacd == 2:
                cookie = Cookie()
                carrinho.adicionar_item(cookie, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacd == 3:
                muffin = Muffin()
                carrinho.adicionar_item(muffin, quantidade)
                print(f"O item foi adicionado ao carrinho")

            elif escolhacd == 4:
                donuts = Donuts()
                carrinho.adicionar_item(donuts, quantidade)
                print(f"O item foi adicionado ao carrinho")
                
            elif escolhacd == 5:
                brownie = Brownie()
                carrinho.adicionar_item(brownie, quantidade)
                print(f"O item foi adicionado ao carrinho")

            else:
                print("Opção inválida")
                
    else:
        print("Opção inválida")
    
def visualizar_carrinho(carrinho):
    carrinho.mostrar_carrinho()

def main():
    carrinho = Carrinho()
    while True:
        print("Bem vindo ao Starbucks, faça o seu pedido")
        iniciar_pedido(carrinho)
        print("O que deseja fazer?\n[1] Adicionar produto ao carrinho\n[2] Visualizar carrinho\n[3] Finalizar compra")
        esc = int(input("> "))
        if esc == 1:
            carrinho.adicionar_item(carrinho)  
        elif esc == 2:
            visualizar_carrinho(carrinho)
        elif esc == 3:
            total = carrinho.calcular_total()
            print(f"Total: R${total:.2f}")
            break