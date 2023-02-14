import random
def open_menssage():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def secret_word_function():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def correct_letters(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def jogar():

    open_menssage()

    palavra_secreta = secret_word_function()

    letras_acertadas = correct_letters(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    print (letras_acertadas)

    while(not acertou and not enforcou):

        chute = input ("Qual a Letra? -- ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                index += 1
        else:
            erros += 1

            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros  == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Boa! Voce acertou a palavra ;) ")
    else:
        print("Putz, tu errou tudo hein, acabaram as suas tentativas")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
