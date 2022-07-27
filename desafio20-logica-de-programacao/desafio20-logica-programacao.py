import pandas as pd

avaliacao_df = pd.read_csv('notas_alunos.csv', sep = ';')

media = (avaliacao_df['nota_1'] + avaliacao_df['nota_2']) / 2
avaliacao_df['media'] = media

avaliacao_df.loc[avaliacao_df['faltas'] > 5, 'situacao'] = 'Reprovado' 
avaliacao_df.loc[avaliacao_df['media'] < 7, 'situacao'] = 'Reprovado'
avaliacao_df.loc[avaliacao_df['situacao'] != 'Reprovado', 'situacao'] = 'Aprovado'

print(avaliacao_df)

print('O maior número de faltas é ' + str(avaliacao_df['faltas'].max()))
print('A média geral das notas dos alunos é ' + str(avaliacao_df['media'].mean()))
print('A maior média entre os alunos é ' + str(avaliacao_df['media'].max()))

avaliacao_df.to_csv(r'C:\Users\breno\OneDrive\Documentos\DEV\curso-softex-recife\desafio20-logica-de-programacao\alunos_situacao.csv', index = False)
print(avaliacao_df["media"])