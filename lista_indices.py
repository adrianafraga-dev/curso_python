# Autor: Adriana Fraga
# Projetos: Trabalhando com Índices
# Programa que lê cinco números  e armagena em uma lista e 
# depois solicita ao usuario que escolha um numero a mostar.

numeros = [0] * 5
x = 0 

while x < 5:
    numeros[x] = int (input(f'Número {x + 1}: '))
    x = x + 1

while True : 
    escolhido = int (input('Que posição vc quer imprimir (0 para sair)'))

    if escolhido == 0:
        break 
    print (f'Vc escolheu o número: {numeros [escolhido - 1 ]} ')    

