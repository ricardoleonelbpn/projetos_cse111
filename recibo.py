import csv
from datetime import datetime

# Lê um arquivo CSV e cria um dicionário usando uma coluna como chave.
def ler_dicionario(filename, indice_coluna_chave):
    
    dicionario = {}

    # Abre o arquivo CSV para leitura.
    with open(filename, "rt", encoding= "utf-8") as arquivo_produtos:

        leitor = csv.reader(arquivo_produtos)
        next(leitor)

        # Adiciona cada produto ao dicionário usando seu código como chave.
        for linha in leitor:
            chave = linha[indice_coluna_chave]
            dicionario[chave] = linha
    return dicionario

def main():
    try:
        # Obtém a data e a hora atuais do computador.
        data_hora_atual = datetime.now()

        # Define os índices das colunas dos arquivos CSV.
        INDICE_CHAVE_PRODUTO = 0
        INDICE_NOME_PRODUTO = 1
        INDICE_QUANTIDADE = 1
        INDICE_VALOR = 2

        total_itens = 0
        total_compras = 0

        # Lê o catálogo de produtos e cria um dicionário.
        dic_produto = ler_dicionario("produtos.csv", 0)
        print()

        with open("pedido.csv", "rt", encoding="utf-8") as pedido:

            
            leitor = csv.reader(pedido)
            next(leitor)

            print(20*'-' + " Mercearia Dona Filó " + 20*'-')
            print()
            print(5*"-" + " Recibo " + 5*"-")

            for linha in leitor:

                if len(linha) != 0:
                    chave = linha[INDICE_CHAVE_PRODUTO]
                    produto = dic_produto[chave]
                    
                    nome_produto = produto[INDICE_NOME_PRODUTO]
                    quantidade = linha[INDICE_QUANTIDADE]
                    valor_produto = produto[INDICE_VALOR]

                print(f"Produto: {nome_produto}.") 
                print(f"Qtd: {quantidade} unidade.")
                print(f"Valor: {valor_produto} unitário.")
                print()

                quantidade = int(quantidade)
                valor_produto = float(valor_produto)
                soma = quantidade * valor_produto
                total_itens = total_itens + quantidade
                total_compras = total_compras + soma

        # Calcula o imposto de 6% sobre o subtotal.
        imposto = total_compras * 0.06
        valor_devido = total_compras + imposto

        print(f"Total de itens: {total_itens}")
        print(f"Subtotal: R$ {total_compras:.2f}")
        print(f"Imposto: R$ {imposto:.2f}")
        print(f"Total devido: R$ {valor_devido:.2f}")
        print("Obrigado por visita nossa loja!")
        print(f"Volte sempre! {data_hora_atual:%Y-%m-%d %H:%M}\n")

    except FileNotFoundError as erro_arquivo:
        print(f"Arquivo não encontrado ou diretório: {erro_arquivo}")
    except PermissionError as err_de_perm:
        print(f"Acesso não autorizado: {err_de_perm}")
    except KeyError as err_de_chave:
        print(type(err_de_chave).__name__, err_de_chave)
       
if __name__ == "__main__":
    main()