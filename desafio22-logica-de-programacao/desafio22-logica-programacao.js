class Cadeira {
    constructor(qtdPernas, giratoria) {
        this.qtdPernas = qtdPernas
        this.giratoria = giratoria
    }

    girarCadeira() {
        if(this.giratoria === true) {
            console.log('Cadeira giratória!')
        } else {
            console.log('Cadeira não giratória!')
        }
    }
}

let cadeira1 = new Cadeira(4, false)
cadeira1.girarCadeira()

let cadeira2 = new Cadeira(1, true)
cadeira2.girarCadeira()

let cadeira3 = new Cadeira(3, false)
cadeira3.girarCadeira()