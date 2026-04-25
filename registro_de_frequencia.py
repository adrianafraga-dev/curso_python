alunos = []
# Pergunta a quantiddade

qtde = int(input("Quantos alunos temos hoje?"))

# Laço de repetição e armazenamento

for i in range (qtde):
    nome = input(f"Digite o nome do Aluno{i + 1}")
    alunos.append (nome)


#Saída

print ("----Lista de presença---")

for lista_nome in alunos:
    print (f" - {lista_nome} ")
     