# Desafio de Projeto 18
# Lógica de Programação

def calcular_idade(nome, ano_nasc):
    ano_atual = 2022
    idade = ano_atual - ano_nasc
    idade = '{}, em 2022 você completa {} anos.'.format(nome, idade)
    return idade

nome = str(input('Insira seu nome completo: '))
err = True
while err == True:
    try:
        ano_nasc = int(input('Insira o ano do seu nascimento: '))
        if ano_nasc >= 1922 and ano_nasc <= 2021:
            print(calcular_idade(nome, ano_nasc))
            err = False
        else:
            print('O ano inserido é inválido!')
            err = True
    except:
        print('Informação inválida!')
        err = True