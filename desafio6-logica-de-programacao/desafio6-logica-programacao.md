# Desafio de Projeto 6

## Lógica de Programação

programa
{
    funcao registro()
    {
        caractere nome, turma
        real nota
        inteiro totAlunos = 0

		faca
		{
            escreva("Informe seu nome: ")
            leia(nome)
            escreva("Informe sua turma: ")
            leia(turma)
            escreva("Informe sua nota: ")
            leia(nota)
            limpa()
      	}
      	enquanto(totAlunos <= 100)
      	
      	se (nota >= 7)
      	{
      		escreva("Aluno aprovado!")
      	}
    }
}

Não consegui resolver.

programa {
	funcao inicio() {
	caracter nome, turma, melhor_alunoG, melhor_alunoTA, melhor_alunoTB, melhor_alunoTC, melhor_alunoTD
        real nota, maior_notaG, maior_notaTA, maior_notaTB, maior_notaTC, maior_notaTD
        inteiro tot_alunosT = 0, tot_alunos = 0, tot_aprovadosTA = 0, tot_aprovadosTB = 0, tot_aprovadosTC = 0, tot_aprovadosTD = 0, tot_aprovados = 0
        inteiro turmaA = 0, turmaB = 0, turmaC = 0, turmaD = 0

		faca
		{
            escreva("Informe seu nome: ")
            leia(nome)
            escreva("Informe sua turma: ")
            leia(turma)
            escreva("Informe sua nota: ")
            leia(nota)
            limpa()
            
            escolha (turma)
            {
                caso 1:
                    maior_notaA = nota
                    melhor_alunoA = nome
                pare
                
                caso 2:
                    maior_notaB = nota
                    melhor_alunoB = nome
                pare
                
                caso 3:
                    maior_notaC = nota
                    melhor_alunoC = nome
                pare
                
                caso 4:
                    maior_notaD = nota
                    melhor_alunoD = nome
            }
      	}
      	enquanto(tot_alunosT <= 25 e tot_alunos <= 100)
      	
      	se (nota >= 7)
      	{
      		tot_aprovados = tot_aprovados + 1
      		tot_aprovadosTA = tot_aprovadosTA + 1
      		tot_aprovadosTB = tot_aprovadosTB + 1
      		tot_aprovadosTC = tot_aprovadosTC + 1
      		tot_aprovadosTD = tot_aprovadosTD + 1
      		
      		escolha (turma)
      		{
      		    caso 1:
      		        turmaA = turmaA + 1
      		    pare
      		    
      		    caso 2:
      		        turmaB = turmaB + 1
      		    pare
      		    
      		    caso 3:
      		        turmaC = turmaC + 1
      		    pare
      		    
      		    caso 4:
      		        turmaD = turmaD + 1
      		}
      	}
      	
      	se (nota > maior_notaG)
      	{
      	    maior_notaG = nota
      	    melhor_alunoG = nome + turma
      	}
	}
}
