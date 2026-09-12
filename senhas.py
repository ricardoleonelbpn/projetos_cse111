MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", '"', '"', ",", ".", "<", ">", "?", "/", "`", "~"]

def procurar_palavra(palavra, nome_do_arquivo, maiusculas_e_minusculas=False):

    with open(nome_do_arquivo, "r", encoding="utf8") as arquivo:        
        for linha in arquivo:
            linha_limpa = linha.strip()
            if maiusculas_e_minusculas:
                if palavra == linha_limpa:
                    return True
            else:
                if palavra.lower() == linha_limpa.lower():
                    return True
        return False

def palavra_tem_caractere(palavra, lista_caractere):
    for caractere in palavra:
        if caractere in lista_caractere:
            return True
    return False
    
def calcular_complexidade(palavra):
    contador = 0

    if palavra_tem_caractere(palavra, MINUSCULAS):
        contador +=1
    if palavra_tem_caractere(palavra, MAIUSCULAS):
        contador +=1
    if palavra_tem_caractere(palavra, DIGITOS):
        contador +=1
    if palavra_tem_caractere(palavra, ESPECIAIS):
        contador +=1
    return contador

def validar_senha(senha, comprimento_min=10, comprimento_forte=16):

    if procurar_palavra(senha, "dicionario.txt"):
        print("A senha está no dicionário e não é segura.")
        return 0 

    if procurar_palavra(senha, "senhas_mais_comuns.txt", maiusculas_e_minusculas=True):
        print("A senha é comumente usada e não é segura.")
        return 0 

    
    if len(senha) < comprimento_min:
        print("A senha é muito curta e não é segura.")
        return 1

    if len(senha) >= comprimento_forte:
        print("A senha é longa, o comprimento supera a complexidade e é uma boa senha.")
        return 5

    força_complexidade = calcular_complexidade(senha)
    força = força_complexidade + 1
    return força

def main():

    senha = input("Digite a senha: ")

    while senha != "q" and senha != "Q":
        força = validar_senha(senha)
        print(f"A força da senha é: {força} ")
        
        senha = input("Digite outra senha: ")

if __name__ == "__main__":
    main()