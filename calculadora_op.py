# Autor: Adriana Fraga
# função a calcular 
def calcular(a,b,op):
    return eval(f'{a}{op}{b}')


# entarda de dados
valor1 = float(input('Digite o primeiro número:'))
valor2 = float (input('Digite o segundo número:'))
op = input('Escolha a operação (+ - * /)')


# print dos resultados 
print('Resultado', calcular (valor1,valor2,op))
