# Autor Adriana Fraga
# Funções em Python
# Função para cálculo da área do triângulo

#Código principal
base = float(input("Valor da base: "))
altura = float(input("Valor da altura: "))

area_triangulo = (base * altura) / 2
print(f"A área do triângulo é {area_triangulo:.2f}")

def areatriangulo( b , h):
    A_triangulo = (b * h) / 2
    return A_triangulo

print ('Usando funcoes para calcular Area do Triangulo:')

print (f' A Area do Tringulo é {areatriangulo(base,altura)}')