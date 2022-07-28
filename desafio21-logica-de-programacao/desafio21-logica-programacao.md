# Desafio de Projeto 21 

## Lógica de Programação OO


#### Objetos Materiais

class Pessoa {
	constructor() {
		this.nome
		this.idade
		this.sexo
	}
	
	falar() {}
	
	andar() {}
	
	trabalhar() {}
}

class controleRemoto {
	constructor() {
		this.marca
		this.pilhas
		this.tamanho
	}
	
	ligarDesligar() {}
	
	mudarCanal() {}
	
	aumDimVolume() {}
}

#### Objetos Abstratos

class ContaBancaria {
	constructor() {
		this.agencia
		this.numeroConta
		this.saldo
	}
	
	depositar(valorDeposito) {}
	
	sacar(valorSaque) {}
	
	consultarSaldo() {}
}

class Produto {
	constructor() {
		this.nome
		this.descricao
		this.valor
	}
	
	verProduto() {}
	
	comprarProduto() {}
	
	trocarProduto() {}
}