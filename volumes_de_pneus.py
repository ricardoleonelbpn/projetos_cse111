print("\n---------------- Volumes de Pneus ----------------")

# Importa as bibliotecas necessárias para realizar o cálculo do volume
# e obter a data atual do computador.
import math
from datetime import datetime

data_atual = datetime.now().strftime('%Y-%m-%d')

largura = int(input("\nDigite a largura do pneu em mm (ex: 205): "))
perfil = int(input("Digite o perfil do pneu (ex: 55): "))
diametro = int(input("Digite o diâmetro da roda em polegadas (ex: 16): "))
volume = math.pi * math.pow(largura, 2) * perfil * (largura *perfil + 2540 * diametro) / math.pow(10, 10) # Calcula o volume aproximado do pneu utilizando as medidas informadas.

pneus = [
    [195, 60, 15, 206.40],
    [205, 55, 16, 234.90],
    [215, 55, 17, 349.90],
    [225, 60, 18, 431.26]
]

encontrado = False

# Verifica se as três medidas informadas pelo usuário correspondem
# a algum dos pneus disponíveis no estoque.
if largura == pneus[0][0] and perfil == pneus[0][1] and diametro == pneus[0][2]:
    preco = pneus[0][3]
    encontrado = True
    print(f"\nO preço do pneu é: R$ {pneus[0][3]:.2f} reais.")
    print(f"O volume aproximado é: {volume:.2f} litros.")
elif largura == pneus[1][0] and perfil == pneus[1][1] and diametro == pneus[1][2]:
    preco = pneus[1][3]
    encontrado = True
    print(f"\nO preço do pneu é: R$ {pneus[1][3]:.2f} reais.")
    print(f"O volume aproximado é: {volume:.2f} litros.")
elif largura == pneus[2][0] and perfil == pneus[2][1] and diametro == pneus[2][2]:
    preco = pneus[2][3]
    encontrado = True
    print(f"\nO preço do pneu é: R$ { pneus[2][3]:.2f} reais.")
    print(f"O volume aproximado é: {volume:.2f} litros.")
elif largura == pneus[3][0] and perfil == pneus[3][1] and diametro == pneus[3][2]:
    preco = pneus[3][3]
    encontrado = True
    print(f"\nO preço do pneu é: R$ {pneus[3][3]:.2f} reais.")
    print(f"O volume aproximado é: {volume:.2f} litros.")
else:
    print("Desculpe, mas não temos pneus com essas especificações em nosso estoque.") 

telefone = ""

if encontrado:

    seguir = input("\nDeseja seguir com a compra do pneu? (S/N): ").upper()

    if seguir == "S":

        telefone = input("\nPara receber um cupom de desconto, digite seu telefone: ")

        # Verifica se o pneu escolhido faz parte dos modelos que estão
        # participando da promoção de 10% de desconto.
        if (largura == pneus[3][0] and perfil == pneus[3][1] and diametro == pneus[3][2]) or (largura == pneus[0][0] and perfil == pneus[0][1] and diametro == pneus[0][2]):

            valor_final = preco
            promo = 0.10
            desconto = preco * promo
            valor_final = preco - desconto

            print("\n-----------------Promoção------------------")
            print("\nParabéns! O aro escolhido participa da nossa promoção!") 
            print("Você ganhou 10% de desconto na compra do diametro escolhido.")
            print(f"Valor com desconto: R$ {valor_final:.2f} reais.")
        else:
            print("Obrigado por comprar conosco! Volte sempre!")
    else:
       print("\nObrigado por visitar nossa loja! Volte sempre!")
else:
    print("")

# Abre o arquivo volumes.txt no modo "a" (append),
# mantendo os registros anteriores e adicionando o novo registro ao final.
with open('volumes.txt', 'a') as arquivo:
    # Registra os dados do pneu no arquivo. 
    arquivo.write(f"{data_atual}, {largura}, {perfil}, {diametro}, {volume:.2f}, {telefone}\n") 
