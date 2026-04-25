# Autor: Adriana Fraga

# Codigo sem funções 

# Calculadora sem funções 

# numero1 = float(input('Digite o primeiro número: '))
# numero2 = float(input('Digite o segundo número: '))
# soma = numero1 + numero2
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2

# print (f'O Resultado da Soma é {soma}')
# print (f'O Resultado da Subtração é {subtracao}')
# print (f'O Resultado da Multipilicação é {multiplicacao}')
# print (f'O Resultado da Divisão é {divisao}')

#codigo com funções 


# variáveis para armazenar os valores
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

# Criando a função para realizar os cálculos
def calculos(a, b):
    soma=valor1+valor2
    subtracao=valor1-valor2
    mutiplicacao=valor1*valor2
    divisao=valor1/valor2

    print("O resultado da soma é: ",soma)
    print("O resultado da subtração é: ",subtracao)
    print("O resultado da mutiplicação é: ",mutiplicacao)
    print("O resultado da divisão é: ",divisao)


# Chamando a função
calculos(valor1, valor2)