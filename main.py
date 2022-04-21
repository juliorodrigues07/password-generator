from Cryptodome.Random import random
import string
import sys

# Conjunto de caracteres:
characters = ["", "", "", ""]
characters[0] = string.ascii_lowercase
characters[1] = string.ascii_uppercase
characters[2] = string.digits
characters[3] = string.punctuation


def password_complexity():

    levels = []

    for i in range(0, 4):
        option = input()

        if (int(option) >= 0) and (int(option) <= 3):
            levels += option
        else:
            break

    if not levels:
        print("Impossível gerar a senha! \n")
        sys.exit()

    return levels


def password_generator(levels, size):

    gen_list = []
    password = ""

    for i in range(0, len(levels)):
        j = int(levels[i])
        gen_list += characters[j]

    for i in range(0, size):
        password += random.choice(gen_list)

    return password


def main():

    size = int(input("Digite o tamanho da senha: \n"))

    while size <= 0:
        print("Tamanho inválido! \n")
        size = int(input("Digite o tamanho da senha: \n"))

    print("Informe a composição da senha:    (Um dígito por linha) \n\n"
          "0 - Letras Minúsculas             (a - z) \n"
          "1 - Letras Maiúsculas             (A - Z) \n"
          "2 - Algarismos                    (0 - 9) \n"
          "3 - Caracteres Especiais          (# - %) \n"
          "100 - Gerar senha \n")

    level = password_complexity()
    password = password_generator(level, size)
    print(password)


main()
