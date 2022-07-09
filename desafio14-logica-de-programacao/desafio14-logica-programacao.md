# Desafio de Projeto 14

## Lógica de Programação

inteiro qtd_rodas, qtd_pessoas;
real peso_veiculo;

se (qtd_rodas == 2 OU qtd_rodas == 3) {
	escreva("Habilitação categoria A")
} senão se (qtd_rodas == 4 E qtd_pessoas <= 8 E peso_veiculo <= 3.500) {
	escreva("Habilitação categoria B")
} senão se (qtd_rodas >= 4 E peso_veiculo >= 3.500 E peso_veiculo <= 6.000) {
	escreva("Habilitação categoria C")
} senão se (qtd_rodas >= 4 E qtd_pessoas > 8) {
	escreva("Habilitação categoria D")
} senão se (qtd_rodas >= 4 E peso_veiculo > 6.000) {
	escreva("Habilitação categoria E")
}