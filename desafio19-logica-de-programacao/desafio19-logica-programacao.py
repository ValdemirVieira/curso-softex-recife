print('Eleição iniciada!')

candidato_X = 0
candidato_Y = 0
candidato_Z = 0
votos_brancos = 0
votos_nulos = 0
encerrar = False

while encerrar == False:
    for voto in range(0, 1, 1):
      try:
        voto = int(input('Digite o número do seu candidato: '))
        if voto == 889:
          candidato_X = candidato_X + 1
        elif voto == 847:
          candidato_Y = candidato_Y + 1
        elif voto == 515:
          candidato_Z = candidato_Z + 1
        elif voto == 0:
          votos_brancos = votos_brancos + 1
        else:
          votos_nulos = votos_nulos + 1

        encerrar = int(input('Deseja encerar a votação?\nCaso SIM, digite 1 \nCaso NÃO, digite 2\n'))
      except:
        continue

    if encerrar == 2:
      encerrar = False
    elif encerrar == 1:
      if candidato_X > candidato_Y and candidato_X > candidato_Z:
        print('O Cadidado X foi eleito com ' + str(candidato_X) + ' votos!')
        print('O Candidato Y recebeu ' + str(candidato_Y) + ' votos!')
        print('O Candidato Z recebeu ' + str(candidato_Z) + ' votos!')
        print('O total de votos Brancos e Nulos foi ' + str(votos_brancos + votos_nulos))
      elif candidato_Y > candidato_X and candidato_Y > candidato_Z:
        print('O Cadidado Y foi eleito com ' + str(candidato_Y) + ' votos!')
        print('O Candidato X recebeu ' + str(candidato_X) + ' votos!')
        print('O Candidato Z recebeu ' + str(candidato_Z) + ' votos!')
        print('O total de votos Brancos e Nulos foi ' + str(votos_brancos + votos_nulos))
      elif candidato_Z > candidato_X and candidato_Z > candidato_Y:
        print('O Cadidado Z foi eleito com ' + str(candidato_Z) + ' votos!')
        print('O Candidato X recebeu ' + str(candidato_X) + ' votos!')
        print('O Candidato Y recebeu ' + str(candidato_Y) + ' votos!')
        print('O total de votos Brancos e Nulos foi ' + str(votos_brancos + votos_nulos))

print('Eleição encerrada!')