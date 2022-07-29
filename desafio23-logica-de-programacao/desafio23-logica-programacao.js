class Livro {
    constructor(titulo, autor, totPag) {
        this._titulo = titulo
        this._autor = autor
        this._totPag = totPag
        this.pagAtual = 0
    }

    get titulo() {
        return this._titulo
    }

    get autor() {
        return this._autor
    }

    get totPag() {
        return this._totPag
    }

    set titulo(tituloL) {
        this._titulo = tituloL
    }

    set autor(autor) {
        this._autor = autor
    }

    set totPag(totPag) {
        this._totPag = totPag
    }

    folhear(pag) {
        if(pag > this._totPag) {
            this.pagAtual = 0
        } else {
            this.pagAtual = pag
        }
    }
}

let livro1 = new Livro('JavaScript Básico', 'José da Silva', 300)
let liro2 = new Livro('JavaScript Intermediário', 'Maria dos santos', 500)
let livro3 = new Livro('JavaScript Avançado', 'João Maria', 800)

livro1.folhear(81)
console.log(livro1)