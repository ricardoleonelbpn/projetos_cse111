import csv

def ler_dicionario(filename, indice_coluna_chave):
    
    dicionario = {}

    with open(filename, "rt", encoding= "utf-8") as arquivo_produtos:

        leitor = csv.reader(arquivo_produtos)
        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]
            dicionario[chave] = linha
    return dicionario

def main():

    dic_produto = ler_dicionario("produtos.csv", 0)
    print(dic_produto)
    print()

    with open("pedido.csv", "rt", encoding="utf-8") as pedido:

        leitor = csv.reader(pedido)
        next(leitor)

        print(5*'-' + "Itens Pedidos" + 5*'-')
        for linha in leitor:

            if len(linha) != 0:
                chave = linha[0]
                produto = dic_produto[chave]
                
                nome_produto = produto[1]
                quantidade = linha[1]
                valor_produto = produto[2]
                
                print(f"Produto: {nome_produto}.") 
                print(f"Qtd: {quantidade} unidade.")
                print(f"Valor: {valor_produto} unidade.")
                print()


if __name__ == "__main__":
    main()