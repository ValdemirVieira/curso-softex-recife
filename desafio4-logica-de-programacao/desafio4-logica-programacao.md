# Desafio de Projeto 4

## Lógica de Programação

algoritmo
const registro = {
	nome, endereco, cidade, nomePai, nomeMae: caractere,
	cpf, rg, idade: inteiro,
	peso, rendaBruta: real
}

escreva("Digite seu nome: ")
leia(nome)
escreva("Informe seu endereço: ")
leia(endereco)
escreva("Qual a sua cidade? ")
leia(cidade)
escreva("Digite seu CPF: ")
leia(cpf)
escreva("Digite seu RG: ")
leia(rg)
escreva("Informe sua idade: ")
leia(idade)
escreva("Digite o nome do seu pai: ")
leia(nomePai)
escreva("Digite o nome da sua mãe: ")
leia(nomeMae)
escreva("Informe o seu peso: ")
leia(peso)
escreva("Qual sua renda bruta mensal? ")
leia(rendaBruta)

escreva(nome, "mora no endereço: ", endereco, ",", cidade, ". Cadastrado no CPF: ", cpf, ", com RG de número: ", rg, " e tem ", idade, ". O nome do seu pai é: ", nomePai, " e o nome da sua mãe é: ", nomeMae, ". Seu peso é: ", peso, " e sua renda bruta mensal é no valor de: R$", rendaBruta)