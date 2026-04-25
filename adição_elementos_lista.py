# Autor: Adriana Fraga
# Projeto: Adicionar elementos na lista
# A principal vantagem de usar lista é poder adicionara novos 
# elementos durante a execução de outto programa.
# Para adicionarmos um elemnto no fim da lista, usaremos o append

L = []

L.append('a')
print('Valor gravado na Lista')
print (L)

L.append('b')
L.append('C')

print ('A lista final é:', L) 

print ('#' * 10)

L = [0]

while True:
    n = int(input('Digite um número (0 para sair)'))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len (L):
    print (L[x])
    x = x + 1