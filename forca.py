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
def kick_word():
    chute = input("Qual a Letra? -- ")
    chute = chute.strip().upper()
    return chute
def correct_kick_mark(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
def winner_mensage():
    print("yay You write the correct word, congrats!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def loser_mensage(palavra_secreta):
    print("hahahah you don't hit it")
    print("The Word was {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def dying_player(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7 - erros))
        print()
    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7 - erros))
        print("U'll goona dye my boy, don't run")
        print()
    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7 - erros))
        print("Almost a half of your body")
        print()
    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7 - erros))
        print("hahahaha U don't kwon how it's that word hahaha")
        print()
    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7 - erros))
        print()
    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print(" |            ")
        print("_|___         ")
        print("Oh no its a wrong word you have {} attempts remaining".format(7- erros))
        print("give up, will be better")
        print()
    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print("oh Gosh you are so bad, what a shame")
        print()
def jogar():

    open_menssage()

    palavra_secreta = secret_word_function()

    letras_acertadas = correct_letters(palavra_secreta)
    print (letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0


    while(not acertou and not enforcou):

        chute = kick_word()

        if (chute in palavra_secreta):
            correct_kick_mark(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1

            dying_player(erros)

        enforcou = erros  == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
       winner_mensage()
    else:
        loser_mensage(palavra_secreta)

if(__name__ == "__main__"):
    jogar()
