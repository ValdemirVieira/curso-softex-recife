# Desafio de Projeto 5

## Lógica de Programação

Algoritmo
function veiculo() {
  let terrestre, duasPessoas, pesado, temPedal, usaCapacete, temPassageiro, usaTrilho, andaNaPista, alto, usaCarroceria, temCobrador = "";

  if (terrestre) {
    if (duasPessoas) {
      if (pesado) {
        return "trator"
      } else if (temPedal) {
        return "bicicleta"
      }
    } else if (usaCapacete) {
      return "moto"
    } else if (temPassageiro) {
      if (usaTrilho) {
          return "trem"
      } else if (andaNaPista) {
        if (alto) {
          if (usaCarroceria) {
            return "caminhão"
          } else if (temCobrador) {
              return "ônibus"
          }
        } else if (leve) {
            return "carro"
        }
      }
    }
  }

  let aereo, precisaPular, viajaDentro, devagar, temPiloto, asasFixas, vooVertical = "";

  if (aereo) {
    if (precisaPular) {
      return "Asa Delta"
    } else if (viajaDentro) {
      if (devagar) {
        return "Balão"
      } else if (temPiloto) {
        if (asasFixas) {
          return "Avião"
        } else if (vooVertical) {
          return "Helicóptero"
        }
      }
    }
  }

  let aquatico, cobertoDagua, navegaNaAgua, temVela, temMotor, alto2, podeSerDescoberto = "";

  if (aquatico) {
    if (cobertoDagua) {
      return "Submarino"
    } else if (navegaNaAgua) {
      if (temVela) {
        return "Barco"
      } else if (temMotor) {
        if (alto2) {
          return "Navio"
        } else if (podeSerDescoberto) {
          return "Lancha"
        }
      }
    }
  }
}

console.log(veiculo())