from Cryptodome.Random import random
import string
import sys


# Conjunto de caracteres:
characters = list()
characters.append(string.ascii_lowercase)
characters.append(string.ascii_uppercase)
characters.append(string.digits)
characters.append(string.punctuation)
max_options = 4


def password_complexity():

    levels = list()

    for i in range(max_options):
            
        try:
            option = int(input())
                
            if (int(option) >= 0) and (int(option) <= 3):
                levels.append(option)
            else:
                break

        except ValueError:
            print('Insira valores inteiros válidos!\n')

    if not levels:
        print("Impossível gerar a senha!\n")
        sys.exit()

    return levels


def password_generator(levels, size):

    gen_list = list()
    password = str()

    for i in range(len(levels)):
        j = int(levels[i])
        gen_list += characters[j]

    for i in range(size):
        password += random.choice(gen_list)

    return password


def main():

    while True:
        try:
            size = int(input("Digite o tamanho da senha: "))
            
            if size <= 0:
                print("Tamanho inválido! \n")
                continue
            else:
                break

        except ValueError:
            print('Insira valores inteiros válidos!\n')

    print("\nInforme a composição da senha:    (Um dígito por linha) \n\n"
          "0 - Letras Minúsculas             (a - z) \n"
          "1 - Letras Maiúsculas             (A - Z) \n"
          "2 - Algarismos                    (0 - 9) \n"
          "3 - Caracteres Especiais          (# - %) \n"
          "\nQualquer outra tecla ---> Gerar senha \n")

    level = password_complexity()
    password = password_generator(level, size)
    print("\nSenha gerada: " + password)


if __name__ == '__main__':
    main()
